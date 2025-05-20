from vistas import mostrar_vuelo, mostrar_reserva, mostrar_pasajero, mostrar_avion
from persistencia import *
from modelos import ReservaEjecutiva, ReservaEconomica

############################## FUNCIONES PARA CREAR INSTANCIAS #####################################
# Funcion para crear un pasajero
def crear_pasajero(id_pasajero, nombre, correo):
    if not isinstance(id_pasajero, int) or id_pasajero < 0:
        print("El ID del pasajero debe ser un número entero no negativo.")
        return None

    if obtener_pasajero(id_pasajero) is not None:
        print(f"Ya existe un pasajero con ID {id_pasajero}.")
        return None

    if not isinstance(nombre, str) or nombre.strip() == "":
        print("El nombre del pasajero no puede estar vacío.")
        return None

    if not isinstance(correo, str) or "@" not in correo or "." not in correo:
        print("El correo debe tener formato válido (ejemplo@dominio.com).")
        return None

    pasajero = Pasajero(id_pasajero, nombre.strip(), correo.strip())
    pasajeros.append(pasajero)
    guardar()
    print("Pasajero creado exitosamente.")
    return pasajero

# Funcion para crear un avion
def crear_avion(id_avion, modelo, capacidad_economica, capacidad_ejecutiva):
    if not isinstance(id_avion, int) or id_avion < 0:
        print("El ID del avión debe ser un número entero no negativo.")
        return None

    if obtener_avion(id_avion) is not None:
        print(f"Ya existe un avión con ID {id_avion}.")
        return None

    if not isinstance(modelo, str) or modelo.strip() == "":
        print("El modelo del avión no puede estar vacío.")
        return None

    if not isinstance(capacidad_economica, int) or capacidad_economica < 0:
        print("La capacidad económica debe ser un número entero no negativo.")
        return None

    if not isinstance(capacidad_ejecutiva, int) or capacidad_ejecutiva < 0:
        print("La capacidad ejecutiva debe ser un número entero no negativo.")
        return None

    avion = Avion(id_avion, modelo.strip(), capacidad_economica, capacidad_ejecutiva)
    aviones.append(avion)
    guardar()
    print("Avión creado exitosamente.")
    return avion

# Funcion para crear un vuelo
def crear_vuelo(id_vuelo, id_avion, origen, destino, fecha_hora_salida, fecha_hora_llegada, precio_economica, precio_ejecutiva):
    if not isinstance(id_vuelo, int) or id_vuelo < 0:
        print("El ID del vuelo debe ser un número entero no negativo.")
        return None

    if obtener_vuelo(id_vuelo) is not None:
        print(f"Ya existe un vuelo con ID {id_vuelo}.")
        return None

    if not isinstance(id_avion, int) or id_avion < 0:
        print("El ID del avión debe ser un número entero no negativo.")
        return None

    if obtener_avion(id_avion) is None:
        print(f"No existe ningún avión con ID {id_avion}.")
        return None
    
    if not isinstance(origen, str) or origen.strip() == "":
        print(f"Origen inválido: debe ser una cadena no vacía.")
        return None

    if not isinstance(destino, str) or destino.strip() == "":
        print(f"Destino inválido: debe ser una cadena no vacía.")
        return None

    if not isinstance(fecha_hora_salida, datetime):
        print(f"Fecha de salida inválida: debe ser un objeto datetime.")
        return None

    if not isinstance(fecha_hora_llegada, datetime):
        print(f"Fecha de llegada inválida: debe ser un objeto datetime.")
        return None

    if fecha_hora_llegada < fecha_hora_salida:
        print("La fecha de llegada debe ser posterior a la fecha de salida.")
        return None

    if not isinstance(precio_economica, (int, float)) or precio_economica < 0:
        print("El precio en económica debe ser un número no negativo.")
        return None

    if not isinstance(precio_ejecutiva, (int, float)) or precio_ejecutiva < 0:
        print("El precio en ejecutiva debe ser un número no negativo.")
        return None

    vuelo = Vuelo(id_vuelo, id_avion, origen, destino, fecha_hora_salida, fecha_hora_llegada, precio_economica, precio_ejecutiva)
    vuelos.append(vuelo)
    guardar()
    print("Vuelo creado exitosamente.")
    return vuelo

