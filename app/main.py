from fastapi import FastAPI
from app.routes.segmentacion import router as segmentacion_router

app = FastAPI(title="Servicio de Segmentación")

app.include_router(segmentacion_router, prefix="/api")