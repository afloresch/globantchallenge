# Globant Challenge - Solución Completa

Este repositorio contiene la solución completa al challenge técnico propuesto, estructurado en tres secciones principales: API, SQL, y Bonus Track (Cloud, Testing y Containers).

---

## Sección 1: API REST para migración de datos

### Objetivo
Crear una API REST que:
- Reciba datos históricos desde archivos CSV (`departments`, `jobs`, `hired_employees`)
- Inserte los datos en una base de datos SQL (SQLite para propósito local, fácilmente adaptable a SQL Server)
- Permita inserción masiva de hasta 1000 registros

### Estructura
- `app/main.py`: define y expone los endpoints
- `app/cargar.py`: lógica para cargar CSVs y registros
- `app/database.py`: conexión con base de datos SQLite

### Cómo correr localmente
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Acceder a Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Sección 2: SQL y métricas solicitadas

### Objetivo
Exponer métricas solicitadas por el cliente a través de endpoints adicionales:

1. **Contrataciones por trimestre en 2021** agrupadas por departamento y puesto de trabajo.
2. **Departamentos que contrataron sobre el promedio en 2021**.

### Archivos relevantes
- `app/consultas.py`: lógica SQL para ambas consultas
- `app/main.py`: agrega los endpoints `/metricas/trimestres` y `/metricas/sobresalientes`

---

## Sección 3: Bonus Track - Arquitectura, Testing y Contenedores

### Cloud
- **Azure App Service** elegido como servicio de despliegue por simplicidad e integración con GitHub
- Flujo automático de CI/CD desde GitHub a producción

### Testing automatizado
- Framework sugerido: `pytest` con `TestClient` de FastAPI
- Tests recomendados incluidos en README_bonus.md

### Docker
Archivo `Dockerfile` incluido, listo para contenerizar y ejecutar:
```dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Estructura del repositorio
```
├── app/
│   ├── cargar.py
│   ├── consultas.py
│   ├── database.py
│   └── main.py
├── docs/
│   └── [archivos CSV de ejemplo]
├── requirements.txt
├── README.md (este)
├── README_bonus.md
└── Dockerfile
```

---

## Autor
Andrés Flores Chong  
[GitHub: afloresch](https://github.com/afloresch)

---

Este repositorio representa una solución completa, escalable y profesional al desafío técnico, utilizando FastAPI, SQL, Docker y Azure como base tecnológica.
