from objetos import *

############################## FUNCIONES PARA MANIPULAR RESERVAS ###################################
# Funcion para hacer una reserva
def reservar(id_pasajero, id_vuelo, tipo_asiento):
    # Buscar pasajero
    pasajero = next((p for p in pasajeros if p.getId() == id_pasajero), None)
    if not pasajero:
        print("Pasajero no encontrado.")
        return

    # Buscar vuelo
    vuelo = next((v for v in vuelos if v.getId() == id_vuelo), None)
    if not vuelo:
        print("Vuelo no encontrado.")
        return

    # Verificar si ya tiene una reserva activa en ese vuelo
    for r in reservas:
        if r.getIdPasajero() == id_pasajero and r.getIdVuelo() == id_vuelo and r.getEstado() == "activa":
            print("El pasajero ya tiene una reserva activa en este vuelo.")
            return

    # Contar cuántas reservas activas hay de cada tipo en el vuelo
    reservas_vuelo = [r for r in reservas if r.getIdVuelo() == id_vuelo]
    economicas_ocupadas = sum(1 for r in reservas_vuelo if r.getTipoAsiento() == "economico" and r.getEstado() == "activa")
    ejecutivas_ocupadas = sum(1 for r in reservas_vuelo if r.getTipoAsiento() == "ejecutivo" and r.getEstado() == "activa")

    avion = next((a for a in aviones if(a.getId() == vuelo.getIdAvion())), None)
    if not avion:
        raise ValueError(f"El avión asignado a ese vuelo no existe")

    # Verificar disponibilidad
    if tipo_asiento == "economico":
        if economicas_ocupadas >= avion.getCapacidadEconomica():
            print("No hay asientos económicos disponibles.")
            return
        nueva_reserva = ReservaEconomica(id_pasajero, id_vuelo)
    elif tipo_asiento == "ejecutivo":
        if ejecutivas_ocupadas >= avion.getCapacidadEjecutiva():
            print("No hay asientos ejecutivos disponibles.")
            return
        nueva_reserva = ReservaEjecutiva(id_pasajero, id_vuelo)
    else:
        print("Tipo de asiento inválido.")
        return

    # Registrar reserva
    reservas.append(nueva_reserva)
    guardar()
    print("Reserva realizada con éxito.")


# Funcion para cambiar una reserva de economica a ejecutiva
def cambiar_a_ejecutiva(id_pasajero, id_vuelo):
    # Buscar la reserva correspondiente
    reserva = next((r for r in reservas if r.getIdPasajero() == id_pasajero and r.getIdVuelo() == id_vuelo), None)

    if not reserva:
        print("No se encontró una reserva con esos datos.")
        return

    if reserva.getTipoAsiento() != "economica":
        print("La reserva no es de clase económica, no se puede cambiar.")
        return

    if reserva.getEstado().lower() != "activa":
        print("La reserva no está activa, no se puede cambiar.")
        return

    vuelo = next((v for v in vuelos if v.getId() == id_vuelo), None)
    if not vuelo:
        raise ValueError(f"No existe ningún vuelo asociado a esa reserva")

    id_avion = vuelo.getIdAvion()
    avion = next((a for a in aviones if a.getId() == id_avion), None)
    if not avion:
        raise ValueError(f"No existe ningún avión asociado a ese vuelo")

    # Contar cuántas reservas ejecutivas ya hay para este vuelo
    reservas_ejecutivas = sum(
        1 for r in reservas if r.getIdVuelo() == id_vuelo and r.getTipoAsiento() == "ejecutiva" and r.getEstado().lower() == "activa"
    )

    if reservas_ejecutivas >= avion.getCapacidadEjecutiva():
        print("No hay asientos ejecutivos disponibles.")
        return

    # Cambiar la reserva
    reserva.setTipoAsiento("ejecutiva")

    print("Reserva actualizada a clase ejecutiva.")


#################################### FUNCIONES PARA CONSULTAR VUELOS #################################
# Funcion para mostrar un vuelo
def mostrar_vuelo(vuelo):
    id_vuelo = vuelo.getId()

    avion = next((a for a in aviones if a.getId() == vuelo.getIdAvion()), None)
    if not avion:
        raise ValueError (f"  [!] Error: No se encontró el avión para el vuelo {id_vuelo}")

    # Contar reservas activas
    reservas_vuelo = [r for r in reservas if r.getIdVuelo() == id_vuelo and r.getEstado().lower() == "activa"]
    economicas_ocupadas = sum(1 for r in reservas_vuelo if r.getTipoAsiento() == "economico")
    ejecutivas_ocupadas = sum(1 for r in reservas_vuelo if r.getTipoAsiento() == "ejecutivo")

    disponibles_economico = avion.getCapacidadEconomica() - economicas_ocupadas
    disponibles_ejecutivo = avion.getCapacidadEjecutiva() - ejecutivas_ocupadas

    print(f"ID: {id_vuelo}")
    print(f"  Origen: {vuelo.getOrigen()}")
    print(f"  Destino: {vuelo.getDestino()}")
    print(f"  Salida: {vuelo.getFechaHoraSalida().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Llegada: {vuelo.getFechaHoraLlegada().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Precio Económica: ${vuelo.getPrecioEconomica():.2f}")
    print(f"  Precio Ejecutiva: ${vuelo.getPrecioEjecutiva():.2f}")
    print(f"  Asientos disponibles (Económica): {disponibles_economico}")
    print(f"  Asientos disponibles (Ejecutiva): {disponibles_ejecutivo}")
    print("-" * 40)

