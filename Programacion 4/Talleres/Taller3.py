# Sergio Moncada Muñoz 1089380570
# Programación IV - Taller 3


import math

# 1. Diseñe las siguientes entidades con al menos 4 atributos y al
# menos dos métodos:
# a. Avión
# b. Celular
# c. Asignatura
# d. Ejercito
# e. Silla
# f. Audífonos

class Avion:
    def __init__(self, modelo, capacidad, velocidad, enVuelo):
        self.modelo = modelo
        self.capacidad = capacidad
        self.velocidad = velocidad
        self.enVuelo = enVuelo

    def despegar(self):
        self.enVuelo = True
        print("El avión ha despegado")
    
    def aterrizar(self):
        self.enVuelo = False
        print("El avión ha aterrizado")


class Celular:
    def __init__(self, marca, modelo, color, precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio

    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}\nPrecio: {self.precio}"
    
    def llamar(self, numero):
        print(f"Llamando al número {numero}")


class Asignatura:
    def __init__(self, nombre, creditos, docente, horario):
        self.nombre = nombre
        self.creditos = creditos
        self.docente = docente
        self.horario = horario

    def __str__(self):
        return f"Asignatura: {self.nombre}\nCréditos: {self.creditos}\nDocente: {self.docente}\nHorario: {self.horario}"
    
    def cambiarDocente(self, nuevoDocente):
        self.docente = nuevoDocente
        print(f"El docente ha sido cambiado a {nuevoDocente}")


class Ejercito:
    def __init__(self, nombre, pais, cantidadSoldados, armamento):
        self.nombre = nombre
        self.pais = pais
        self.cantidadSoldados = cantidadSoldados
        self.armamento = armamento

    def __str__(self):
        return f"Ejército: {self.nombre}\nPaís: {self.pais}\nCantidad de soldados: {self.cantidadSoldados}\nArmamento: {self.armamento}"
    
    def muerenSoldados(self, cantidad):
        if cantidad > self.cantidadSoldados:
            print("No pudieron morir tantos soldados ya que no hay suficientes soldados en el ejército")
        else:
            self.cantidadSoldados -= cantidad
            print(f"Ha habido {cantidad} bajas en el ejército")


class Silla:
    def __init__(self, material, color, tipo, precio):
        self.material = material
        self.color = color
        self.tipo = tipo
        self.precio = precio

    def __str__(self):
        return f"Material: {self.material}\nColor: {self.color}\nTipo: {self.tipo}\nPrecio: {self.precio}"
    
    def cambiarColor(self, nuevoColor):
        self.color = nuevoColor
        print(f"El color ha sido cambiado a {nuevoColor}")


class Audifonos:
    def __init__(self, marca, modelo, color, precio, volumen):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
        self.volumen = volumen

    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}\nPrecio: {self.precio}"
    
    def cambiarVolumen(self, nuevoVolumen):
        self.volumen = nuevoVolumen
        print(f"Volumen cambiado a {nuevoVolumen}")


# 2. Diseñar una clase para crear un objeto rectángulo con sus
# respectivos atributos, un método que dibuje el rectángulo con “*”
# y otro método que realice alguna fórmula con los datos del
# rectángulo.

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def dibujar(self):
        for i in range(self.altura):
            print("*" * self.base)

    def area(self):
        return self.base * self.altura
    

# 3. Diseñar una clase para crear un objeto empleado con al menos 5
# atributos y los siguientes métodos:
#   a. Calcular lo que se gana al mes teniendo en cuenta el
#      número de horas que trabaja, el valor de cada hora.
#   b. Calcular el tiempo de antigüedad y cuanto le falta para
#      pensionarse teniendo en cuenta que las mujeres se
#      pensionan antes que los hombres.
#   c. Calcular cuánto paga por salud y pensión al mes el
#      empleado teniendo en cuenta que es 4% de salud y 4% de
#      pensión y al año cuanto abona en pensión.
#   d. Se deben guardar todos los datos de los empleados en un
#      archivo.

