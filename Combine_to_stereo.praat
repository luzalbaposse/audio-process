# Combine_to_stereo.praat

# Obtener argumentos de la línea de comandos
input_folder = Get command line arguments
numberOfArgs = numberOfItems(input_folder)

# Crear una lista para almacenar los objetos de sonido
Create Strings as list: "fileList"

# Leer cada archivo WAV en un objeto de sonido y agregarlo a la lista
for i from 1 to numberOfArgs
    fileName = Get item i of input_folder
    soundObj = Read from file: fileName
    Append: fileList, fileName
endfor

# Combinar a estéreo
combinedSound = Combine: "Stereo", fileList

# Obtener la ruta del primer archivo WAV
outputPath = Get item 1 of input_folder
outputPath = stringfilepath$ + "combined_stereo.wav"

# Guardar el resultado como archivo WAV
Write to WAV file: outputPath, combinedSound

# Salir de Praat
exit
