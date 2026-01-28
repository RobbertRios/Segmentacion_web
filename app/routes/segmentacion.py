from fastapi import APIRouter, UploadFile, File
from app.services.segmentador import procesar_imagen

router = APIRouter()

@router.post("/segmentar")
async def segmentar(file: UploadFile = File(...)):
    return procesar_imagen(file)