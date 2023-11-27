# Conversor de M4A a WAV

Este script en Python facilita la conversión de archivos M4A a WAV en lotes utilizando `ffmpeg`. 

## Requisitos

- Python 3.x
- [ffmpeg](https://ffmpeg.org/download.html) instalado en el sistema

## Instalación de ffmpeg

Asegurate de tener `ffmpeg` instalado en tu sistema. Podes bajarlo desde [ffmpeg.org](https://ffmpeg.org/download.html) o Homebrew en macOS.

En macOS, puedes instalar `ffmpeg` con Homebrew ejecutando el siguiente comando en la terminal:

```bash
brew install ffmpeg
```

Uso del Script
Descarga o clona este repositorio en tu máquina local.

Abre una terminal y navega al directorio donde guardaste el repositorio.

Ejecuta el script convert.py:

```bash
python convert.py
```

Se te pedirá que ingreses la ruta del directorio que contiene tus archivos M4A. Ingresa la ruta y presiona Enter.

El script recorrerá cada carpeta, buscará archivos M4A, y los convertirá a archivos WAV. Los archivos WAV se guardarán en una carpeta llamada "WAV" dentro de cada directorio.

Nota: Si ya existe una carpeta "WAV" en un directorio, ese directorio se omitirá.
