# ===================== CLASES =====================

class Animal:
    def __init__(self, nombre, especie, edad, color, peso):
        self.setNombre(nombre)
        self.setEspecie(especie)
        self.setEdad(edad)
        self.setColor(color)
        self.setPeso(peso)

    # Metodos set
    def setNombre(self, nuevoNombre):
        if isinstance(nuevoNombre, str):
            self.__nombre = nuevoNombre
        else:
            raise ValueError("Tipo de dato no permitido, ingrese una cadena")
        
    def setEspecie(self, nuevaEspecie):
        if isinstance(nuevaEspecie, str):
            self.__especie = nuevaEspecie
        else:
            raise ValueError("Tipo de dato no permitido, ingrese una cadena")
        
    def setEdad(self, nuevaEdad):
        if isinstance(nuevaEdad, int) and nuevaEdad >= 0:
            self.__edad = nuevaEdad
        else:
            raise ValueError("Tipo de dato no permitido, ingrese un entero no negativo")
        
    def setColor(self, nuevoColor):
        if isinstance(nuevoColor, str):
            self.__color = nuevoColor
        else:
            raise ValueError("Tipo de dato no permitido, ingrese una cadena")
        
    def setPeso(self, nuevoPeso):
        if isinstance(nuevoPeso, (int, float)) and nuevoPeso > 0.0:
            self.__peso = nuevoPeso
        else:
            raise ValueError("Tipo de dato no permitido, ingrese un numero positivo")
        
    # Metodos get
    def getNombre(self):
        return self.__nombre
    
    def getEspecie(self):
        return self.__especie
    
    def getEdad(self):
        return self.__edad
    
    def getColor(self):
        return self.__color
    
    def getPeso(self):
        return self.__peso
    

    def mostrar_info(self):
        return f"{self.getNombre()}, {self.getEspecie()}, {self.getEdad()} años, {self.getColor()}, {self.getPeso()} kg"
    
##################################################################################################################
class Cliente:
    def __init__(self, nombre, cedula, direccion, telefono, correo):
        self.setNombre(nombre)
        self.setCedula(cedula)
        self.setDireccion(direccion)
        self.setTelefono(telefono)
        self.setCorreo(correo)

    # Metodos set
    def setNombre(self, nuevoNombre):
        if isinstance(nuevoNombre, str):
            self.__nombre = nuevoNombre
        else:
            raise ValueError("Tipo de dato no permitido, ingrese una cadena")
        
    def setCedula(self, nuevaCedula):
        if isinstance(nuevaCedula, str):
            self.__cedula = nuevaCedula
        else:
            raise ValueError("Tipo de dato no permitido, ingrese una cadena")
        
    def setDireccion(self, nuevaDireccion):
        if isinstance(nuevaDireccion, str):
            self.__direccion = nuevaDireccion
        else:
            raise ValueError("Tipo de dato no permitido, ingrese una cadena")
        
    def setTelefono(self, nuevoTelefono):
        if isinstance(nuevoTelefono, str):
            self.__telefono = nuevoTelefono
        else:
            raise ValueError("Tipo de dato no permitido, ingrese una cadena")
        
    def setCorreo(self, nuevoCorreo):
        if isinstance(nuevoCorreo, str):
            self.__correo = nuevoCorreo
        else:
            raise ValueError("Tipo de dato no permitido, ingrese una cadena")
        
    # Metodos get
    def getNombre(self):
        return self.__nombre
    
    def getCedula(self):
        return self.__cedula
        
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def getCorreo(self):
        return self.__correo


    def mostrar_info(self):
        return f"{self.getNombre()}, C.C: {self.getCedula()}, {self.getTelefono()}, {self.getCorreo()}"
    
##################################################################################################################
# Subclases de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, color, peso, raza):
        super().__init__(nombre, "Perro", edad, color, peso)
        self.setRaza(raza)

    # Métodos set y get solo para 'raza'
    def setRaza(self, nuevaRaza):
        if isinstance(nuevaRaza, str):
            self.__raza = nuevaRaza
        else:
            raise ValueError("Tipo de dato no permitido, ingrese una cadena")

    def getRaza(self):
        return self.__raza

    def ladrar(self):
        return f"{self.getNombre()} dice: ¡Guau!"

