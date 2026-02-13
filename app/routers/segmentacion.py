from fastapi import APIRouter, UploadFile, File

from app.services.segmentador import segmentar_pipeline
from app.utils.poligonos import obtener_poligonos_desde_mascara

router = APIRouter()


@router.post("/segmentar")
async def segmentar(file: UploadFile = File(...)):
    """
    Recibe imagen, segmenta y devuelve JSON con polígonos.
    No guarda archivos, no imprime nada.
    """
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

    return json_resultado