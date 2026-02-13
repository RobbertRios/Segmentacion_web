from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
import io
import numpy as np

from app.services.segmentador import segmentar_pipeline

router = APIRouter()


@router.post("/segmentar")
async def segmentar(file: UploadFile = File(...)):
    contenido = await file.read()

    resultado = segmentar_pipeline(contenido)

    buffer = io.BytesIO()
    np.savez_compressed(
        buffer,
        membranas=resultado["membranas"],
        nucleos=resultado["nucleos"],
        micronucleos=resultado["micronucleos"],
    )

    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="application/octet-stream",
        headers={"Content-Disposition": "attachment; filename=resultado.npz"}
    )
