import cv2
import numpy as np

def segmentar_imagen(file):
    contents = file.file.read()
    npimg = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_GRAYSCALE)

    # Segmentación simple (ejemplo)
    _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    return {
        "mensaje": "Segmentación realizada",
        "pixeles_blancos": int(np.sum(thresh == 255))
    }