"""
Módulo de constantes y configuración.

Contiene todos los textos de la interfaz, mensajes, colores y configuraciones
utilizadas en la aplicación de organización de archivos.
"""

# Textos de la interfaz
WINDOW_TITLE = "Organizador de Archivos"
WINDOW_GEOMETRY = "700x700"

# Labels
LABEL_PATH = "Ruta a organizar:"
LABEL_FILE_TYPES = "Tipos de archivos:"

# Botones
BTN_BROWSE = "📂"
BTN_EXECUTE = "Ejecutar"
BTN_RESET = "Reset"

# Colores
COLOR_EXECUTE_BG = "#4CAF50"
COLOR_EXECUTE_FG = "white"

# Mensajes de error
ERROR_TITLE = "Error"
ERROR_INVALID_PATH = "Por favor seleccione una ruta válida."
ERROR_ORGANIZING = "Ocurrió un error al organizar: {}"
ERROR_PERMISSION_DENIED = "No tiene permisos para acceder a:\n{}"
ERROR_FILE_IN_USE = "El archivo está siendo usado por otra aplicación:\n{}"
ERROR_DISK_FULL = "No hay suficiente espacio en disco."
ERROR_PATH_TOO_LONG = "La ruta es demasiado larga:\n{}"
ERROR_SCAN_FAILED = "Error al escanear el directorio:\n{}"
ERROR_MOVE_FAILED = "Error al mover el archivo '{}':\n{}"

# Mensajes de advertencia
WARNING_TITLE = "Advertencia"
WARNING_NO_SELECTION = "No ha seleccionado ningún tipo de archivo."

# Mensajes de éxito
SUCCESS_TITLE = "Éxito"
SUCCESS_ORGANIZED = "Archivos organizados correctamente."
SUCCESS_ORGANIZED_COUNT = "{} archivos organizados correctamente."

# Mensajes de progreso
PROGRESS_SCANNING = "Escaneando directorio..."
PROGRESS_ORGANIZING = "Organizando archivos... {}/{}"
PROGRESS_COMPLETE = "Completado"

# Configuración UI
MAX_COLUMNS_CHECKBOXES = 7

