import os
from moviepy.editor import VideoFileClip

def convert_video_format(input_folder, output_folder, input_format, output_format, delete_input_after_conversion=False):
    # Verificar si las carpetas existen, si no, crearlas
    if not os.path.exists(input_folder):
        print(f"La carpeta de entrada '{input_folder}' no existe.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"La carpeta de salida '{output_folder}' no existe. Se ha creado la carpeta.")

    # Obtener la lista de archivos con el formato de entrada especificado en la carpeta de entrada
    input_files = [file for file in os.listdir(input_folder) if file.lower().endswith(f".{input_format}")]

    if not input_files:
        print(f"No se encontraron archivos con formato '{input_format}' en la carpeta '{input_folder}'.")
        return

    for input_file in input_files:
        # Crear el nombre de archivo para el video de salida
        output_file = os.path.splitext(input_file)[0] + f".{output_format}"

        # Combinar las rutas completas de los archivos
        input_path = os.path.join(input_folder, input_file)
        output_path = os.path.join(output_folder, output_file)

        try:
            # Abrir el archivo de entrada y convertirlo al formato de salida
            video = VideoFileClip(input_path)
            video.write_videofile(output_path, codec=output_format)

            print(f"Se ha convertido {input_file} a {output_file}.")

            # Eliminar el archivo de entrada original si está habilitada la opción
            if delete_input_after_conversion:
                os.remove(input_path)
                print(f"Se ha eliminado {input_file}.")
        except Exception as e:
            print(f"Error al convertir {input_file}: {e}")

if __name__ == "__main__":
    # Rutas de las carpetas de entrada y salida
    input_folder_path = "ruta/carpeta/entrada"    # Reemplazar con la ruta correcta
    output_folder_path = "ruta/carpeta/salida"    # Reemplazar con la ruta correcta

    # Formato de entrada y formato de salida deseados
    input_format = "mp4"   # Reemplazar con el formato de entrada deseado (ejemplo: "mp4", "avi", etc.)
    output_format = "webm"  # Reemplazar con el formato de salida deseado (ejemplo: "webm", "mkv", etc.)

    # Bandera para determinar si se eliminarán automáticamente los archivos de entrada después de la conversión
    delete_input_option = True  # Cambiar a False si no se desea eliminar los archivos de entrada automáticamente

    convert_video_format(input_folder_path, output_folder_path, input_format, output_format, delete_input_after_conversion=delete_input_option)