# Funcion para consultar todos los vuelos
def consultar_vuelos():
    if not vuelos:
        print("No hay vuelos registrados.")
        return

    print("Vuelos disponibles:")
    for vuelo in vuelos:
        mostrar_vuelo(vuelo)

# Funcion para filtrar vuelos por origen - destino
def consultar_vuelos_por_ruta(origen, destino):
    vuelos_disponibles = [
        v for v in vuelos 
        if v.getOrigen().lower() == origen.lower() and v.getDestino().lower() == destino.lower()
    ]

    if not vuelos_disponibles:
        print(f"No hay vuelos disponibles desde {origen} hacia {destino}.")
        return

    print(f"Vuelos desde {origen} hacia {destino}:\n")
    for vuelo in vuelos_disponibles:
        mostrar_vuelo(vuelo)


# Funcion para buscar un vuelo por su id y mandar el objeto a la funcion mostrar_vuelo
def consultar_vuelo_por_id(id_vuelo):
    vuelo = next((v for v in vuelos if v.getId() == id_vuelo), None)
    if not vuelo:
        print("No se encontró un vuelo con ese ID.")
        return
    mostrar_vuelo(vuelo)


###################################### FUNCIONES PARA CONSULTAR RESERVAS ###############################
# Funcion para mostrar una reserva
def mostrar_reserva(reserva):
    pasajero = next((p for p in pasajeros if p.getId() == reserva.getIdPasajero()), None)
    vuelo = next((v for v in vuelos if v.getId() == reserva.getIdVuelo()), None)

    if not pasajero:
        raise ValueError(f"  El pasajero {reserva.getIdPasajero()} no fue encontrado")
    if not vuelo:
        raise ValueError(f"  El vuelo {reserva.getIdVuelo()} no fue encontrado")

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

# Funcion para mostrar las reservas de un pasajero
def consultar_reservas_por_pasajero(id_pasajero):
    pasajero = next((p for p in pasajeros if p.getId() == id_pasajero), None)

    if not pasajero:
        print("Pasajero no encontrado.")
        return

    reservas_pasajero = [r for r in reservas if r.getIdPasajero() == id_pasajero]

    if not reservas_pasajero:
        print("El pasajero no tiene reservas registradas.")
        return

    print(f"Reservas para el pasajero {pasajero.getNombre()} (ID: {id_pasajero}):\n")
    for reserva in reservas_pasajero:
        mostrar_reserva(reserva)

# Funcion para consultar solo las reservas activas
def consultar_reservas_activas():
    reservas_activas = [r for r in reservas if r.getEstado().lower() == "activa"]

    if not reservas_activas:
        print("No hay reservas activas.")
        return

    print("Reservas activas:\n")
    for reserva in reservas_activas:
        mostrar_reserva(reserva)

# Funcion para encontrar una reserva por su id y mandar el objeto a la funcion mostrar_reserva
def consultar_reserva_por_id(id_reserva):
    reserva = next((r for r in reservas if r.getId() == id_reserva), None)
    if not reserva:
        print("No se encontró una reserva con ese ID.")
        return
    mostrar_reserva(reserva)


###################################### FUNCIONES PARA CONSULTAR PASAJEROS ###############################

# Función para mostrar un pasajero
def mostrar_pasajero(pasajero):
    print(f"ID: {pasajero.getId()}")
    print(f"  Nombre: {pasajero.getNombre()}")
    print(f"  Correo: {pasajero.getCorreo()}")
    print("-" * 40)

# Función para consultar un pasajero por su ID
def consultar_pasajero(id_pasajero):
    pasajero = next((p for p in pasajeros if p.getId() == id_pasajero), None)
    if not pasajero:
        print("No se encontró un pasajero con ese ID.")
        return
    mostrar_pasajero(pasajero)

# Función para mostrar los pasajeros de un vuelo específico
def mostrar_pasajeros_vuelo(id_vuelo):
    vuelo = next((v for v in vuelos if v.getId() == id_vuelo), None)
    if not vuelo:
        print("No se encontró un vuelo con ese ID.")
        return

    reservas_vuelo = [r for r in reservas if r.getIdVuelo() == id_vuelo and r.getEstado().lower() == "activa"]

    if not reservas_vuelo:
        print("No hay pasajeros con reservas activas para este vuelo.")
        return

    print(f"Pasajeros con reservas activas para el vuelo {id_vuelo}:\n")
    for reserva in reservas_vuelo:
        pasajero = next((p for p in pasajeros if p.getId() == reserva.getIdPasajero()), None)
        if pasajero:
            mostrar_pasajero(pasajero)
        else:
            print(f"  [!] Pasajero con ID {reserva.getIdPasajero()} no encontrado.")
