# 📁 Organizador de Archivos

Una aplicación de escritorio simple y eficiente para organizar archivos automáticamente por tipo y extensión.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Características

- **Interfaz gráfica intuitiva** - Fácil de usar con Tkinter
- **Organización automática** - Agrupa archivos por categorías (Imágenes, Videos, Documentos, etc.)
- **200+ extensiones soportadas** - Cubre prácticamente todos los tipos de archivos
- **Seguro** - No sobreescribe archivos, añade sufijos numéricos si existen duplicados
- **Rápido y eficiente** - Procesamiento local sin necesidad de conexión
- **Categorías agrupadas** - Visualización organizada por tipo de archivo
- **Manejo robusto de errores** - Mensajes descriptivos y claros

## Categorías Soportadas

- **Imágenes**: JPG, PNG, GIF, SVG, WebP, HEIC, PSD, RAW, etc.
- **Documentos**: PDF, DOCX, XLSX, PPTX, TXT, MD, EPUB, etc.
- **Audio**: MP3, WAV, FLAC, AAC, OGG, M4A, etc.
- **Video**: MP4, AVI, MKV, MOV, WebM, FLV, etc.
- **Comprimidos**: ZIP, RAR, 7Z, TAR, GZ, ISO, etc.
- **Código**: Python, JavaScript, Java, C++, HTML, CSS, JSON, etc.
- **Ejecutables**: EXE, MSI, APK, JAR, DLL, etc.
- **Fuentes**: TTF, OTF, WOFF, WOFF2, etc.
- **3D**: OBJ, FBX, STL, Blender, etc.
- **Bases de datos**: SQLite, MDB, ACCDB, etc.
- **Y más...**

## Instalación

### Requisitos Previos

- Python 3.8 o superior
- tkinter

### Opción 1: Ejecutar desde código fuente

1. Clona el repositorio:
```bash
git clone https://github.com/Elisandil/sorter-app.git
cd SorterApp
```

2. Ejecuta la aplicación:
```bash
python main.py
```

### Opción 2: Usar el ejecutable

1. Descarga el ejecutable desde [Releases](https://github.com/Elisandil/sorter-app/releases)
2. Ejecuta `sorter_app.exe`

### Opción 3: Crear tu propio ejecutable

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "sorter_app" --icon=icon.ico main.py
```

El ejecutable se generará en la carpeta `dist/`

## Uso

1. **Selecciona un directorio**: Haz clic en 📂 o escribe la ruta del directorio que deseas organizar
2. **Escanea el directorio**: Automáticamente se detectarán las extensiones presentes
3. **Selecciona extensiones**: Marca las extensiones que deseas organizar (vienen pre-seleccionadas las encontradas)
4. **Ejecuta**: Haz clic en "Ejecutar" para organizar los archivos
5. **Listo**: Los archivos se moverán a carpetas según su categoría

### Ejemplo

**Antes:**
```
📁 Descargas/
  - foto1.jpg
  - foto2.jpg
  - documento.pdf
  - video.mp4
  - foto287.png
  - musica.mp3
  - video2.mp4
  - audio1.mp3
```

**Después:**
```
📁 Descargas/
  📁 Imágenes/
    - foto1.jpg
    - foto2.jpg
    - foto287.png
  📁 Documentos/
    - documento.pdf
  📁 Video/
    - video.mp4
    - video2.mp4
  📁 Audio/
    - musica.mp3
    - audio1.mp3
```

## Estructura del Proyecto

```
SorterApp/
├── main.py                 # Punto de entrada de la aplicación
├── sorter/
│   ├── __init__.py        # Inicialización del paquete
│   ├── core.py            # Lógica de negocio (escaneo y organización)
│   ├── gui.py             # Interfaz gráfica
│   └── strings.py         # Constantes, textos y configuración
├── assets/
│   └── icon.ico           # Icono de la aplicación
└── README.md
```

## Características Técnicas

- **Manejo de duplicados**: Si un archivo ya existe en el destino, se renombra con sufijo `_1`, `_2`, etc.
- **Carpetas existentes**: Si la carpeta de destino ya existe, se reutiliza sin problemas
- **Seguridad**: Solo mueve archivos con extensiones seleccionadas
- **Permisos**: Maneja correctamente errores de permisos y archivos en uso
- **Scroll automático**: Interfaz con scroll para visualizar todas las extensiones

## Solución de Problemas

### Error: "No tiene permisos para acceder"
- Ejecuta la aplicación como administrador
- Verifica que tienes permisos de lectura/escritura en el directorio

### Error: "El archivo está siendo usado por otra aplicación"
- Cierra cualquier programa que esté usando los archivos
- Intenta de nuevo

### Los archivos no se mueven
- Asegúrate de marcar las extensiones que deseas organizar
- Verifica que la ruta del directorio sea correcta

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## Autor

**Antonio Ortega**

---

⭐ Si te gusta este proyecto, dale una estrella en GitHub!