# Extensiones y categorías
EXTENSIONS = {
    # Imágenes
    '.jpg': 'Imágenes', '.jpeg': 'Imágenes', '.png': 'Imágenes', '.gif': 'Imágenes', 
    '.bmp': 'Imágenes', '.svg': 'Imágenes', '.ico': 'Imágenes', '.webp': 'Imágenes',
    '.tif': 'Imágenes', '.tiff': 'Imágenes', '.raw': 'Imágenes', '.cr2': 'Imágenes',
    '.nef': 'Imágenes', '.orf': 'Imágenes', '.sr2': 'Imágenes', '.heic': 'Imágenes',
    '.heif': 'Imágenes', '.psd': 'Imágenes', '.ai': 'Imágenes', '.eps': 'Imágenes',
    '.dng': 'Imágenes', '.jfif': 'Imágenes', '.avif': 'Imágenes',
    
    # Documentos
    '.pdf': 'Documentos', '.doc': 'Documentos', '.docx': 'Documentos', '.txt': 'Documentos',
    '.xls': 'Documentos', '.xlsx': 'Documentos', '.ppt': 'Documentos', '.pptx': 'Documentos',
    '.odt': 'Documentos', '.ods': 'Documentos', '.odp': 'Documentos', '.rtf': 'Documentos',
    '.tex': 'Documentos', '.wpd': 'Documentos', '.pages': 'Documentos', '.numbers': 'Documentos',
    '.key': 'Documentos', '.csv': 'Documentos', '.md': 'Documentos', '.log': 'Documentos',
    '.epub': 'Documentos', '.mobi': 'Documentos', '.azw': 'Documentos', '.azw3': 'Documentos',
    
    # Audio
    '.mp3': 'Audio', '.wav': 'Audio', '.flac': 'Audio', '.aac': 'Audio',
    '.ogg': 'Audio', '.m4a': 'Audio', '.wma': 'Audio', '.opus': 'Audio',
    '.alac': 'Audio', '.ape': 'Audio', '.aiff': 'Audio', '.aif': 'Audio',
    '.mid': 'Audio', '.midi': 'Audio', '.amr': 'Audio', '.weba': 'Audio',
    '.ra': 'Audio', '.ram': 'Audio', '.dsf': 'Audio', '.dff': 'Audio',
    
    # Video
    '.mp4': 'Video', '.avi': 'Video', '.mkv': 'Video', '.mov': 'Video',
    '.wmv': 'Video', '.flv': 'Video', '.webm': 'Video', '.m4v': 'Video',
    '.mpg': 'Video', '.mpeg': 'Video', '.3gp': 'Video', '.3g2': 'Video',
    '.f4v': 'Video', '.swf': 'Video', '.vob': 'Video', '.ogv': 'Video',
    '.ts': 'Video', '.m2ts': 'Video', '.mts': 'Video', '.divx': 'Video',
    
    # Comprimidos
    '.zip': 'Comprimidos', '.rar': 'Comprimidos', '.7z': 'Comprimidos', 
    '.tar': 'Comprimidos', '.gz': 'Comprimidos', '.bz2': 'Comprimidos',
    '.xz': 'Comprimidos', '.tgz': 'Comprimidos', '.tbz2': 'Comprimidos',
    '.zipx': 'Comprimidos', '.cab': 'Comprimidos', '.iso': 'Comprimidos',
    '.dmg': 'Comprimidos', '.pkg': 'Comprimidos', '.deb': 'Comprimidos',
    '.rpm': 'Comprimidos', '.z': 'Comprimidos', '.lz': 'Comprimidos',
    
    # Código - Lenguajes de programación
    '.py': 'Código', '.js': 'Código', '.java': 'Código', '.cpp': 'Código',
    '.c': 'Código', '.h': 'Código', '.hpp': 'Código', '.cs': 'Código',
    '.rb': 'Código', '.php': 'Código', '.swift': 'Código', '.go': 'Código',
    '.rs': 'Código', '.kt': 'Código', '.scala': 'Código', '.r': 'Código',
    '.m': 'Código', '.vb': 'Código', '.pl': 'Código', '.perl': 'Código',
    '.sh': 'Código', '.bash': 'Código', '.bat': 'Código', '.cmd': 'Código',
    '.ps1': 'Código', '.lua': 'Código', '.dart': 'Código', '.f': 'Código',
    '.f90': 'Código', '.asm': 'Código', '.s': 'Código',
    
    # Código - Web
    '.html': 'Código', '.htm': 'Código', '.css': 'Código', '.scss': 'Código',
    '.sass': 'Código', '.less': 'Código', '.jsx': 'Código', '.tsx': 'Código',
    '.ts': 'Código', '.vue': 'Código', '.svelte': 'Código', '.xml': 'Código',
    '.xhtml': 'Código', '.asp': 'Código', '.aspx': 'Código', '.jsp': 'Código',
    
    # Código - Configuración y datos
    '.json': 'Código', '.yaml': 'Código', '.yml': 'Código', '.toml': 'Código',
    '.ini': 'Código', '.cfg': 'Código', '.conf': 'Código', '.properties': 'Código',
    '.env': 'Código', '.sql': 'Código', '.db': 'Código', '.sqlite': 'Código',
    
    # Ejecutables y binarios
    '.exe': 'Ejecutables', '.msi': 'Ejecutables', '.app': 'Ejecutables',
    '.apk': 'Ejecutables', '.jar': 'Ejecutables', '.war': 'Ejecutables',
    '.dll': 'Ejecutables', '.so': 'Ejecutables', '.dylib': 'Ejecutables',
    '.bin': 'Ejecutables', '.com': 'Ejecutables', '.gadget': 'Ejecutables',
    
    # Fuentes
    '.ttf': 'Fuentes', '.otf': 'Fuentes', '.woff': 'Fuentes', '.woff2': 'Fuentes',
    '.eot': 'Fuentes', '.fon': 'Fuentes', '.fnt': 'Fuentes',
    
    # Modelos 3D y diseño
    '.obj': '3D', '.fbx': '3D', '.stl': '3D', '.dae': '3D',
    '.3ds': '3D', '.blend': '3D', '.max': '3D', '.c4d': '3D',
    '.ma': '3D', '.mb': '3D', '.skp': '3D', '.ply': '3D',
    
    # Bases de datos
    '.sqlite3': 'Bases de datos', '.mdb': 'Bases de datos', '.accdb': 'Bases de datos',
    '.frm': 'Bases de datos', '.myd': 'Bases de datos', '.myi': 'Bases de datos',
    
    # Máquinas virtuales y discos
    '.vmdk': 'Virtualización', '.vdi': 'Virtualización', '.vhd': 'Virtualización',
    '.vhdx': 'Virtualización', '.ova': 'Virtualización', '.ovf': 'Virtualización',
    
    # Otros
    '.torrent': 'Otros', '.lnk': 'Otros', '.url': 'Otros', '.webloc': 'Otros',
    '.tmp': 'Otros', '.temp': 'Otros', '.bak': 'Otros', '.old': 'Otros'
}