##################################################################################################################
class Gato(Animal):
    def __init__(self, nombre, edad, color, peso, pelaje):
        super().__init__(nombre, "Gato", edad, color, peso)
        self.setPelaje(pelaje)

    def setPelaje(self, nuevoPelaje):
        if isinstance(nuevoPelaje, str):
            self.__pelaje = nuevoPelaje
        else:
            raise ValueError("Tipo de dato no permitido, ingrese una cadena")

    def getPelaje(self):
        return self.__pelaje

    def maullar(self):
        return f"{self.getNombre()} dice: Miau"

##################################################################################################################
class Pez(Animal):
    def __init__(self, nombre, edad, color, peso, tipo_agua):
        super().__init__(nombre, "Pez", edad, color, peso)
        self.setTipo_agua(tipo_agua)

    def setTipo_agua(self, nuevoTipo_agua):
        if isinstance(nuevoTipo_agua, str):
            self.__tipo_agua = nuevoTipo_agua
        else:
            raise ValueError("Tipo de dato no permitido, ingrese una cadena")
        
    def getTipo_agua(self):
        return self.__tipo_agua

    def nadar(self):
        return f"{self.getNombre()} nada en agua {self.getTipo_agua()}"

##################################################################################################################
# Subclases de Cliente
class ClienteFrecuente(Cliente):
    def __init__(self, nombre, cedula, direccion, telefono, correo, puntos):
        super().__init__(nombre, cedula, direccion, telefono, correo)
        self.setPuntos(puntos)

    def setPuntos(self, nuevoPuntos):
        if isinstance(nuevoPuntos, int) and nuevoPuntos >= 0:
            self.__puntos = nuevoPuntos
        else:
            raise ValueError("Tipo de dato no permitido, ingrese un entero no negativo")
        
    def getPuntos(self):
        return self.__puntos

    def acumular_puntos(self, cantidad):
        if isinstance(cantidad, int) and cantidad > 0:
            self.__puntos += cantidad
            return f"{self.getNombre()} ahora tiene {self.__puntos} puntos."
        else:
            raise ValueError("La cantidad debe ser un número entero positivo")

##################################################################################################################
class ClienteVIP(Cliente):
    def __init__(self, nombre, cedula, direccion, telefono, correo, descuento):
        super().__init__(nombre, cedula, direccion, telefono, correo)
        self.setDescuento(descuento)

    def setDescuento(self, nuevoDescuento):
        if isinstance(nuevoDescuento, (int, float)) and nuevoDescuento >= 0.0:
            self.__descuento = nuevoDescuento
        else:
            raise ValueError("Tipo de dato no permitido, ingrese un numero no negativo")
        
    def getDescuento(self):
        return self.__descuento
    
    def aplicar_descuento(self, precio):
        precio_final = precio * (1 - self.getDescuento())
        return f"Precio con descuento VIP: ${precio_final:.2f}"

##################################################################################################################
class Adopcion:
    def __init__(self, animal, cliente, fecha):
        self.setAnimal(animal)
        self.setCliente(cliente)
        self.setFecha(fecha)

    # Metodos set
    def setAnimal(self, nuevoAnimal):
        if isinstance(nuevoAnimal, Animal):
            self.__animal = nuevoAnimal
        else:
            raise ValueError("Tipo de dato no permitido, ingrese una cadena")
        
    def setCliente(self, nuevoCliente):
        if isinstance(nuevoCliente, Cliente):
            self.__cliente = nuevoCliente
        else:
            raise ValueError("Tipo de dato no permitido, ingrese una cadena")
        
    def setFecha(self, nuevaFecha):
        if isinstance(nuevaFecha, str):
            self.__fecha = nuevaFecha
        else:
            raise ValueError("Tipo de dato no permitido, ingrese una cadena")
    
    # Metodos get
    def getAnimal(self):
        return self.__animal
    
    def getCliente(self):
        return self.__cliente
    
    def getFecha(self):
        return self.__fecha


    def resumen_adopcion(self):
        return f"{self.getCliente().getNombre()} adoptó a {self.getAnimal().getNombre()} el {self.getFecha()}"