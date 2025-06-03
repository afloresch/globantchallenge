# section1_api/README.md

# Sección 1: API de Migración de Datos

Esta API permite cargar datos históricos desde archivos CSV o desde solicitudes por lote (batch) hacia una base de datos SQL (en este caso, SQLite como motor local para facilitar la ejecución).

---

## Objetivos

- Recibir datos históricos desde archivos CSV
- Subir estos archivos a una base de datos
- Permitir la inserción de transacciones por lote (1 a 1000 filas)

---

## Stack utilizado

- **Lenguaje:** Python 3
- **Framework:** FastAPI
- **Base de datos:** SQLite (simula SQL Server en local)
- **Librerías:** pandas, FastAPI, uvicorn

---

## Estructura

```
section1_api/
├── app/
│   ├── main.py              # Punto de entrada de la API
│   ├── cargar.py            # Endpoints de carga
│   └── database.py          # Creación y conexión a la base
├── data/
│   ├── departments.csv
│   ├── jobs.csv
│   └── hired_employees.csv
├── requirements.txt
└── README.md
```

---

## Cómo ejecutar

1. Clona el repositorio y entra a la carpeta:
```bash
git clone https://github.com/tu_usuario/tu_repo.git
cd section1_api
```

2. Instala los requerimientos:
```bash
pip install -r requirements.txt
```

3. Ejecuta el servidor:
```bash
uvicorn app.main:app --reload
```

4. Abre en el navegador:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Endpoints principales

### `/cargar/csv/{nombre_tabla}`
Carga datos desde un CSV localizado en `/data/`.  
Nombres válidos:
- `departamentos`
- `cargos`
- `empleados`

### `/cargar/lote/{nombre_tabla}`
Inserta un lote de registros en formato JSON (hasta 1000 filas).

---

## Ejemplo de uso (con `curl`)

```bash
curl -X POST http://localhost:8000/cargar/lote/departamentos \
  -H 'Content-Type: application/json' \
  -d '[{"id": 99, "nombre": "Innovación"}]'
```

---

## Notas

- En un entorno real, se reemplazaría SQLite por SQL Server usando `pyodbc`.
- Este diseño modular permite hacer el cambio fácilmente con pocas modificaciones en `database.py`.

---


