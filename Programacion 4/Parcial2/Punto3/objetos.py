import json
from clases import *

# Listas de productos por tipo
electronicos = []
ropa = []
alimentos = []

# Guardar productos en JSON
def guardar_productos():
    todos = [p.to_dict() for p in electronicos + ropa + alimentos]
    with open("productos.json", "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=4)

# Cargar productos desde JSON
def cargar_productos():
    try:
        with open("productos.json", "r", encoding="utf-8") as f:
            datos = json.load(f)
            for d in datos:
                if d["tipo"] == "Electronico":
                    electronicos.append(Electronico(d["nombre"], d["precio"], d["cantidad"], d["garantia"]))
                elif d["tipo"] == "Ropa":
                    ropa.append(Ropa(d["nombre"], d["precio"], d["cantidad"], d["talla"]))
                elif d["tipo"] == "Alimento":
                    alimentos.append(Alimento(d["nombre"], d["precio"], d["cantidad"], d["caducidad"]))
    except FileNotFoundError:
        print("Archivo de productos no encontrado. Se iniciará con listas vacías.")