# app/cargar.py
from fastapi import APIRouter, HTTPException
import pandas as pd
import sqlite3
from app.database import obtener_conexion
from typing import List
import os

router = APIRouter(prefix="/cargar", tags=["Carga de datos"])

TABLAS_PERMITIDAS = {
    "departments": {
        "archivo": "departments.csv",
        "columnas": ["id", "department"]
    },
    "jobs": {
        "archivo": "jobs.csv",
        "columnas": ["id", "job"]
    },
    "hired_employees": {
        "archivo": "hired_employees.csv",
        "columnas": ["id", "name", "datetime", "department_id", "job_id"]
    }
}

DATA_FOLDER = os.path.join(os.path.dirname(__file__), "..", "data")

@router.post("/csv/{nombre_tabla}")
def cargar_csv(nombre_tabla: str):
    if nombre_tabla not in TABLAS_PERMITIDAS:
        raise HTTPException(status_code=400, detail="Tabla no permitida")

    info = TABLAS_PERMITIDAS[nombre_tabla]
    ruta_archivo = os.path.join(DATA_FOLDER, info["archivo"])

    try:
        df = pd.read_csv(ruta_archivo, header=None)
        df.columns = info["columnas"]

        conn = obtener_conexion()
        df.to_sql(nombre_tabla, conn, if_exists='append', index=False)
        conn.close()

        return {"mensaje": f"Datos insertados correctamente en {nombre_tabla}", "filas": len(df)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/lote/{nombre_tabla}")
def cargar_lote(nombre_tabla: str, datos: List[dict]):
    if nombre_tabla not in TABLAS_PERMITIDAS:
        raise HTTPException(status_code=400, detail="Tabla no permitida")

    if len(datos) > 1000:
        raise HTTPException(status_code=400, detail="Máximo 1000 filas por lote")

    columnas = TABLAS_PERMITIDAS[nombre_tabla]["columnas"]
    try:
        df = pd.DataFrame(datos)
        df = df[columnas]  # Reordenar columnas según tabla

        conn = obtener_conexion()
        df.to_sql(nombre_tabla, conn, if_exists='append', index=False)
        conn.close()

        return {"mensaje": f"Lote insertado correctamente en {nombre_tabla}", "filas": len(df)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
