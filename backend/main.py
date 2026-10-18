
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI(title="StyleMatch API")

def crear_base_datos():
    conexion = sqlite3.connect("backend/stylematch.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            color TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS favoritos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            outfit TEXT NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()


crear_base_datos()



@app.get("/")
def inicio():
    return {
        "mensaje": "¡Bienvenido a StyleMatch!",
        "estado": "Backend funcionando"
    }




@app.get("/prendas")
def obtener_prendas():
    conexion = sqlite3.connect("backend/stylematch.db")
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM prendas")
    prendas_guardadas = [
        dict(fila) for fila in cursor.fetchall()
    ]

    conexion.close()
    return prendas_guardadas




class PrendaNueva(BaseModel):
    nombre: str
    categoria: str
    color: str



@app.post("/prendas")
def agregar_prenda(prenda: PrendaNueva):
    conexion = sqlite3.connect("backend/stylematch.db")
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO prendas (nombre, categoria, color) VALUES (?, ?, ?)",
        (prenda.nombre, prenda.categoria, prenda.color)
    )

    conexion.commit()
    nuevo_id = cursor.lastrowid
    conexion.close()

    return {
        "mensaje": "Prenda guardada en la base de datos",
        "prenda": {
            "id": nuevo_id,
            "nombre": prenda.nombre,
            "categoria": prenda.categoria,
            "color": prenda.color
        }
    }


@app.get("/recomendar")
def recomendar_outfit():
    
    prendas = obtener_prendas()

    superiores = [p for p in prendas if p["categoria"] == "superior"]
    inferiores = [p for p in prendas if p["categoria"] == "inferior"]
    calzados = [p for p in prendas if p["categoria"] == "calzado"]

    if not superiores or not inferiores or not calzados:
        return {"mensaje": "No hay suficientes prendas para crear un outfit"}

    return {
        "mensaje": "¡Tu outfit está listo!",
        "outfit": {
            "superior": superiores[0],
            "inferior": inferiores[0],
            "calzado": calzados[0]
        }
    }

outfits_favoritos = []
import json



@app.post("/favoritos")
def guardar_outfit_favorito():
    resultado = recomendar_outfit()

    if "outfit" not in resultado:
        return {"mensaje": "No hay un outfit disponible para guardar"}

    outfit = resultado["outfit"]

    conexion = sqlite3.connect("backend/stylematch.db")
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO favoritos (outfit) VALUES (?)",
        (json.dumps(outfit),)
    )

    conexion.commit()
    nuevo_id = cursor.lastrowid
    conexion.close()

    return {
        "mensaje": "¡Outfit guardado en la base de datos!",
        "id": nuevo_id,
        "outfit": outfit
    }



@app.get("/favoritos")
def obtener_favoritos():
    conexion = sqlite3.connect("backend/stylematch.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT id, outfit FROM favoritos")
    filas = cursor.fetchall()
    conexion.close()

    favoritos = [
        {
            "id": fila[0],
            "outfit": json.loads(fila[1])
        }
        for fila in filas
    ]

    return favoritos

