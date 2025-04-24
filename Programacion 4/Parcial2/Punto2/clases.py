class Habitacion:
    def __init__(self, numero, precio, estado):
        self.setNumero(numero)
        self.setPrecio(precio)
        self.setEstado(estado)

    # Metodos set
    def setNumero(self, nuevoNumero):
        if isinstance(nuevoNumero, int) and nuevoNumero >= 0:
            self.__numero = nuevoNumero
        else:
            raise ValueError("Tipo de dato no permitido, ingrese un numero no negativo")
        
    def setPrecio(self, nuevoPrecio):
        if isinstance(nuevoPrecio, (int, float)) and nuevoPrecio > 0:
            self.__precio = nuevoPrecio
        else:
            raise ValueError("Tipo de dato no permitido, ingrese un precio positivo")

    def setEstado(self, nuevoEstado):
        if isinstance(nuevoEstado, str) and nuevoEstado in ["disponible", "reservado"]:
            self.__estado = nuevoEstado
        else:
            raise ValueError("Estado no válido, use 'disponible' o 'reservado'")


    # Metodos get
    def getNumero(self):
        return self.__numero
    
    def getPrecio(self):
        return self.__precio
    
    def getEstado(self):
        return self.__estado
    

class HabitacionSimple(Habitacion):
    def __init__(self, numero, precio, estado):
        super().__init__(numero, precio, estado)

class HabitacionDoble(Habitacion):
    def __init__(self,  numero, precio, estado, desayuno, spa):
        super().__init__(numero, precio, estado)
        self.setDesayuno(desayuno)
        self.setSpa(spa)

    # Metodos set
    def setDesayuno(self, nuevoDesayuno):
        if isinstance(nuevoDesayuno, bool):
            self.__desayuno = nuevoDesayuno
        else:
            raise ValueError("Tipo no permitido, ingrese un booleano")
        
    def setSpa(self, nuevoSpa):
        if isinstance(nuevoSpa, bool):
            self.__spa = nuevoSpa
        else:
            raise ValueError("Tipo no permitido, ingrese un booleano")
        

    # Metodos get
    def getDesayuno(self):
        return self.__desayuno
    
    def getSpa(self):
        return self.__spa
    

class Suite(Habitacion):
    def __init__(self,  numero, precio, estado, desayuno, spa, gym):
        super().__init__(numero, precio, estado)
        self.setDesayuno(desayuno)
        self.setSpa(spa)
        self.setGym(gym)

    # Metodos set
    def setDesayuno(self, nuevoDesayuno):
        if isinstance(nuevoDesayuno, bool):
            self.__desayuno = nuevoDesayuno
        else:
            raise ValueError("Tipo no permitido, ingrese un booleano")
        
    def setSpa(self, nuevoSpa):
        if isinstance(nuevoSpa, bool):
            self.__spa = nuevoSpa
        else:
            raise ValueError("Tipo no permitido, ingrese un booleano")
        
    def setGym(self, nuevoGym):
        if isinstance(nuevoGym, bool):
            self.__gym= nuevoGym
        else:
            raise ValueError("Tipo no permitido, ingrese un booleano")
        

    # Metodos get
    def getDesayuno(self):
        return self.__desayuno
    
    def getSpa(self):
        return self.__spa
    
    def getGym(self):
        return self.__gym