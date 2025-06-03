# seccion_2_sql/README.md

# Sección 2: Métricas SQL - API

Esta sección del challenge expone una API REST que permite consultar métricas específicas solicitadas por los stakeholders, utilizando datos previamente cargados en una base SQLite.

---

## Requisitos cumplidos

- Métrica 1: Cantidad de contrataciones por trimestre durante 2021, por departamento y cargo
- Métrica 2: Departamentos que contrataron más empleados que el promedio en 2021

---

## Stack utilizado

- **Python 3**
- **FastAPI**
- **SQLite (vía `sqlite3`)**
- **Pandas** para conversión de resultados SQL a JSON

---

## Estructura

```
seccion_2_sql/
├── app/
│   ├── main.py           # Punto de entrada
│   ├── database.py       # Conexión y creación de tablas
│   └── consultas.py      # Endpoints de métricas
├── data/
│   └── migracion.db      # (Generado al correr la API)
├── requirements.txt
└── README.md
```

---

## Cómo ejecutar

1. Clona el repositorio y entra a la carpeta:
```bash
git clone https://github.com/afloresch/globantchallenge.git
cd globantchallenge/seccion_2_sql
```

2. Instala los requerimientos:
```bash
pip install -r requirements.txt
```

3. Inicia el servidor:
```bash
uvicorn app.main:app --reload
```

4. Accede a la documentación Swagger:
```
http://127.0.0.1:8000/docs
```

---

## Endpoints disponibles

### `/metricas/trimestres`
Devuelve el número de contrataciones por departamento y cargo en 2021, dividido por trimestre.

#### Ejemplo de respuesta:
```json
[
  {
    "department": "Staff",
    "job": "Recruiter",
    "Q1": 3,
    "Q2": 0,
    "Q3": 7,
    "Q4": 11
  }
]
```

---

### `/metricas/sobresalientes`
Devuelve los departamentos que contrataron más empleados que el promedio en 2021.

#### Ejemplo de respuesta:
```json
[
  {
    "id": 7,
    "department": "Staff",
    "contrataciones": 45
  },
  {
    "id": 9,
    "department": "Supply Chain",
    "contrataciones": 12
  }
]
```

---

## Checklist de validación

- [x] Código modular en `app/`
- [x] Endpoints funcionales vía Swagger
- [x] Dependencias listas en `requirements.txt`
- [x] `.gitignore` para evitar subir archivos innecesarios
