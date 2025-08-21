import os
import shutil

directory = os.path.join(os.path.expanduser("~"), "Downloads")
# Esta linea evita tener que definir una ruta en el SO 

# Se define que extensiones van a ir en que carpetas
# Las carpetas ya deben existir

extensions = {
    ".jpg": "Imagenes",
    ".png": "Imagenes",
    ".jpeg": "Imagenes",
    ".gif": "Imagenes",
    ".docx": "Archivos",
    ".pdf": "Archivos",
    ".txt": "Archivos",
    ".xlsx": "Archivos",
    ".pptx": "Archivos",
    ".exe": "Eliminar",
    ".zip": "Eliminar",
}

# Ciclo para revisar cada archivo y su ruta
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        # Se normalizan los nombres de los archivos a minuscula para que tome todos los archivos
        extension = os.path.splitext(filename)[1].lower()

        if extension in extensions:
            # Se crean las subcarpetas usando las extensiones como claves
            folder_name = extensions[extension]
            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True) #Si la carpeta ya existe, se omite

            # Se mueven los archivos segun el tipo de extension
            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)

            print(f"Se movió {filename} a la carpeta {folder_name}📁")
        else: 
            # Mueve el archivo de extension desconocida a la carpeta "eliminar"
            folder_name = "Eliminar"
            destination_path = os.path.join(directory, folder_name)
            shutil.move(file_path, destination_path)

            print(f"Se movió {filename} a la carpeta {folder_name} 📁")
    else:
        print(f"Se Omitio {filename} porque es un directorio 👀")

print("Organizacion de archivos: Completada!✅")