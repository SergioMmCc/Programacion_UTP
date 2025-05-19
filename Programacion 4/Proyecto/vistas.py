from modelos import *
from controladores import obtener_avion, obtener_pasajero, obtener_vuelo, contar_reservas_activas

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