# Funcion para crear una reserva
def crear_reserva(id_pasajero, id_vuelo, tipo_asiento):
    if not isinstance(id_pasajero, int) or id_pasajero < 0:
        print("El ID del pasajero debe ser un entero no negativo.")
        return None

    if obtener_pasajero(id_pasajero) is None:
        print(f"No existe ningún pasajero con ID {id_pasajero}.")
        return None

    if not isinstance(id_vuelo, int) or id_vuelo < 0:
        print("El ID del vuelo debe ser un entero no negativo.")
        return None

    if obtener_vuelo(id_vuelo) is None:
        print(f"No existe ningún vuelo con ID {id_vuelo}.")
        return None

    if not isinstance(tipo_asiento, str) or tipo_asiento.lower() not in ["economico", "ejecutivo"]:
        print("Tipo de asiento inválido. Debe ser 'economico' o 'ejecutivo'.")
        return None

    tipo_asiento = tipo_asiento.lower()

    avion = obtener_avion_por_vuelo(id_vuelo)
    if avion is None:
        print("No se pudo encontrar el avión asociado al vuelo.")
        return None

    cantidad_actual = contar_reservas_activas(id_vuelo, tipo_asiento)

    if tipo_asiento == "economico":
        if cantidad_actual >= avion.getCapacidadEconomica():
            print("No hay asientos disponibles en clase económica.")
            return None
        reserva = ReservaEconomica(len(reservas) + 1, id_pasajero, id_vuelo)
    else:
        if cantidad_actual >= avion.getCapacidadEjecutiva():
            print("No hay asientos disponibles en clase ejecutiva.")
            return None
        reserva = ReservaEjecutiva(len(reservas) + 1, id_pasajero, id_vuelo)

    reservas.append(reserva)
    guardar()
    print(f"Reserva realizada exitosamente para el pasajero {id_pasajero} en el vuelo {id_vuelo}, ({tipo_asiento}).")
    return reserva

############################## FUNCIONES PARA MANIPULAR RESERVAS ###################################
# Funcion para cambiar una reserva de economica a ejecutiva
def cambiar_a_ejecutiva(id_reserva):
    reserva = obtener_reserva(id_reserva)
    if reserva is None:
        print("No se encontró una reserva con ese ID.")
        return

    if reserva.getTipoAsiento() != "economico":
        print("La reserva no es de clase económica, no se puede cambiar.")
        return

    id_vuelo = reserva.getIdVuelo()
    vuelo = obtener_vuelo(id_vuelo)
    if vuelo is None:
        print(f"No existe ningún vuelo asociado a esa reserva")
        return

    avion = obtener_avion_por_vuelo(id_vuelo)
    if avion is None:
        print(f"No existe ningún avión asociado a ese vuelo")
        return

    cantidad_actual = contar_reservas_activas(id_vuelo, "ejecutivo")
    if cantidad_actual >= avion.getCapacidadEjecutiva():
        print("No hay asientos ejecutivos disponibles.")
        return

    reserva.setTipoAsiento("ejecutivo")
    guardar()
    print(f"Reserva {reserva.getId()} actualizada a clase ejecutiva.")


#################################### FUNCIONES PARA CONSULTAR VUELOS #################################
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
    if not isinstance(origen, str) or origen.strip() == "":
        print("El origen debe ser una cadena no vacía.")
        return
    if not isinstance(destino, str) or destino.strip() == "":
        print("El destino debe ser una cadena no vacía.")
        return

    origen = origen.lower().strip()
    destino = destino.lower().strip()

    vuelos_disponibles = [
        v for v in vuelos 
        if v.getOrigen().lower() == origen and v.getDestino().lower() == destino
    ]

    if not vuelos_disponibles:
        print(f"No hay vuelos disponibles desde {origen} hacia {destino}.")
        return

    print(f"Vuelos desde {origen} hacia {destino}:\n")
    for vuelo in vuelos_disponibles:
        mostrar_vuelo(vuelo)


