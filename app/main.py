# app/main.py
from fastapi import FastAPI
from app.cargar import router as cargar_router
from app.database import inicializar_bd

app = FastAPI(
    title="API de Migración de Datos",
    description="Sube datos desde CSV o en lote a una base de datos SQL",
    version="1.0"
)

# Crear tablas si no existen
inicializar_bd()

# Incluir rutas
app.include_router(cargar_router)

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la API de Migración"}

@app.get("/salud")
def check_salud():
    return {"estado": "ok"}
