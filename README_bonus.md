# Bonus Track: Arquitectura, Testing y Contenedores

Esta sección describe las decisiones técnicas que tomaría para robustecer la solución propuesta, en caso de escalarla a un entorno productivo. No se implementa directamente debido a restricciones de tiempo y foco, pero se presenta la arquitectura y el stack recomendado.

---

## Hosting en la nube

### Solución propuesta: **Azure App Service**

- **Motivo:** Simplicidad, integración directa con GitHub, escalabilidad y coherencia con mi experiencia previa en Azure.
- **Flujo esperado:**
  1. Push al branch de GitHub
  2. App Service detecta el cambio y redeploya automáticamente
  3. El `startup command` ejecutaría:
     ```bash
     gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
     ```

- **Alternativa avanzada:** Azure Container Apps con despliegue desde imagen Docker.

---

## Testing automatizado

### Stack propuesto: `pytest` + `fastapi.testclient`

- Se pueden validar los endpoints REST simulando peticiones HTTP:

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_metricas_trimestres():
    response = client.get("/metricas/trimestres")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_metricas_sobresalientes():
    response = client.get("/metricas/sobresalientes")
    assert response.status_code == 200
    assert all("department" in r for r in response.json())
```

- Se pueden agregar pruebas por error, vacío de datos o performance si se desea.

---

## Contenerización con Docker

### Dockerfile propuesto:

```dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

- Esto permite empaquetar todo el backend para ser desplegado en Azure, AWS o localmente.
- Compatible con servicios como Azure Container Registry + Container Apps.

---

## Conclusión

La arquitectura está pensada para escalar, mantenerse de forma sencilla, y adaptarse a distintos entornos (desarrollo, staging, producción) sin necesidad de grandes cambios.

Se prioriza FastAPI por su rendimiento y documentación automática (Swagger), Azure por mi experiencia previa y las pruebas automatizadas como base para calidad continua.
