# Sistema de manejo de vuelos de una aerolinea
###################################### CLASES ########################################
class Pasajero:
    def __init__(self, id_pasajero, nombre, correo):
        self.setId(id_pasajero)
        self.setNombre(nombre)
        self.setCorreo(correo)

    # Métodos set
    def setId(self, nuevoId):
        self.__id = nuevoId

    def setNombre(self, nuevoNombre):
        self.__nombre = nuevoNombre

    def setCorreo(self, nuevoCorreo):
        self.__correo = nuevoCorreo

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
        self.__id = nuevoId

    def setModelo(self, nuevoModelo):
        self.__modelo = nuevoModelo

    def setCapacidadEconomica(self, nuevaCapacidad):
        self.__capacidad_economica = nuevaCapacidad

    def setCapacidadEjecutiva(self, nuevaCapacidad):
        self.__capacidad_ejecutiva = nuevaCapacidad

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
    def __init__(self, id_vuelo, id_avion, origen, destino, salida, llegada, precio_economica, precio_ejecutiva):
        self.setId(id_vuelo)
        self.setIdAvion(id_avion)
        self.setOrigen(origen)
        self.setDestino(destino)
        self.setFechaHoraSalida(salida)
        self.setFechaHoraLlegada(llegada)
        self.setPrecioEconomica(precio_economica)
        self.setPrecioEjecutiva(precio_ejecutiva)

    # Métodos set
    def setId(self, nuevoId):
        self.__id = nuevoId

    def setIdAvion(self, id_avion):
        self.__id_avion = id_avion

    def setOrigen(self, nuevoOrigen):
        self.__origen = nuevoOrigen

    def setDestino(self, nuevoDestino):
        self.__destino = nuevoDestino

    def setFechaHoraSalida(self, nuevaSalida):
        self.__fecha_hora_salida = nuevaSalida

    def setFechaHoraLlegada(self, nuevaLlegada):
        self.__fecha_hora_llegada = nuevaLlegada


    def setPrecioEconomica(self, nuevoPrecio):
        self.__precio_economica = nuevoPrecio

    def setPrecioEjecutiva(self, nuevoPrecio):
        self.__precio_ejecutiva = nuevoPrecio

    # Métodos get
    def getId(self):
        return self.__id

    def getIdAvion(self):
        return self.__id_avion

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

class Reserva:
    def __init__(self, id, id_pasajero, id_vuelo, tipo_asiento):
        self.setId(id)
        self.setIdPasajero(id_pasajero)
        self.setIdVuelo(id_vuelo)
        self.setTipoAsiento(tipo_asiento)
        self.__estado = "activa"
    
    # Métodos set
    def setId(self, id):
        self.__id = id

    def setIdPasajero(self, id_pasajero):
        self.__id_pasajero = id_pasajero

    def setIdVuelo(self, id_vuelo):
        self.__id_vuelo = id_vuelo

    def setTipoAsiento(self, tipo):
        self.__tipo_asiento = tipo.lower()

    def setEstado(self, nuevo_estado):
        self.__estado = nuevo_estado

    # Métodos get
    def getId(self):
        return self.__id
    
    def getIdPasajero(self):
        return self.__id_pasajero

    def getIdVuelo(self):
        return self.__id_vuelo

    def getTipoAsiento(self):
        return self.__tipo_asiento

    def getEstado(self):
        return self.__estado


class ReservaEconomica(Reserva):
    def __init__(self, id_reserva, id_pasajero, id_vuelo):
        super().__init__(id_reserva, id_pasajero, id_vuelo, "economico")

class ReservaEjecutiva(Reserva):
    def __init__(self, id_reserva, id_pasajero, id_vuelo):
        super().__init__(id_reserva, id_pasajero, id_vuelo, "ejecutivo")