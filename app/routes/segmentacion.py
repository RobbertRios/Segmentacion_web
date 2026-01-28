from fastapi import APIRouter, UploadFile, File
from app.services.segmentador import segmentar_imagen

router = APIRouter()

@router.post("/segmentar")
async def segmentar(file: UploadFile = File(...)):
    resultado = segmentar_imagen(file)
    return resultado