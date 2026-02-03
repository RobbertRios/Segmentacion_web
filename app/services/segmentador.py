import numpy as np
import os
import uuid

def procesar_imagen(file):
    """
    Simula una segmentación:
    - genera una máscara .npy
    - genera métricas aleatorias
    """

    # Crear carpeta output
    os.makedirs("output", exist_ok=True)

    # Nombre único
    nombre_base = str(uuid.uuid4())
    ruta_npy = f"output/{nombre_base}.npy"

    # 🔹 Simular máscara (o aquí puedes cargar una real)
    mascara = np.random.randint(0, 2, (256, 256))
    np.save(ruta_npy, mascara)

    # 🔹 Métricas simuladas
    area = int(mascara.sum())
    volumen = float(area * 0.15)
    nucleos = int(area * 0.02)
    micronucleos = int(nucleos * 0.1)

    return {
        "archivo_npy": ruta_npy,
        "metricas": {
            "area": area,
            "volumen": volumen,
            "nucleos": nucleos,
            "micronucleos": micronucleos
        },
        "estado": "listo"
    }