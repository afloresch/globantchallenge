from fastapi import FastAPI
from app.consultas import router as consultas_router
from app.database import inicializar_bd

inicializar_bd()

app = FastAPI(
    title="API de Métricas SQL",
    description="Endpoints para consultar contrataciones 2021",
    version="2.0"
)

app.include_router(consultas_router)

@app.get("/")
def inicio():
    return {"mensaje": "API de métricas activada"}

@app.get("/salud")
def salud():
    return {"estado": "ok"}
