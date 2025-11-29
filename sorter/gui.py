"""
Módulo de interfaz gráfica de usuario.

Contiene la clase FileSorterApp que implementa la interfaz de usuario
para la aplicación de organización de archivos usando Tkinter.
"""

import os
import tkinter as tk
import threading
from tkinter import ttk, filedialog, messagebox
from sorter.core import scan_directory, sort_files, get_extensions_by_category
from sorter import strings as txt


class FileSorterApp:
    """
    Aplicación principal de organización de archivos.
    
    Proporciona una interfaz gráfica para escanear directorios,
    seleccionar tipos de archivos y organizarlos en carpetas.
    """
    
    def __init__(self, root):
        """
        Inicializa la aplicación.
        
        Args:
            root: Ventana principal de Tkinter.
        """
        self.root = root
        self._configure_window()
        
        self.path_var = tk.StringVar()
        self.check_vars = {} 
        self.is_sorting = False
        
        self.create_widgets()
        self.populate_checkboxes()
    
    def _configure_window(self):
        """Configura las propiedades de la ventana principal."""
        self.root.title(txt.WINDOW_TITLE)
        self.root.geometry(txt.WINDOW_GEOMETRY)
        self.root.resizable(False, False)
    
    def create_widgets(self):
        """Crea todos los widgets de la interfaz gráfica."""
        self._create_layout_containers()
        self._create_path_section()
        self._create_extensions_section()
        self._create_actions_section()
        self._create_progress_section()
    
    def _create_layout_containers(self):
        """Crea los contenedores principales del layout."""
        self.path_frame = tk.Frame(self.root, pady=20)
        self.path_frame.pack(fill=tk.X, padx=20)
        
        self.extensions_frame = tk.Frame(self.root, bd=2, relief=tk.GROOVE)
        self.extensions_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.actions_frame = tk.Frame(self.root, pady=20)
        self.actions_frame.pack(fill=tk.X, padx=20)
    
    def _create_path_section(self):
        """Crea la sección de selección de ruta."""
        tk.Label(self.path_frame, text=txt.LABEL_PATH).pack(anchor=tk.W)
        
        entry_frame = tk.Frame(self.path_frame)
        entry_frame.pack(fill=tk.X, pady=5)
        
        self.path_entry = tk.Entry(entry_frame, textvariable=self.path_var)
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.path_entry.bind('<FocusOut>', self.on_path_change)
        self.path_entry.bind('<Return>', self.on_path_change)
        
        browse_btn = tk.Button(
            entry_frame,
            text=txt.BTN_BROWSE,
            command=self.browse_directory
        )
        browse_btn.pack(side=tk.RIGHT, padx=(5, 0))
    
    def _create_extensions_section(self):
        """Crea la sección de selección de extensiones."""
        tk.Label(
            self.root,
            text=txt.LABEL_FILE_TYPES,
            bg=self.root.cget('bg')
        ).place(in_=self.extensions_frame, rely=0, relx=0, y=-20, anchor="sw")
        
        self.canvas = tk.Canvas(self.extensions_frame)
        scrollbar = tk.Scrollbar(
            self.extensions_frame,
            orient="vertical",
            command=self.canvas.yview
        )
        self.checkbox_frame = tk.Frame(self.canvas)
        
        self.checkbox_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.checkbox_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
    
    def _create_actions_section(self):
        """Crea la sección de botones de acción."""
        btn_container = tk.Frame(self.actions_frame)
        btn_container.pack(anchor='center')

        self.execute_btn = tk.Button(
            btn_container,
            text=txt.BTN_EXECUTE,
            command=self.execute_sort,
            bg=txt.COLOR_EXECUTE_BG,
            fg=txt.COLOR_EXECUTE_FG,
            width=15
        )
        self.execute_btn.pack(side=tk.LEFT, padx=5)
        
        self.reset_btn = tk.Button(
            btn_container,
            text=txt.BTN_RESET,
            command=self.clear_all,
            width=15
        )
        self.reset_btn.pack(side=tk.LEFT, padx=5)
    
    def _create_progress_section(self):
        """Crea la barra de progreso."""
        self.progress = ttk.Progressbar(
            self.root,
            orient=tk.HORIZONTAL,
            mode='determinate'
        )
        self.progress.pack(fill=tk.X, padx=20, pady=(0, 20))
    
    def populate_checkboxes(self):
        """Llena el área de checkboxes con todas las extensiones disponibles."""
        self._clear_checkboxes()
        
        categories_dict = get_extensions_by_category()
        container = self._create_checkbox_container()
        
        current_row = 0
        for category_name, extensions in categories_dict.items():
            current_row = self._add_category_section(
                container,
                category_name,
                extensions,
                current_row
            )
    
    def _clear_checkboxes(self):
        """Limpia todos los checkboxes existentes."""
        for widget in self.checkbox_frame.winfo_children():
            widget.destroy()
        self.check_vars.clear()
    
    def _create_checkbox_container(self):
        """Crea el contenedor para los checkboxes."""
        container = tk.Frame(self.checkbox_frame)
        container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5, anchor='nw')
        return container
    
    def _add_category_section(self, container, category_name, extensions, start_row):
        """
        Añade una sección de categoría con sus checkboxes.
        
        Returns:
            int: La siguiente fila disponible.
        """
        current_row = self._add_category_label(container, category_name, start_row)
        current_row = self._add_category_checkboxes(container, extensions, current_row)
        return current_row
    
    def _add_category_label(self, container, category_name, row):
        """Añade la etiqueta de una categoría."""
        category_label = tk.Label(
            container,
            text=f"{category_name}:",
            font=('Arial', 10, 'bold')
        )
        category_label.grid(
            row=row,
            column=0,
            columnspan=txt.MAX_COLUMNS_CHECKBOXES,
            sticky='w',
            padx=5,
            pady=(10, 5)
        )
        return row + 1
    
    def _add_category_checkboxes(self, container, extensions, start_row):
        """
        Añade los checkboxes de una categoría en cuadrícula.
        
        Returns:
            int: La siguiente fila disponible.
        """
        max_cols = txt.MAX_COLUMNS_CHECKBOXES
        
        for i, ext in enumerate(extensions):
            row = start_row + (i // max_cols)
            col = i % max_cols
            
            var = tk.BooleanVar(value=False)
            self.check_vars[ext] = var
            
            cb = tk.Checkbutton(container, text=ext, variable=var)
            cb.grid(row=row, column=col, sticky='w', padx=10, pady=2)
        
        rows_used = (len(extensions) + max_cols - 1) // max_cols
        return start_row + rows_used
    
    def _on_mousewheel(self, event):
        """Maneja el evento de scroll con la rueda del ratón."""
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    
    def browse_directory(self):
        """Abre un diálogo para seleccionar un directorio."""
        directory = filedialog.askdirectory()
        if directory:
            self.path_var.set(directory)
            self.scan_and_update_ui(directory)
    
    def on_path_change(self, event=None):
        """Maneja el evento de cambio en el campo de ruta."""
        path = self.path_var.get()
        if os.path.isdir(path):
            self.scan_and_update_ui(path)
    
    def scan_and_update_ui(self, path):
        """Escanea el directorio y actualiza la interfaz con los resultados."""
        try:
            results = scan_directory(path)
            self._update_checkboxes_from_scan(results)
        except PermissionError:
            self._show_permission_error(path)
        except OSError as e:
            self._show_scan_error(e)
    
    def _update_checkboxes_from_scan(self, results):
        """Actualiza los checkboxes basándose en los resultados del escaneo."""
        self._uncheck_all()
        
        if results:
            for extension in results.keys():
                if extension in self.check_vars:
                    self.check_vars[extension].set(True)
    
    def _uncheck_all(self):
        """Desmarca todos los checkboxes."""
        for var in self.check_vars.values():
            var.set(False)
    
    def _show_permission_error(self, path):
        """Muestra error de permisos."""
        messagebox.showerror(
            txt.ERROR_TITLE,
            txt.ERROR_PERMISSION_DENIED.format(path)
        )
    
    def _show_scan_error(self, error):
        """Muestra error de escaneo."""
        messagebox.showerror(
            txt.ERROR_TITLE,
            txt.ERROR_SCAN_FAILED.format(str(error))
        )
    
    def execute_sort(self):
        """Ejecuta la organización de archivos según las extensiones seleccionadas."""
        if not self._validate_execution():
            return
        
        path = self.path_var.get()
        selected_types = self._get_selected_extensions()
        
        self._start_sorting(path, selected_types)
    
    def _validate_execution(self):
        """
        Valida que se puede ejecutar la organización.
        
        Returns:
            bool: True si es válido, False en caso contrario.
        """
        path = self.path_var.get()
        
        if not path or not os.path.isdir(path):
            messagebox.showerror(txt.ERROR_TITLE, txt.ERROR_INVALID_PATH)
            return False
        
        if not self._get_selected_extensions():
            messagebox.showwarning(txt.WARNING_TITLE, txt.WARNING_NO_SELECTION)
            return False
        
        if self.is_sorting:
            return False
        
        return True
    
    def _get_selected_extensions(self):
        """Obtiene las extensiones seleccionadas."""
        return [name for name, var in self.check_vars.items() if var.get()]
    
    def _start_sorting(self, path, selected_types):
        """Inicia el proceso de organización en un hilo separado."""
        self._set_sorting_state(True)
        
        thread = threading.Thread(
            target=self._run_sort_thread,
            args=(path, selected_types)
        )
        thread.daemon = True
        thread.start()
    
    def _set_sorting_state(self, is_sorting):
        """Establece el estado de ordenación y actualiza la UI."""
        self.is_sorting = is_sorting
        state = tk.DISABLED if is_sorting else tk.NORMAL
        self.execute_btn.config(state=state)
        self.reset_btn.config(state=state)
    
    def _run_sort_thread(self, path, selected_types):
        """Ejecuta la lógica de ordenación en un hilo separado."""
        try:
            self._reset_progress()
            sort_files(path, selected_types, progress_callback=self._update_progress)
            self._on_sort_success(path)
        except PermissionError:
            self._on_sort_error(path, txt.ERROR_PERMISSION_DENIED.format(path))
        except OSError as e:
            self._on_sort_error(path, self._get_error_message(e))
        except Exception as e:
            self._on_sort_error(path, txt.ERROR_ORGANIZING.format(str(e)))
    
    def _reset_progress(self):
        """Resetea la barra de progreso."""
        self.root.after(0, lambda: self.progress.configure(value=0))
    
    def _update_progress(self, current, total):
        """Actualiza la barra de progreso."""
        if total > 0:
            progress_val = (current / total) * 100
            self.root.after(0, lambda: self.progress.configure(value=progress_val))
    
    def _get_error_message(self, error):
        """Obtiene el mensaje de error apropiado."""
        error_str = str(error)
        
        if "espacio" in error_str.lower():
            return txt.ERROR_DISK_FULL
        elif "uso" in error_str.lower():
            return error_str
        else:
            return txt.ERROR_ORGANIZING.format(error_str)
    
    def _on_sort_success(self, path):
        """Maneja el éxito de la organización."""
        self.root.after(0, lambda: self._on_sort_complete(True, path))
    
    def _on_sort_error(self, path, error_message):
        """Maneja el error de la organización."""
        self.root.after(0, lambda: self._on_sort_complete(False, path, error_message))
    
    def _on_sort_complete(self, success, path, error_message=None):
        """Maneja la finalización del proceso de ordenación en el hilo principal."""
        self._set_sorting_state(False)
        
        if success:
            self._show_success()
        else:
            self._show_error(error_message)
        
        self.scan_and_update_ui(path)
    
    def _show_success(self):
        """Muestra mensaje de éxito."""
        self.progress['value'] = 100
        messagebox.showinfo(txt.SUCCESS_TITLE, txt.SUCCESS_ORGANIZED)
    
    def _show_error(self, error_message):
        """Muestra mensaje de error."""
        self.progress['value'] = 0
        messagebox.showerror(txt.ERROR_TITLE, error_message)
    
    def clear_all(self):
        """Limpia la ruta y desmarca todos los checkboxes."""
        self.path_var.set("")
        self._uncheck_all()