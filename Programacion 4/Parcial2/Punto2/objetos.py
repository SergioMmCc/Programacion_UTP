import json, os
from clases import *

############################ Listas ######################################
simples = []
dobles = []
suites = []


##################### FUNCION PARA GUARDAR LOS DATOS #####################
def guardar():
    data = []
    for h in simples:
        base = {
            "tipo": "simple",
            "numero": h.getNumero(),
            "precio": h.getPrecio(),
            "estado": h.getEstado()
        }
        data.append(base)
    for h in dobles:
        base = {
            "tipo": "doble",
            "numero": h.getNumero(),
            "precio": h.getPrecio(),
            "estado": h.getEstado(),
            "desayuno": h.getDesayuno(),
            "spa": h.getSpa()
        }
        data.append(base)
    for h in suites:
        base = {
            "tipo": "suite",
            "numero": h.getNumero(),
            "precio": h.getPrecio(),
            "estado": h.getEstado(),
            "desayuno": h.getDesayuno(),
            "spa": h.getSpa(),
            "gym": h.getGym()
        }
        data.append(base)

    with open("habitaciones.json", "w") as f:
        json.dump(data, f, indent=4)

    return True


###################### FUNCION PARA CARGAR LOS DATOS #####################
def cargar():
    if not os.path.exists("habitaciones.json"):
        return
    with open("habitaciones.json", "r") as f:
        data = json.load(f)

    # Limpiar listas antes de cargar
    simples.clear()
    dobles.clear()
    suites.clear()

    for h in data:
        if h["tipo"] == "simple":
            simples.append(HabitacionSimple(h["numero"], h["precio"], h["estado"]))
        elif h["tipo"] == "doble":
            dobles.append(HabitacionDoble(h["numero"], h["precio"], h["estado"], h["desayuno"], h["spa"]))
        elif h["tipo"] == "suite":
            suites.append(Suite(h["numero"], h["precio"], h["estado"], h["desayuno"], h["spa"], h["gym"]))

    print("Datos cargados correctamente")