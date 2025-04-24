# --------------------- CLASES --------------------------
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.setNombre(nombre)
        self.setPrecio(precio)
        self.setCantidad(cantidad)

    # Metodos set
    def setNombre(self, nuevoNombre):
        if isinstance(nuevoNombre, str) and nuevoNombre.strip():
            self.__nombre = nuevoNombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía")

    def setPrecio(self, nuevoPrecio):
        if isinstance(nuevoPrecio, (int, float)) and nuevoPrecio > 0:
            self.__precio = nuevoPrecio
        else:
            raise ValueError("El precio debe ser un número mayor a 0")

    def setCantidad(self, nuevaCantidad):
        if isinstance(nuevaCantidad, int) and nuevaCantidad >= 0:
            self.__cantidad = nuevaCantidad
        else:
            raise ValueError("Tipo de dato no permitido, ingrese un entero no negativo")
        

    # Metodos get
    def getNombre(self): 
        return self.__nombre
    def getPrecio(self): 
        return self.__precio
    def getCantidad(self): 
        return self.__cantidad
    

    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "nombre": self.getNombre(),
            "precio": self.getPrecio(),
            "cantidad": self.getCantidad()
        }


class Electronico(Producto):
    def __init__(self, nombre, precio, cantidad, garantia):
        super().__init__(nombre, precio, cantidad)
        self.setGarantia(garantia)

    # Métodos set
    def setGarantia(self, nuevaGarantia):
        if isinstance(nuevaGarantia, int) and nuevaGarantia > 0:
            self.__garantia = nuevaGarantia
        else:
            raise ValueError("La garantía debe ser un número entero positivo")

    # Métodos get
    def getGarantia(self):
        return self.__garantia


    def to_dict(self):
        d = super().to_dict()
        d["garantia"] = self.getGarantia()
        return d

class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.setTalla(talla)

    # Métodos set
    def setTalla(self, nuevaTalla):
        if isinstance(nuevaTalla, str) and nuevaTalla.strip():
            self.__talla = nuevaTalla
        else:
            raise ValueError("La talla debe ser una cadena no vacía")

    # Métodos get
    def getTalla(self):
        return self.__talla


    def to_dict(self):
        d = super().to_dict()
        d["talla"] = self.getTalla()
        return d


class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, caducidad):
        super().__init__(nombre, precio, cantidad)
        self.setCaducidad(caducidad)

    # Métodos set
    def setCaducidad(self, nuevaCaducidad):
        if isinstance(nuevaCaducidad, str) and nuevaCaducidad.strip():
            self.__caducidad = nuevaCaducidad
        else:
            raise ValueError("La caducidad debe ser una cadena no vacía")

    # Métodos get
    def getCaducidad(self):
        return self.__caducidad


    def to_dict(self):
        d = super().to_dict()
        d["caducidad"] = self.getCaducidad()
        return d