# Funcion para buscar un vuelo por su id y mandar el objeto a la funcion mostrar_vuelo
def consultar_vuelo_por_id(id_vuelo):
    if not isinstance(id_vuelo, int) or id_vuelo < 0:
        print("El ID del vuelo debe ser un número entero no negativo.")
        return

    vuelo = obtener_vuelo(id_vuelo)
    if not vuelo:
        print(f"No se encontró un vuelo con ID {id_vuelo}.")
        return

    mostrar_vuelo(vuelo)


###################################### FUNCIONES PARA CONSULTAR RESERVAS ###############################
# Funcion para mostrar las reservas de un pasajero
def consultar_reservas_por_pasajero(id_pasajero):
    if not isinstance(id_pasajero, int) or id_pasajero < 0:
        print("El ID del pasajero debe ser un número entero no negativo.")
        return

    pasajero = obtener_pasajero(id_pasajero)
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
    reservas_activas = [r for r in reservas if r.getEstado().strip().lower() == "activa"]

    if not reservas_activas:
        print("No hay reservas activas.")
        return

    print("Reservas activas:\n")
    for reserva in reservas_activas:
        mostrar_reserva(reserva)


# Funcion para encontrar una reserva por su id y mandar el objeto a la funcion mostrar_reserva
def consultar_reserva_por_id(id_reserva):
    if not isinstance(id_reserva, int) or id_reserva < 0:
        print("El ID de la reserva debe ser un número entero no negativo.")
        return

    reserva = obtener_reserva(id_reserva)
    if reserva is None:
        print(f"No se encontró una reserva con ID {id_reserva}.")
        return

    mostrar_reserva(reserva)


###################################### FUNCIONES PARA CONSULTAR PASAJEROS ###############################
# Función para consultar un pasajero por su ID
def consultar_pasajero(id_pasajero):
    if not isinstance(id_pasajero, int) or id_pasajero < 0:
        print("El ID del pasajero debe ser un número entero no negativo.")
        return

    pasajero = obtener_pasajero(id_pasajero)
    if not pasajero:
        print("No se encontró un pasajero con ese ID.")
        return

    mostrar_pasajero(pasajero)


# Función para mostrar los pasajeros de un vuelo específico
def mostrar_pasajeros_vuelo(id_vuelo):
    if not isinstance(id_vuelo, int) or id_vuelo < 0:
        print("El ID del vuelo debe ser un número entero no negativo.")
        return

    vuelo = obtener_vuelo(id_vuelo)
    if vuelo is None:
        print("No se encontró un vuelo con ese ID.")
        return

    reservas_vuelo = [
        r for r in reservas if r.getIdVuelo() == id_vuelo and r.getEstado().lower() == "activa"
    ]

    if not reservas_vuelo:
        print("No hay pasajeros con reservas activas para este vuelo.")
        return

    print(f"Pasajeros con reservas activas para el vuelo {id_vuelo}:\n")
    for reserva in reservas_vuelo:
        pasajero = obtener_pasajero(reserva.getIdPasajero())
        if pasajero:
            mostrar_pasajero(pasajero)
        else:
            print(f"Pasajero con ID {reserva.getIdPasajero()} no encontrado.")


################################## FUNCIONES PARA CONSULTAR AVIONES ###################################
# Funcion para consultar un avion por id
def consultar_avion_por_id(id_avion):
    if not isinstance(id_avion, int) or id_avion < 0:
        print("El ID del avión debe ser un número entero no negativo.")
        return

    avion = obtener_avion(id_avion)
    if avion is None:
        print(f"No se encontró un avión con ID {id_avion}.")
        return

    mostrar_avion(avion)


# Funcion para consultar todos los aviones
def consultar_todos_los_aviones():
    if not aviones:
        print("No hay aviones registrados.")
        return

    print("Aviones registrados:\n")
    for avion in aviones:
        mostrar_avion(avion)
