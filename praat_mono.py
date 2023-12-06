import os
import subprocess

def combine_to_stereo(input_folder):
    for root, dirs, files in os.walk(input_folder):
        if "WAV" in dirs:
            # Found a folder with "WAV", let's process it
            input_folder_path = os.path.join(root, "WAV")
            
            # Get a list of all WAV files in the "WAV" folder
            wav_files = [file for file in os.listdir(input_folder_path) if file.endswith(".wav")]

            # Praat command
            praat_command = ["/Applications/Praat.app/Contents/MacOS/Praat", "--run", "Combine_to_stereo.praat"]

            # Construir una lista de argumentos, cada uno encapsulado como cadena
            arguments = [f'"{input_folder_path}"'] + [f'"{file}"' for file in wav_files]

            # Extender la lista de comandos de Praat con los argumentos
            praat_command.extend(arguments)

            # Unir todos los argumentos en una cadena para mejorar la legibilidad en la consola
            praat_command_str = " ".join(praat_command)

            # Imprimir el comando para verificar
            print(f"Ejecutando el comando de Praat: {praat_command_str}")

            # Ejecutar el comando de Praat
            subprocess.run(praat_command)

if __name__ == "__main__":
    parent_directory_path = input("Enter the parent directory path containing folders with WAV files: ")
    combine_to_stereo(parent_directory_path)
