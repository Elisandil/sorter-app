"""
Módulo principal de lógica de negocio.

Contiene las funciones para escanear directorios, organizar archivos
y gestionar las extensiones soportadas.
"""

import os
import shutil
from sorter.strings import EXTENSIONS


def scan_directory(path):
    """
    Escanea un directorio y cuenta los archivos por extensión.
    
    Args:
        path (str): Ruta del directorio a escanear.
    
    Returns:
        dict: Diccionario con extensiones como claves y información sobre
              los archivos encontrados (count, files, category).
    
    Raises:
        PermissionError: Si no hay permisos para acceder al directorio.
        OSError: Si ocurre un error al acceder al sistema de archivos.
    """
    if not os.path.exists(path):
        return {}
    
    results = {}
    
    try:
        for root, _, files in os.walk(path):
            if root != path:
                continue
                
            for file in files:
                ext = _get_file_extension(file)
                if ext in EXTENSIONS:
                    _add_file_to_results(results, ext, file)
                    
    except PermissionError:
        raise PermissionError(f"No hay permisos para acceder a: {path}")
    except OSError as e:
        raise OSError(f"Error al acceder al directorio: {str(e)}")
    
    return results


def sort_files(path, selected_extensions, progress_callback=None):
    """
    Organiza los archivos en carpetas según sus extensiones.
    
    Args:
        path (str): Ruta del directorio donde organizar los archivos.
        selected_extensions (list): Lista de extensiones a organizar.
        progress_callback (callable, optional): Función a llamar para actualizar el progreso.
                                              Debe aceptar (current, total).
    
    Note:
        Si un archivo ya existe en el destino, se le añade un sufijo numérico.
    
    Raises:
        PermissionError: Si no hay permisos para mover archivos.
        OSError: Si ocurre un error al mover archivos (disco lleno, archivo en uso, etc.).
    """
    if not os.path.exists(path):
        return

    files_to_move = _get_files_to_process(path, selected_extensions)
    total_files = len(files_to_move)
    errors = []
    
    for i, file in enumerate(files_to_move):
        _update_progress(progress_callback, i, total_files)
        
        error = _move_file_to_category(file, path)
        if error:
            errors.append(error)
    
    _update_progress(progress_callback, total_files, total_files)
    
    if errors:
        _raise_move_errors(errors)


def get_all_extensions():
    """
    Obtiene todas las extensiones soportadas.
    
    Returns:
        list: Lista ordenada de extensiones de archivo soportadas.
    """
    return sorted(list(EXTENSIONS.keys()))


def get_extensions_by_category():
    """
    Agrupa las extensiones por su categoría.
    
    Returns:
        dict: Diccionario con categorías como claves y listas de extensiones como valores.
    """
    categories = {}
    
    for ext, category in EXTENSIONS.items():
        if category not in categories:
            categories[category] = []
        categories[category].append(ext)
    
    for category in categories:
        categories[category].sort()
    
    return dict(sorted(categories.items()))


# Funciones privadas auxiliares

def _get_file_extension(filename):
    """Extrae y normaliza la extensión de un archivo."""
    _, ext = os.path.splitext(filename)
    return ext.lower()


def _add_file_to_results(results, ext, filename):
    """Añade un archivo a los resultados del escaneo."""
    if ext not in results:
        results[ext] = {
            'count': 0,
            'files': [],
            'category': EXTENSIONS[ext]
        }
    results[ext]['count'] += 1
    results[ext]['files'].append(filename)


def _get_files_to_process(path, selected_extensions):
    """Identifica los archivos que deben ser movidos."""
    files_to_move = []
    
    for file in os.listdir(path):
        if _should_process_file(path, file, selected_extensions):
            files_to_move.append(file)
    
    return files_to_move


def _should_process_file(path, file, selected_extensions):
    """Determina si un archivo debe ser procesado."""
    file_path = os.path.join(path, file)
    
    if not os.path.isfile(file_path):
        return False
    
    ext = _get_file_extension(file)
    return ext in EXTENSIONS and ext in selected_extensions


def _update_progress(callback, current, total):
    """Actualiza el progreso si hay callback disponible."""
    if callback:
        callback(current, total)


def _move_file_to_category(file, source_path):
    """
    Mueve un archivo a su carpeta de categoría.
    
    Returns:
        tuple: (filename, error_message) si hay error, None si es exitoso.
    """
    try:
        ext = _get_file_extension(file)
        folder_name = EXTENSIONS[ext]
        target_folder = os.path.join(source_path, folder_name)
        
        _ensure_folder_exists(target_folder)
        _move_file_safely(file, source_path, target_folder)
        
        return None
        
    except PermissionError:
        return (file, "Sin permisos para mover el archivo")
    except OSError as e:
        return _handle_move_error(file, e)


def _ensure_folder_exists(folder_path):
    """Crea la carpeta si no existe."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def _move_file_safely(file, source_path, target_folder):
    """Mueve un archivo manejando colisiones de nombres."""
    file_path = os.path.join(source_path, file)
    target_path = os.path.join(target_folder, file)

    if os.path.exists(target_path):
        target_path = _resolve_collision(target_folder, file)
    
    shutil.move(file_path, target_path)


def _resolve_collision(target_folder, filename):
    """Genera un nombre único para evitar sobreescribir archivos."""
    base, extension = os.path.splitext(filename)
    counter = 1
    
    while True:
        new_name = f"{base}_{counter}{extension}"
        target_path = os.path.join(target_folder, new_name)
        if not os.path.exists(target_path):
            return target_path
        counter += 1


def _handle_move_error(file, error):
    """Maneja errores específicos al mover archivos."""
    if error.errno == 32:
        return (file, "Archivo en uso por otra aplicación")
    elif error.errno == 28:
        raise OSError("No hay suficiente espacio en disco")
    else:
        return (file, str(error))


def _raise_move_errors(errors):
    """Lanza una excepción con todos los errores de movimiento."""
    error_msg = "\n".join([f"- {f}: {msg}" for f, msg in errors])
    raise OSError(f"Algunos archivos no pudieron moverse:\n{error_msg}")