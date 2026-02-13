import cv2
import json
import numpy as np


def cargar_poligonos_json(ruta_json):
    """
    Carga el JSON con los polígonos
    """
    with open(ruta_json, "r", encoding="utf-8") as f:
        return json.load(f)


def dibujar_poligonos(imagen, lista_poligonos, color):
    """
    Dibuja una lista de polígonos sobre la imagen
    """
    for item in lista_poligonos:
        # Convertir string -> lista de puntos
        puntos = json.loads(item["poligono"])

        contorno = np.array(puntos, dtype=np.int32)
        contorno = contorno.reshape((-1, 1, 2))

        cv2.drawContours(
            imagen,
            [contorno],
            contourIdx=-1,
            color=color,
            thickness=2
        )


# ---------- CREAR FONDO NEGRO ----------
# Tamaño debe ser mayor o igual a las coordenadas máximas
alto = 2000
ancho = 2000

imagen = np.zeros((alto, ancho, 3), dtype=np.uint8)


# ---------- CARGAR JSON ----------
datos = cargar_poligonos_json("resultados/01.json")


# ---------- DIBUJAR CAPAS ----------
dibujar_poligonos(imagen, datos["membranas"], (0, 0, 255))       # rojo
dibujar_poligonos(imagen, datos["nucleos"], (0, 255, 0))         # verde
dibujar_poligonos(imagen, datos["micronucleos"], (255, 0, 0))   # azul


# ---------- MOSTRAR RESULTADO ----------
cv2.imshow("Capas sobre fondo negro", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ---------- GUARDAR RESULTADO ----------
cv2.imwrite("01.png", imagen)

print("Imagen generada: 11.png")