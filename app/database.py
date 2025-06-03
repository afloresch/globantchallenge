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
        CREATE TABLE IF NOT EXISTS departamentos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cargos (
            id INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            id_departamento INTEGER,
            id_cargo INTEGER,
            fecha_contratacion TEXT,
            FOREIGN KEY(id_departamento) REFERENCES departamentos(id),
            FOREIGN KEY(id_cargo) REFERENCES cargos(id)
        )
    ''')

    conn.commit()
    conn.close()
