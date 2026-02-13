from fastapi import APIRouter, UploadFile, File
import os
import json

from app.services.segmentador import segmentar_pipeline
from app.utils.poligonos import obtener_poligonos_desde_mascara

router = APIRouter()


@router.post("/segmentar")
async def segmentar(file: UploadFile = File(...)):
    # Leer la imagen subida
    contenido = await file.read()

    # Ejecutar la segmentación
    resultado = segmentar_pipeline(contenido)

    # Convertir máscaras a polígonos
    json_resultado = {
        "membranas": obtener_poligonos_desde_mascara(resultado["membranas"]),
        "nucleos": obtener_poligonos_desde_mascara(resultado["nucleos"]),
        "micronucleos": obtener_poligonos_desde_mascara(resultado["micronucleos"]),
    }

    # Crear nombre del archivo JSON usando el nombre de la imagen
    nombre_base = os.path.splitext(file.filename)[0]
    nombre_json = f"{nombre_base}.json"

    # Guardar el JSON
    os.makedirs("resultados", exist_ok=True)
    ruta_salida = os.path.join("resultados", nombre_json)

    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(json_resultado, f, separators=(",", ":"))

    return {
        "status": "ok",
        "archivo": nombre_json
    }