class Empleado:
    def __init__(self, nombre, apellido, genero, horasTrabajadas, valorHora):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.horasTrabajadas = horasTrabajadas
        self.valorHora = valorHora

    def salario(self):
        return self.horasTrabajadas * self.valorHora
    
    def antiguedad(self, edad):
        if self.genero == "Femenino":
            return 60 - edad
        else:
            return 65 - edad
        
    def pension(self):
        print(f"El empleado paga {self.salario() * 0.04} por salud y {self.salario() * 0.04} por pensión al mes")
        print(f"Al año abona {self.salario() * 0.04 * 12} en pensión")

    def guardarDatos(self):
        with open("empleados.txt", "a") as file:
            file.write(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nGénero: {self.genero}\nHoras trabajadas: {self.horasTrabajadas}\nValor hora: {self.valorHora}\n\n")


# 4. Diseñar una clase para un objeto calculadora científica con sus
# respectivos atributos y al menos 12 métodos.

class Calculadora:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b
    
    def multiplicacion(self, a, b):
        return a * b
    
    def division(self, a, b):
        if b == 0:
            return "No se puede dividir por cero"
        return a / b
    
    def potencia(self, a, b):
        return a ** b
    
    def raizCuadrada(self, a):
        if a < 0:
            return "No se puede calcular la raíz cuadrada de un número negativo"
        return a ** 0.5
    
    def seno(self, a):
        return math.sin(math.radians(a))
    
    def coseno(self, a):
        return math.cos(math.radians(a))
    
    def tangente(self, a):
        return math.tan(math.radians(a))
    
    def logaritmo(self, a):
        if a <= 0:
            return "No se puede calcular el logaritmo de un número menor o igual a cero"
        return math.log(a)
    
    def factorial(self, a):
        if a < 0:
            return "No se puede calcular el factorial de un número negativo"
        return math.factorial(a)
    
    def exponencial(self, a):
        return math.exp(a)
    

# 5. Para la siguiente lista:
# Lista =[1, 1991, "taller", 200, 3, "programación", 700, "utp", "POO"]
# Implemente uno o varios métodos para hacer:
#  La lista inicial debe quedar guardada en un archivo
#  A partir de la lista inicial se debe guardar en un archivo una
#   lista con los números enteros y en otro archivo guardar la
#   lista con las cadenas.
#  En un ultimo archivo vamos a guardar una lista donde se
#   reemplacen los números impares con la palabra:
#   “reemplazo”
#  Al final debe crear un método donde se imprima solo la
#   mitad de la lista.

class Listas:
    def __init__(self):
        self.lista = [1, 1991, "taller", 200, 3, "programación", 700, "utp", "POO"]

    def guardarLista(self):
        with open("lista.txt", "w") as file:
            for item in self.lista:
                file.write(f"{item}\n")
    
    def guardarEnteros(self):
        with open("enteros.txt", "w") as file:
            for item in self.lista:
                if type(item) == int:
                    file.write(f"{item}\n")
    
    def guardarCadenas(self):
        with open("cadenas.txt", "w") as file:
            for item in self.lista:
                if type(item) == str:
                    file.write(f"{item}\n")
    
    def reemplazarImpares(self):
        with open("reemplazo.txt", "w") as file:
            for item in self.lista:
                if type(item) == int and item % 2 != 0:
                    file.write("reemplazo\n")
                else:
                    file.write(f"{item}\n")
    
    def imprimirMitad(self):
        mitad = len(self.lista) // 2
        for i in range(mitad):
            print(self.lista[i])


# 6. Realice un ejemplo de cada método de archivos visto en clase.
# - Sentencia With
# - Método Seek
# - Método tell
# - Método readline
# - Método readlines
# - Método writelines


def sexto():
    # Sentencia With
    with open("archivo.txt", "w") as file:
        file.write("Hola mundo")

    # Método Seek
    with open("archivo.txt", "r") as file:
        print(file.read())
        file.seek(0)
        print(file.read())

    # Método tell
    with open("archivo.txt", "r") as file:
        print(file.tell())

    # Método readline
    with open("archivo.txt", "r") as file:
        print(file.readline())

    # Método readlines
    with open("archivo.txt", "r") as file:
        print(file.readlines())

    # Método writelines
    with open("archivo.txt", "w") as file:
        file.writelines(["Hola\n", "Mundo\n"])


# 7. Realice un menú para estructurar todos los puntos del taller.
def menu():
    while True:
        print("\nMenu:")
        print("1. Crear entidades")
        print("2. Crear rectángulo")
        print("3. Crear empleado")
        print("4. Crear calculadora científica")
        print("5. Operaciones con listas")
        print("6. Ejemplos de métodos de archivos")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            avion = Avion("Boeing 747", 416, 900, False)
            celular = Celular("Samsung", "Galaxy S21", "Negro", 799)
            asignatura = Asignatura("Matemáticas", 4, "Dr. Smith", "Lunes 10:00-12:00")
            ejercito = Ejercito("Fuerzas Armadas", "Colombia", 50000, "Rifles")
            silla = Silla("Madera", "Marrón", "Oficina", 150)
            audifonos = Audifonos("Sony", "WH-1000XM4", "Negro", 350, 50)
            print(avion)
            print(celular)
            print(asignatura)
            print(ejercito)
            print(silla)
            print(audifonos)
        
        elif opcion == "2":
            rectangulo = Rectangulo(5, 3)
            rectangulo.dibujar()
            print(f"Área del rectángulo: {rectangulo.area()}")
        
        elif opcion == "3":
            empleado = Empleado("Juan", "Pérez", "Masculino", 160, 10)
            print(f"Salario mensual: {empleado.salario()}")
            print(f"Años para pensionarse: {empleado.antiguedad(30)}")
            empleado.pension()
            empleado.guardarDatos()
        
        elif opcion == "4":
            calculadora = Calculadora("Casio", "FX-991ES")
            print(f"Suma: {calculadora.suma(5, 3)}")
            print(f"Resta: {calculadora.resta(5, 3)}")
            print(f"Multiplicación: {calculadora.multiplicacion(5, 3)}")
            print(f"División: {calculadora.division(5, 3)}")
            print(f"Potencia: {calculadora.potencia(5, 3)}")
            print(f"Raíz cuadrada: {calculadora.raizCuadrada(25)}")
            print(f"Seno: {calculadora.seno(math.pi/2)}")
            print(f"Coseno: {calculadora.coseno(math.pi/2)}")
            print(f"Tangente: {calculadora.tangente(math.pi/4)}")
            print(f"Logaritmo: {calculadora.logaritmo(10)}")
            print(f"Factorial: {calculadora.factorial(5)}")
            print(f"Exponencial: {calculadora.exponencial(2)}")
        
        elif opcion == "5":
            listas = Listas()
            listas.guardarLista()
            listas.guardarEnteros()
            listas.guardarCadenas()
            listas.reemplazarImpares()
            listas.imprimirMitad()
        
        elif opcion == "6":
            sexto()
        
        elif opcion == "7":
            break
        
        else:
            print("Opción no válida, intente de nuevo.")

menu()