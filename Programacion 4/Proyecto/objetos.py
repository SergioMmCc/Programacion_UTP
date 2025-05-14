import json, os
from clases import *

############################ Listas ######################################
aviones = []
vuelos = []
pasajeros = []
reservas = []

##################### FUNCION PARA GUARDAR LOS DATOS #####################
def guardar():
    # Guardamos los datos de los aviones
    data_aviones = [{
        "id": a.getId(),
        "modelo": a.getModelo(),
        "capacidadEconomica": a.getCapacidadEconomica(),
        "capacidadEjecutiva": a.getCapacidadEjecutiva()
    } for a in aviones]

    # Guardamos los datos de los vuelos
    data_vuelos = [{
        "id": v.getId(),
        "avionId": v.getAvion().getId(),  # Guardamos el id del avión, no el objeto completo
        "origen": v.getOrigen(),
        "destino": v.getDestino(),
        "fechaHoraSalida": v.getFechaHoraSalida().strftime("%Y-%m-%d %H:%M:%S"),
        "fechaHoraLlegada": v.getFechaHoraLlegada().strftime("%Y-%m-%d %H:%M:%S"),
        "precioEconomica": v.getPrecioEconomica(),
        "precioEjecutiva": v.getPrecioEjecutiva()
    } for v in vuelos]

    # Guardamos los datos de los pasajeros
    data_pasajeros = [{
        "id": p.getId(),
        "nombre": p.getNombre(),
        "correo": p.getCorreo()
    } for p in pasajeros]

    # Guardamos los datos de las reservas
    data_reservas = [{
        "pasajeroId": r.getPasajero().getId(),  # Guardamos el id del pasajero, no el objeto completo
        "vueloId": r.getVuelo().getId(),        # Guardamos el id del vuelo, no el objeto completo
        "tipoAsiento": r.getTipoAsiento(),
        "estado": r.getEstado()
    } for r in reservas]

    # Guardamos los datos en archivos JSON
    with open("archivos/aviones.json", "w", encoding="utf-8") as f:
        json.dump(data_aviones, f, indent=4, ensure_ascii=False)
    with open("archivos/vuelos.json", "w", encoding="utf-8") as f:
        json.dump(data_vuelos, f, indent=4, ensure_ascii=False)
    with open("archivos/pasajeros.json", "w", encoding="utf-8") as f:
        json.dump(data_pasajeros, f, indent=4, ensure_ascii=False)
    with open("archivos/reservas.json", "w", encoding="utf-8") as f:
        json.dump(data_reservas, f, indent=4, ensure_ascii=False)

    print("Datos guardados exitosamente.")


###################### FUNCION PARA CARGAR LOS DATOS #####################
def cargar():
    # Limpiar las listas antes de cargar nuevos datos
    aviones.clear()
    vuelos.clear()
    pasajeros.clear()
    reservas.clear()

    # Cargar los aviones desde el archivo
    if os.path.exists("archivos/aviones.json"):
        with open("archivos/aviones.json", "r", encoding="utf-8") as f:
            for a in json.load(f):
                avion = Avion(a["id"], a["modelo"], a["capacidadEconomica"], a["capacidadEjecutiva"])
                aviones.append(avion)

    # Cargar los vuelos desde el archivo
    if os.path.exists("archivos/vuelos.json"):
        with open("archivos/vuelos.json", "r", encoding="utf-8") as f:
            for v in json.load(f):
                avion = next((a for a in aviones if a.getId() == v["avionId"]), None)
                vuelo = Vuelo(v["id"], avion, v["origen"], v["destino"], 
                              datetime.strptime(v["fechaHoraSalida"], "%Y-%m-%d %H:%M:%S"),
                              datetime.strptime(v["fechaHoraLlegada"], "%Y-%m-%d %H:%M:%S"),
                              v["precioEconomica"], v["precioEjecutiva"])
                vuelos.append(vuelo)

    # Cargar las pasajeros desde el archivo
    if os.path.exists("archivos/pasajeros.json"):
        with open("archivos/pasajeros.json", "r", encoding="utf-8") as f:
            for p in json.load(f):
                pasajero = Pasajero(p["id"], p["nombre"], p["correo"])
                pasajeros.append(pasajero)

    # Cargar las reservas desde el archivo
    if os.path.exists("archivos/reservas.json"):
        with open("archivos/reservas.json", "r", encoding="utf-8") as f:
            for r in json.load(f):
                pasajero = next((p for p in pasajeros if p.getId() == r["pasajeroId"]), None)
                vuelo = next((v for v in vuelos if v.getId() == r["vueloId"]), None)
                reserva = Reserva(pasajero, vuelo, r["tipoAsiento"])
                reserva.setEstado(r["estado"])  # Actualizamos el estado de la reserva
                reservas.append(reserva)

    print("Datos cargados exitosamente.")
