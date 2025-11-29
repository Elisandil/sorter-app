"""
Punto de entrada principal de la aplicación.

Ejecuta la aplicación de organización de archivos.
"""

import tkinter as tk
from sorter.gui import FileSorterApp

def main():
    """
    Inicializa y ejecuta la aplicación.
    """
    root = tk.Tk()
    app = FileSorterApp(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()