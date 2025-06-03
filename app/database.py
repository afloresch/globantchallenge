# app/database.py
import sqlite3
from pathlib import Path

# Ruta de la base de datos local
RUTA_BD = Path(__file__).resolve().parent.parent / "seccion_1_api" / "migracion.db"

# Crear carpeta si no existe
RUTA_BD.parent.mkdir(parents=True, exist_ok=True)

# Crear la conexión y las tablas si no existen
def obtener_conexion():
    conn = sqlite3.connect(RUTA_BD)
    return conn

def inicializar_bd():
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            department TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY,
            job TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hired_employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            datetime TEXT NOT NULL,
            department_id INTEGER,
            job_id INTEGER,
            FOREIGN KEY(department_id) REFERENCES departments(id),
            FOREIGN KEY(job_id) REFERENCES jobs(id)
        )
    ''')

    conn.commit()
    conn.close()
