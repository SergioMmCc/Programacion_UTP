from modelos import Avion, Pasajero, Vuelo, Reserva
from datetime import datetime
import json, os

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
        "idAvion": v.getIdAvion(),
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
        "id": r.getId(),  # Nuevo campo: ID único de la reserva
        "idPasajero": r.getIdPasajero(),
        "idVuelo": r.getIdVuelo(),
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
                vuelo = Vuelo(v["id"], v["idAvion"], v["origen"], v["destino"], 
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
                reserva = Reserva(r["id"], r["idPasajero"], r["idVuelo"], r["tipoAsiento"])  # ← aquí se pasa el id
                reserva.setEstado(r["estado"])  # Actualizamos el estado de la reserva
                reservas.append(reserva)


    print("Datos cargados exitosamente.")


############################## FUNCIONES PARA VALIDACIONES ##################################
# Función para obtener un pasajero por ID
def obtener_pasajero(id_pasajero):
    return next((p for p in pasajeros if p.getId() == id_pasajero), None)

# Función para obtener un avión por ID
def obtener_avion(id_avion):
    return next((a for a in aviones if a.getId() == id_avion), None)

# Función para obtener un vuelo por ID
def obtener_vuelo(id_vuelo):
    return next((v for v in vuelos if v.getId() == id_vuelo), None)

# Obtener reserva por su id
def obtener_reserva(id_reserva):
    return next((r for r in reservas if r.getId() == id_reserva), None)

# Función para obtener una reserva activa por pasajero y vuelo
def obtener_reserva_activa(id_pasajero, id_vuelo):
    return next(
        (r for r in reservas if r.getIdPasajero() == id_pasajero and r.getIdVuelo() == id_vuelo and r.getEstado() == "activa"),
        None
    )

# Funcion para obtener el avión correspondiente a un vuelo
def obtener_avion_por_vuelo(id_vuelo):
    vuelo = obtener_vuelo(id_vuelo)
    if vuelo is None:
        return None
    return obtener_avion(vuelo.getIdAvion())

# Funcion para contar la cantidad de reservas activas de cierto vuelo
def contar_reservas_activas(id_vuelo, tipo_asiento):
    return sum(
        1 for r in reservas
        if r.getIdVuelo() == id_vuelo and r.getTipoAsiento() == tipo_asiento and r.getEstado() == "activa"
    )