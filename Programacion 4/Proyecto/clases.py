# Sistema de manejo de vuelos de una aerolinea
from datetime import datetime

class Pasajero:
    def __init__(self, id_pasajero, nombre, correo):
        self.setId(id_pasajero)
        self.setNombre(nombre)
        self.setCorreo(correo)

    # Métodos set
    def setId(self, nuevoId):
        if isinstance(nuevoId, int) and nuevoId >= 0:
            self.__id = nuevoId
        else:
            raise ValueError("ID inválido: debe ser un entero no negativo.")

    def setNombre(self, nuevoNombre):
        if isinstance(nuevoNombre, str) and nuevoNombre.strip() != "":
            self.__nombre = nuevoNombre
        else:
            raise ValueError("Nombre inválido: debe ser una cadena no vacía.")

    def setCorreo(self, nuevoCorreo):
        if isinstance(nuevoCorreo, str) and "@" in nuevoCorreo and "." in nuevoCorreo:
            self.__correo = nuevoCorreo
        else:
            raise ValueError("Correo inválido: debe tener formato de email.")

    # Métodos get
    def getId(self):
        return self.__id

    def getNombre(self):
        return self.__nombre

    def getCorreo(self):
        return self.__correo

class Avion:
    def __init__(self, id_avion, modelo, capacidad_economica, capacidad_ejecutiva):
        self.setId(id_avion)
        self.setModelo(modelo)
        self.setCapacidadEconomica(capacidad_economica)
        self.setCapacidadEjecutiva(capacidad_ejecutiva)

    # Métodos set
    def setId(self, nuevoId):
        if isinstance(nuevoId, int) and nuevoId >= 0:
            self.__id = nuevoId
        else:
            raise ValueError("ID inválido: debe ser un número entero no negativo.")

    def setModelo(self, nuevoModelo):
        if isinstance(nuevoModelo, str) and nuevoModelo.strip() != "":
            self.__modelo = nuevoModelo
        else:
            raise ValueError("Modelo inválido: debe ser una cadena no vacía.")

    def setCapacidadEconomica(self, nuevaCapacidad):
        if isinstance(nuevaCapacidad, int) and nuevaCapacidad >= 0:
            self.__capacidad_economica = nuevaCapacidad
        else:
            raise ValueError("Capacidad económica inválida: debe ser un número entero no negativo.")

    def setCapacidadEjecutiva(self, nuevaCapacidad):
        if isinstance(nuevaCapacidad, int) and nuevaCapacidad >= 0:
            self.__capacidad_ejecutiva = nuevaCapacidad
        else:
            raise ValueError("Capacidad ejecutiva inválida: debe ser un número entero no negativo.")

    # Métodos get
    def getId(self):
        return self.__id

    def getModelo(self):
        return self.__modelo

    def getCapacidadEconomica(self):
        return self.__capacidad_economica

    def getCapacidadEjecutiva(self):
        return self.__capacidad_ejecutiva

