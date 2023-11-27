# Procesamiento de Audio
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

# Conversor y Combinador a Estéreo de Archivos WAV

Este script de Python utiliza Praat para combinar archivos WAV a estéreo. Los archivos WAV deben estar organizados en carpetas individuales dentro de un directorio principal.

## Requisitos

- Python 3.x
- Praat instalado en el sistema

## Instalación de Praat

Asegurate de tener Praat instalado en tu sistema. Podes descargarlo desde [el sitio web oficial de Praat](https://www.fon.hum.uva.nl/praat/).

## Uso del Script

1. Descarga o clona este repositorio

2. Asegurate de tener un archivo Praat script llamado "Combine_to_stereo.praat" en la misma carpeta que el script de Python. Este script de Praat debe contener los comandos necesarios para combinar archivos WAV a estéreo.

3. Abri una terminal y navega al directorio donde guardaste el repositorio.

4. Ejecuta el script `combine_to_stereo.py`:

    ```bash
    python combine_to_stereo.py
    ```

5. Se te pedirá que ingreses la ruta del directorio principal que contiene carpetas individuales con archivos WAV. Ingresa la ruta y presiona Enter.

6. El script recorrerá cada carpeta, buscará archivos WAV y los combinará a estéreo utilizando Praat. Los archivos combinados se guardarán en cada carpeta con el nombre "combined_stereo.wav".
