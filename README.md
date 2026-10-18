# StyleMatch Product Analytics 👗📊

## Context

StyleMatch is a fictional AI-powered fashion application that helps users
create outfits using clothes from their own wardrobe.

## Business Problem

The product team wants to understand how users interact with the application,
identify where users abandon the main product journey, and discover
opportunities to improve activation, conversion, and retention.

## Main Product Journey

Visit → Sign Up → Upload Garment → Generate Outfit → Save Outfit → Premium

## Objectives

- Analyze user behavior.
- Define product KPIs.
- Build a conversion funnel.
- Analyze activation and retention.
- Perform cohort analysis.
- Segment users by behavior and acquisition channel.
- Design and analyze an A/B experiment.
- Build an interactive Power BI dashboard.
- Generate actionable product recommendations.

## Tools

- Python
- SQL
- Power BI
- Statistics


## StyleMatch API - Backend

API REST desarrollada con Python y FastAPI para gestionar prendas de vestir, generar recomendaciones de outfits y guardar combinaciones favoritas.

### Tecnologías utilizadas

- Python
- FastAPI
- SQLite
- SQL
- Swagger UI

### Funcionalidades

- Registrar prendas de vestir.
- Consultar prendas almacenadas en SQLite.
- Generar un outfit con prendas de diferentes categorías.
- Guardar outfits favoritos en una base de datos.
- Consultar los outfits favoritos.
- Mantener los datos guardados después de reiniciar el servidor.

### Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | / | Verificar funcionamiento de la API |
| GET | /prendas | Consultar prendas |
| POST | /prendas | Registrar una prenda |
| GET | /recomendar | Generar un outfit |
| POST | /favoritos | Guardar un outfit favorito |
| GET | /favoritos | Consultar favoritos |

### Cómo ejecutar el backend

Instalar las dependencias:

```bash
pip install "fastapi[standard]"
```

Iniciar el servidor desde la carpeta principal del proyecto:

```bash
python -m uvicorn backend.main:app --reload
```

Abrir la documentación interactiva:

http://127.0.0.1:8000/docs

### Nota

Las recomendaciones se generan utilizando las prendas registradas en SQLite. La versión actual selecciona una prenda superior, una inferior y un calzado disponibles.