class Vuelo:
    def __init__(self, id_vuelo, avion, origen, destino, salida, llegada, precio_economica, precio_ejecutiva):
        self.setId(id_vuelo)
        self.setAvion(avion)
        self.setOrigen(origen)
        self.setDestino(destino)
        self.setFechaHoraSalida(salida)
        self.setFechaHoraLlegada(llegada)
        self.setPrecioEconomica(precio_economica)
        self.setPrecioEjecutiva(precio_ejecutiva)
        self.__reservas = []  # Lista vacía para ir guardando reservas

    # Métodos set
    def setId(self, nuevoId):
        if isinstance(nuevoId, int) and nuevoId >= 0:
            self.__id = nuevoId
        else:
            raise ValueError("ID inválido: debe ser un número entero no negativo.")

    def setAvion(self, nuevoAvion):
        if isinstance(nuevoAvion, Avion):
            self.__avion = nuevoAvion
        else:
            raise ValueError("Debe asignarse un objeto de tipo avión.")

    def setOrigen(self, nuevoOrigen):
        if isinstance(nuevoOrigen, str) and nuevoOrigen.strip() != "":
            self.__origen = nuevoOrigen
        else:
            raise ValueError("Origen inválido: debe ser una cadena no vacía.")

    def setDestino(self, nuevoDestino):
        if isinstance(nuevoDestino, str) and nuevoDestino.strip() != "":
            self.__destino = nuevoDestino
        else:
            raise ValueError("Destino inválido: debe ser una cadena no vacía.")

    def setFechaHoraSalida(self, nuevaSalida):
        if isinstance(nuevaSalida, datetime):
            self.__fecha_hora_salida = nuevaSalida
        else:
            raise ValueError("Fecha de salida inválida: debe ser un objeto datetime.")

    def setFechaHoraLlegada(self, nuevaLlegada):
        if isinstance(nuevaLlegada, datetime):
            self.__fecha_hora_llegada = nuevaLlegada
        else:
            raise ValueError("Fecha de llegada inválida: debe ser un objeto datetime.")

    def setPrecioEconomica(self, nuevoPrecio):
        if isinstance(nuevoPrecio, (int, float)) and nuevoPrecio > 0:
            self.__precio_economica = nuevoPrecio
        else:
            raise ValueError("Precio económica inválido: debe ser positivo.")

    def setPrecioEjecutiva(self, nuevoPrecio):
        if isinstance(nuevoPrecio, (int, float)) and nuevoPrecio > 0:
            self.__precio_ejecutiva = nuevoPrecio
        else:
            raise ValueError("Precio ejecutiva inválido: debe ser positivo.")

    # Métodos get
    def getId(self):
        return self.__id

    def getAvion(self):
        return self.__avion

    def getOrigen(self):
        return self.__origen

    def getDestino(self):
        return self.__destino

    def getFechaHoraSalida(self):
        return self.__fecha_hora_salida

    def getFechaHoraLlegada(self):
        return self.__fecha_hora_llegada

    def getPrecioEconomica(self):
        return self.__precio_economica

    def getPrecioEjecutiva(self):
        return self.__precio_ejecutiva

    def getReservas(self):
        return self.__reservas

    def agregarReserva(self, reserva):
        self.__reservas.append(reserva)

class Reserva:
    def __init__(self, pasajero, vuelo, tipo_asiento):
        self.setPasajero(pasajero)
        self.setVuelo(vuelo)
        self.setTipoAsiento(tipo_asiento)
        self.__estado = "activa"  # puede ser 'activa' o 'cancelada'

    # Métodos set
    def setPasajero(self, pasajero):
        if isinstance(pasajero, Pasajero):
            self.__pasajero = pasajero
        else:
            raise ValueError("Debe asignarse un objeto de tipo Pasajero.")

    def setVuelo(self, vuelo):
        if isinstance(vuelo, Vuelo):
            self.__vuelo = vuelo
        else:
            raise ValueError("Debe asignarse un objeto de tipo Vuelo.")

    def setTipoAsiento(self, tipo):
        if tipo.lower() in ["economico", "ejecutivo"]:
            self.__tipo_asiento = tipo.lower()
        else:
            raise ValueError("El tipo de asiento debe ser 'economico' o 'ejecutivo'.")

    def setEstado(self, nuevo_estado):
        if nuevo_estado in ["activa", "cancelada"]:
            self.__estado = nuevo_estado
        else:
            raise ValueError("Estado inválido. Use 'activa' o 'cancelada'.")

    # Métodos get
    def getPasajero(self):
        return self.__pasajero

    def getVuelo(self):
        return self.__vuelo

    def getTipoAsiento(self):
        return self.__tipo_asiento

    def getEstado(self):
        return self.__estado

class ReservaEconomica(Reserva):
    def __init__(self, pasajero, vuelo):
        super().__init__(pasajero, vuelo, "economico")
    
class ReservaEjecutiva(Reserva):
    def __init__(self, pasajero, vuelo):
        super().__init__(pasajero, vuelo, "ejecutivo")