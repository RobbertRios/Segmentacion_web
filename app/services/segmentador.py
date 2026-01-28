import cv2
import numpy as np

def procesar_imagen(file):
    try:
        contenido = file.file.read()

        return {
            "nombre_archivo": file.filename,
            "tamano_bytes": len(contenido),
            "mensaje": "Imagen recibida correctamente"
        }

    except Exception as e:
        return {
            "error": "Fallo al procesar la imagen",
            "detalle": str(e)
        }