# app/consultas.py
from fastapi import APIRouter, HTTPException
import sqlite3
import pandas as pd
from app.database import obtener_conexion

router = APIRouter(prefix="/metricas", tags=["Métricas SQL"])

@router.get("/trimestres")
def contrataciones_por_trimestre():
    try:
        conn = obtener_conexion()
        query = '''
            SELECT d.department, j.job,
                SUM(CASE WHEN strftime('%m', h.datetime) BETWEEN '01' AND '03' THEN 1 ELSE 0 END) AS Q1,
                SUM(CASE WHEN strftime('%m', h.datetime) BETWEEN '04' AND '06' THEN 1 ELSE 0 END) AS Q2,
                SUM(CASE WHEN strftime('%m', h.datetime) BETWEEN '07' AND '09' THEN 1 ELSE 0 END) AS Q3,
                SUM(CASE WHEN strftime('%m', h.datetime) BETWEEN '10' AND '12' THEN 1 ELSE 0 END) AS Q4
            FROM hired_employees h
            JOIN departments d ON h.department_id = d.id
            JOIN jobs j ON h.job_id = j.id
            WHERE strftime('%Y', h.datetime) = '2021'
            GROUP BY d.department, j.job
            ORDER BY d.department, j.job
        '''
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/sobresalientes")
def departamentos_sobresalientes():
    try:
        conn = obtener_conexion()
        query = '''
            SELECT d.id, d.department, COUNT(*) AS contrataciones
            FROM hired_employees h
            JOIN departments d ON h.department_id = d.id
            WHERE strftime('%Y', h.datetime) = '2021'
            GROUP BY d.id, d.department
            HAVING COUNT(*) > (
                SELECT AVG(contador) FROM (
                    SELECT COUNT(*) AS contador
                    FROM hired_employees
                    WHERE strftime('%Y', datetime) = '2021'
                    GROUP BY department_id
                )
            )
            ORDER BY contrataciones DESC
        '''
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
