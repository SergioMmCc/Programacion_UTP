import math

# 1. Realice un programa para calcular diferentes áreas al menos 4 áreas de
#    figuras trigonométricas haciendo uso de clases y herencia se puede realizar
#    el modelamiento, deben encapsular todos los atributos y métodos, cuando
#    diseñen el set de cada atributo deben tener en cuenta dentro de este
#    método set que solo se deben ingresar números positivos.

# Figura 1: Rectangulo
class Rectangulo():
    def __init__(self, ancho, altura):
        self.setAncho(ancho)
        self.setAltura(altura)
    # Metodos set
    def setAncho(self, nuevoAncho):
        if isinstance(nuevoAncho, (int, float)) and nuevoAncho > 0:
            self.__ancho = nuevoAncho
        else:
            raise ValueError("Tipo de dato no permitido, ingrese un numero positivo")

    def setAltura(self, nuevaAltura):
        if isinstance(nuevaAltura, (int, float)) and nuevaAltura > 0:
            self.__altura = nuevaAltura
        else:
            raise ValueError("Tipo de dato no permitido, ingrese un numero positivo")

    # Metodos get
    def getAncho(self):
        return self.__ancho
    
    def getAltura(self):
        return self.__altura
    

    def calcularArea(self):
        return self.getAltura() * self.getAncho()
    

# Figura 2: Cuadrado
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        self.setLado(lado)

    # Metodos set
    def setLado(self, nuevoLado):
        if isinstance(nuevoLado, (int, float)) and nuevoLado > 0:
            self.setAncho(nuevoLado)
            self.setAltura(nuevoLado)
        else:
            raise ValueError("Tipo de dato no permitido, ingrese un numero positivo")
        
    # Metodos get
    def getLado(self):
        return self.getAncho()
    

    def calcularArea(self):
        return self.getLado() ** 2
    

# Figura 3: Circulo
class Circulo():
    def __init__(self, radio):
        self.setRadio(radio)

    # Metodos set
    def setRadio(self, nuevoRadio):
        if isinstance(nuevoRadio, (int, float)) and nuevoRadio > 0:
            self.__radio = nuevoRadio
        else:
            raise ValueError("Tipo de dato no permitido, ingrese un numero positivo")
        
    # Metodos get
    def getRadio(self):
        return self.__radio
    

    def calcularArea(self):
        return (self.getRadio() ** 2) * math.pi
    

# Figura 4: Triangulo
class Triangulo():
    def __init__(self, base, altura):
        self.setBase(base)
        self.setAltura(altura)

    # Metodos set
    def setBase(self, nuevoBase):
        if isinstance(nuevoBase, (int, float)) and nuevoBase > 0:
            self.__base = nuevoBase
        else:
            raise ValueError("Tipo de dato no permitido, ingrese un numero positivo")
        
    def setAltura(self, nuevaAltura):
        if isinstance(nuevaAltura, (int, float)) and nuevaAltura > 0:
            self.__altura = nuevaAltura
        else:
            raise ValueError("Tipo de dato no permitido, ingrese un numero positivo")
        
    # Metodos get
    def getBase(self):
        return self.__base
    
    def getAltura(self):
        return self.__altura
    

    def calcularArea(self):
        return self.getBase() * self.getAltura() / 2.0
    


# Menu
def mostrar_menu():
    print("\n=== Calculadora de Áreas ===")
    print("1. Rectángulo")
    print("2. Cuadrado")
    print("3. Círculo")
    print("4. Triángulo")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ")

    try:
        if opcion == "1":
            ancho = float(input("Ingrese el ancho: "))
            altura = float(input("Ingrese la altura: "))
            rect = Rectangulo(ancho, altura)
            print("Área del rectángulo:", rect.calcularArea())

        elif opcion == "2":
            lado = float(input("Ingrese el lado: "))
            cuad = Cuadrado(lado)
            print("Área del cuadrado:", cuad.calcularArea())

        elif opcion == "3":
            radio = float(input("Ingrese el radio: "))
            circ = Circulo(radio)
            print("Área del círculo:", circ.calcularArea())

        elif opcion == "4":
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            tri = Triangulo(base, altura)
            print("Área del triángulo:", tri.calcularArea())

        elif opcion == "5":
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

        input("\nPresione Enter para continuar...") # Esperar a que el usuario presione Enter

    except ValueError as e:
        print("Error:", e)
