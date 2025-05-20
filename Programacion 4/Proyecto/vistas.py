from datetime import datetime
from persistencia import *

######################## FUNCIONES PARA MOSTRAR INSTANCIAS #################################
# Funcion para mostrar un vuelo
def mostrar_vuelo(vuelo):
    id_vuelo = vuelo.getId()

    avion = obtener_avion(vuelo.getIdAvion())
    if not avion:
        print(f"Error: No se encontró el avión para el vuelo {id_vuelo}")
        return

    # Contar reservas activas
    ocupadas_economicas = contar_reservas_activas(id_vuelo, "economico")
    ocupadas_ejecutivas = contar_reservas_activas(id_vuelo, "ejecutivo")

    disponibles_economico = avion.getCapacidadEconomica() - ocupadas_economicas
    disponibles_ejecutivo = avion.getCapacidadEjecutiva() - ocupadas_ejecutivas

    print(f"ID del vuelo: {id_vuelo}")
    print(f"  Origen: {vuelo.getOrigen()}")
    print(f"  Destino: {vuelo.getDestino()}")
    print(f"  Salida: {vuelo.getFechaHoraSalida().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Llegada: {vuelo.getFechaHoraLlegada().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Precio Económica: ${vuelo.getPrecioEconomica():.2f}")
    print(f"  Precio Ejecutiva: ${vuelo.getPrecioEjecutiva():.2f}")
    print(f"  Disponibles - Económica: {disponibles_economico} / {avion.getCapacidadEconomica()}")
    print(f"  Disponibles - Ejecutiva: {disponibles_ejecutivo} / {avion.getCapacidadEjecutiva()}")
    print("-" * 40)


# Funcion para mostrar una reserva
def mostrar_reserva(reserva):
    pasajero = obtener_pasajero(reserva.getIdPasajero())
    vuelo = obtener_vuelo(reserva.getIdVuelo())

    if not pasajero:
        print(f"Pasajero con ID {reserva.getIdPasajero()} no encontrado.")
        return
    if not vuelo:
        print(f"Vuelo con ID {reserva.getIdVuelo()} no encontrado.")
        return

    print(f"ID Reserva: {reserva.getId()}")
    print(f"  Pasajero: {pasajero.getNombre()} (ID: {pasajero.getId()})")
    print(f"  Tipo de asiento: {reserva.getTipoAsiento().capitalize()}")
    print(f"  Estado: {reserva.getEstado().capitalize()}")
    print(f"  Vuelo ID: {vuelo.getId()}")
    print(f"    Origen: {vuelo.getOrigen()}")
    print(f"    Destino: {vuelo.getDestino()}")
    print(f"    Salida: {vuelo.getFechaHoraSalida().strftime('%Y-%m-%d %H:%M')}")
    print(f"    Llegada: {vuelo.getFechaHoraLlegada().strftime('%Y-%m-%d %H:%M')}")
    print("-" * 40)


# Función para mostrar un pasajero
def mostrar_pasajero(pasajero):
    print(f"Pasajero ID: {pasajero.getId()}")
    print(f"  Nombre: {pasajero.getNombre().title()}")
    print(f"  Correo: {pasajero.getCorreo()}")
    print("-" * 40)


# Función para mostrar un avión
def mostrar_avion(avion):
    print(f"Avión ID: {avion.getId()}")
    print(f"  Modelo: {avion.getModelo()}")
    print(f"  Capacidad Económica: {avion.getCapacidadEconomica()}")
    print(f"  Capacidad Ejecutiva: {avion.getCapacidadEjecutiva()}")
    print("-" * 40)


######################### FUNCIONES PARA SOLICITAR DATOS AL USUARIO ##############################
# Función para pedir los datos de un pasajero
def datos_pasajero_desde_input():
    try:
        id_pasajero = int(input("ID del pasajero: "))
        nombre = input("Nombre del pasajero: ").strip()
        correo = input("Correo del pasajero: ").strip()
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return None
    return id_pasajero, nombre, correo

# Función para pedir los datos de un avión
def datos_avion_desde_input():
    try:
        id_avion = int(input("ID del avión: "))
        modelo = input("Modelo del avión: ").strip()
        capacidad_economica = int(input("Capacidad económica: "))
        capacidad_ejecutiva = int(input("Capacidad ejecutiva: "))
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar números enteros donde corresponde.")
        return None
    return id_avion, modelo, capacidad_economica, capacidad_ejecutiva

# Función para pedir los datos de un vuelo
def datos_vuelo_desde_input():
    try:
        id_vuelo = int(input("ID del vuelo: "))
        id_avion = int(input("ID del avión: "))
        origen = input("Ciudad de origen: ").strip()
        destino = input("Ciudad de destino: ").strip()
        salida_str = input("Fecha y hora de salida (YYYY-MM-DD HH:MM): ")
        llegada_str = input("Fecha y hora de llegada (YYYY-MM-DD HH:MM): ")
        fecha_hora_salida = datetime.strptime(salida_str, "%Y-%m-%d %H:%M")
        fecha_hora_llegada = datetime.strptime(llegada_str, "%Y-%m-%d %H:%M")
        precio_economica = float(input("Precio clase económica: "))
        precio_ejecutiva = float(input("Precio clase ejecutiva: "))
    except ValueError:
        print("Error de formato. Verifica que los datos numéricos y fechas sean correctos.")
        return None
    return (id_vuelo, id_avion, origen, destino,
            fecha_hora_salida, fecha_hora_llegada,
            precio_economica, precio_ejecutiva)

# Función para pedir los datos para una reserva
def datos_reserva_desde_input():
    try:
        id_pasajero = int(input("ID del pasajero: "))
        id_vuelo = int(input("ID del vuelo: "))
        tipo_asiento = input("Tipo de asiento (economico/ejecutivo): ").strip().lower()
    except ValueError:
        print("Error de entrada. Asegúrate de que los IDs sean números enteros.")
        return None
    return id_pasajero, id_vuelo, tipo_asiento

# Función para pedir el ID de la reserva a cambiar a ejecutiva
def id_reserva_para_cambio_desde_input():
    try:
        id_reserva = int(input("Ingrese el ID de la reserva: "))
    except ValueError:
        print("Error: El ID de la reserva debe ser un número entero.")
        return None
    return id_reserva



######################### FUNCIONES REUTILIZABLES PARA PEDIR DATOS AL USUARIO ##############################

def pedir_id_pasajero():
    try:
        return int(input("Ingrese el ID del pasajero: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return None

def pedir_id_avion():
    try:
        return int(input("Ingrese el ID del avión: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return None

def pedir_id_vuelo():
    try:
        return int(input("Ingrese el ID del vuelo: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return None

def pedir_id_reserva():
    try:
        return int(input("Ingrese el ID de la reserva: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return None

def pedir_origen_y_destino():
    origen = input("Ingrese la ciudad de origen: ").strip()
    destino = input("Ingrese la ciudad de destino: ").strip()
    return origen, destino
