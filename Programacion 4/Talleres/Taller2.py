from io import *
archivo = open(r"/home/sergio/Desktop/Programacion/Programacion_UTP/Programacion 4/Talleres/archivo.txt", "a")

# Primer punto
# Realice un programa que reciba en una lista solo números enteros de dos
# cifras, luego de llenar la lista, recorra cada elemento sumando el digito uno
# con el digito dos. La lista puede ser de la longitud que el usuario ingrese.
def primero():
    n = int(input("Ingrese la longitud de la lista: "))
    lista = []
    ans = []
    for i in range (0, n):
        num = int(input("Ingrese un número: "))
        lista.append(num)
    
    for num in lista:
        suma = num // 10 + num % 10
        ans.append(suma)

    for suma in ans:
        print(f"{suma} ", end = "")
        archivo.write(f"{suma} ")
    print()
    archivo.write("\n")


# Segundo punto
# Realice un programa que recorra una lista llena de los objetos usuario que
# quieran, luego van a contar la cantidad que un usuario aparezca en la lista y
# luego debe decir si aparece una cantidad par o impar de veces.
# Al diseñar las clases usted debe considerar los atributos que crea
# necesarios.
class Usuario:
    def __init__(self, nombre=""):
        self.nombre = nombre

    def ingresar_datos(self):
        self.nombre = input("Ingrese el nombre: ")

    def __eq__(self, other):
        return isinstance(other, Usuario) and self.nombre == other.nombre

def segundo():
    usuarios = int(input("Ingrese la cantidad de usuarios que desea agregar: "))
    listaUsuarios = []
    for _ in range(usuarios):
        nuevoUsuario = Usuario()
        nuevoUsuario.ingresar_datos()
        listaUsuarios.append(nuevoUsuario)
    
    buscar = Usuario(input("\nIngrese el usuario que desea buscar: "))
    cantidad = listaUsuarios.count(buscar)
    
    print(f"El usuario {buscar.nombre} aparece {cantidad} veces en la lista, ", end = "")
    archivo.write(f"El usuario {buscar.nombre} aparece {cantidad} veces en la lista, ")
    if cantidad % 2:
        print(f"la cantidad es impar")
        archivo.write(f"la cantidad es impar\n")
    else:
        print(f"la cantidad es par")
        archivo.write(f"la cantidad es par\n")


# Tercer punto
# Realice un método que ordene una lista de mínimo 15 cadenas empezando
# por todas las cadenas pares y luego las impares.
# Recuerden que definimos si una cadena es par o impar por la cantidad de
# caracteres que tenga, por ejemplo:
# “hola” es una cadena par por que se compone de 4 caracteres y “oso” sería
# una cadena impar porque tiene tres caracteres.
# Si las cadenas tienen la misma cantidad de caracteres no importa cuál va
# de primera.
def ordenar(lista):
    lista = sorted(lista, key=lambda x: (len(x) % 2, len(x)))
    return lista

def tercero():
    lista = ["agua", "oso", "hola", "fuego", "juego", "murcielago", "esternocleidomastoideo", 
             "parangaricutirimicuaro", "aguacero", "meci", "fubol", "aaa", "siuu", "x", "chao"]
    lista = ordenar(lista)
    for elemento in lista:
        print(f"{elemento} ", end = "")
        archivo.write(f"{elemento} ")
    print()
    archivo.write("\n")


# Cuarto punto
# Diseñe las siguientes entidades con al menos 5 atributos y al
# menos dos métodos:
# a. Libro
# b. Casa
# c. Película
# d. Bodega
# e. Lámpara
# f. Modem
# g. Router
# h. Maletín
# i. Paciente Oncológico
# j. Gato

class Libro:
    def __init__(self):
        self.nombre = ""
        self.autor = ""
        self.anioPublicacion = 0
        self.editorial = ""
        self.genero = ""

    def ingresarDatos(self):
        self.nombre = input("Ingrese el nombre del libro: ")
        self.autor = input(f"Ingrese el autor de {self.nombre}: ")
        self.anioPublicacion = int(input(f"Ingrese el año en que fue publicado {self.nombre}: "))
        self.editorial = input(f"Ingrese la editorial de {self.nombre}: ")
        self.genero = input(f"Ingrese el género de {self.nombre}: ")

    def mostrar(self):
        mensaje = f"{self.nombre} es un libro de {self.genero}, escrito por {self.autor} y publicado en {self.anioPublicacion}. Su editorial es {self.editorial}."
        print(mensaje)
        archivo.write(mensaje + "\n")
        

class Casa:
    def __init__(self):
        self.ancho = 0.0
        self.largo = 0.0
        self.pisos = 0
        self.direccion = ""
        self.dueno = ""

    def ingresarDatos(self):
        self.ancho = float(input("Ingrese el ancho de la casa: "))
        self.largo = float(input("Ingrese el largo de la casa: "))
        self.pisos = int(input("Ingrese la cantidad de pisos de la casa: "))
        self.direccion = input("Ingrese la dirección de la casa: ")
        self.dueno = input("Ingrese el dueño de la casa: ")

    def mostrar(self):
        mensaje = f"La casa esta ubicada en {self.direccion}, es propiedad de {self.dueno}, tiene {self.pisos} pisos y sus dimensiones son {self.ancho}x{self.largo} metros."
        print(mensaje)
        archivo.write(mensaje + "\n")


class Pelicula:
    def __init__(self):
        self.nombre = ""
        self.genero = ""
        self.anioLanzamiento = 0
        self.director = ""
        self.estudio = ""

    def ingresarDatos(self):
        self.nombre = input("Ingrese el nombre de la película: ")
        self.genero = input(f"Ingrese el género de {self.nombre}: ")
        self.anioLanzamiento = int(input(f"Ingrese el año de lanzamiento de {self.nombre}: "))
        self.director = input(f"Ingrese el director de {self.nombre}: ")
        self.estudio = input(f"Ingrese el estudio de {self.nombre}: ")

    def mostrar(self):
        mensaje = f"{self.nombre} es una película de {self.genero}, dirigida por {self.director} y lanzada en {self.anioLanzamiento} por el estudio {self.estudio}."
        print(mensaje)
        archivo.write(mensaje + "\n")


class Bodega:
    def __init__(self):
        self.largo = 0.0
        self.ancho = 0.0
        self.alto = 0.0
        self.volumen = 0.0
        self.direccion = ""

    def ingresarDatos(self):
        self.largo = float(input("Ingrese el largo de la bodega: "))
        self.ancho = float(input("Ingrese el ancho de la bodega: "))
        self.alto = float(input("Ingrese el alto de la bodega: "))
        self.direccion = input("Ingrese la dirección de la bodega: ")
        self.volumen = self.largo * self.ancho * self.alto

    def mostrar(self):
        mensaje = f"La bodega esta ubicada en {self.direccion}. Tiene un volumen de {self.volumen} metros cúbicos."
        print(mensaje)
        archivo.write(mensaje + "\n")


class Lampara:
    def __init__(self):
        self.tipo = ""
        self.potencia = 0.0
        self.color = ""
        self.marca = ""
        self.estado = ""

    def ingresarDatos(self):
        self.tipo = input("Ingrese el tipo de lámpara: ")
        self.potencia = float(input("Ingrese la potencia de la lámpara: "))
        self.color = input("Ingrese el color de la lámpara: ")
        self.marca = input("Ingrese la marca de la lámpara: ")
        self.estado = input("Ingrese el estado de la lámpara: ")

    def mostrar(self):
        mensaje = f"La lámpara es de tipo {self.tipo}, de la marca {self.marca}, tiene una potencia de {self.potencia} watts y es de color {self.color}. Actualmente se encuentra {self.estado}."
        print(mensaje)
        archivo.write(mensaje + "\n")


class Modem:
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.velocidad = 0
        self.estado = ""
        self.puertos = 0

    def ingresarDatos(self):
        self.marca = input("Ingrese la marca del modem: ")
        self.modelo = input("Ingrese el modelo del modem: ")
        self.velocidad = int(input("Ingrese la velocidad del modem: "))
        self.estado = input("Ingrese el estado del modem: ")
        self.puertos = int(input("Ingrese la cantidad de puertos del modem: "))

    def mostrar(self):
        mensaje = f"El modem es marca {self.marca} modelo {self.modelo}, tiene una velocidad de {self.velocidad} Mbps y cuenta con {self.puertos} puertos. Actualmente se encuentra {self.estado}."
        print(mensaje)
        archivo.write(mensaje + "\n")


class Router:
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.frecuencia = 0.0
        self.antenas = 0
        self.seguridad = ""

    def ingresarDatos(self):
        self.marca = input("Ingrese la marca del router: ")
        self.modelo = input("Ingrese el modelo del router: ")
        self.frecuencia = float(input("Ingrese la frecuencia del router (en GHz): "))
        self.antenas = int(input("Ingrese la cantidad de antenas del router: "))
        self.seguridad = input("Ingrese el tipo de seguridad del router: ")

    def mostrar(self):
        mensaje = f"El router es marca {self.marca}, modelo {self.modelo} opera a una frecuencia de {self.frecuencia} GHz, tiene {self.antenas} antenas y utiliza seguridad {self.seguridad}."
        print(mensaje)
        archivo.write(mensaje + "\n")


class Maletin:
    def __init__(self):
        self.ancho = 0.0
        self.largo = 0.0
        self.alto = 0.0
        self.material = ""
        self.color = ""

    def ingresarDatos(self):
        self.ancho = float(input("Ingrese el ancho del maletín: "))
        self.largo = float(input("Ingrese el largo del maletín: "))
        self.alto = float(input("Ingrese el alto del maletín: "))
        self.material = input("Ingrese el material del maletín: ")
        self.color = input("Ingrese el color del maletín: ")

    def mostrar(self):
        mensaje = f"El maletín es de color {self.color} y material {self.material}. Tiene dimensiones {self.ancho}x{self.largo}x{self.alto} cm."
        print(mensaje)
        archivo.write(mensaje + "\n")


class PacienteOncologico:
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.diagnostico = ""
        self.tratamiento = ""
        self.estado = ""

    def ingresarDatos(self):
        self.nombre = input("Ingrese el nombre del paciente: ")
        self.edad = int(input("Ingrese la edad del paciente: "))
        self.diagnostico = input("Ingrese el diagnóstico del paciente: ")
        self.tratamiento = input("Ingrese el tratamiento del paciente: ")
        self.estado = input("Ingrese el estado del paciente: ")

    def mostrar(self):
        mensaje = f"El paciente {self.nombre} de {self.edad} años tiene un diagnóstico de {self.diagnostico}. Actualmente se encuentra {self.estado} y su tratamiento es {self.tratamiento}."
        print(mensaje)
        archivo.write(mensaje + "\n")


class Gato:
    def __init__(self):
        self.nombre = ""
        self.raza = ""
        self.edad = 0
        self.color = ""
        self.peso = 0.0

    def ingresarDatos(self):
        self.nombre = input("Ingrese el nombre del gato: ")
        self.raza = input("Ingrese la raza del gato: ")
        self.edad = int(input("Ingrese la edad del gato: "))
        self.color = input("Ingrese el color del gato: ")
        self.peso = float(input("Ingrese el peso del gato: "))

    def mostrar(self):
        mensaje = f"{self.nombre} es un gato de raza {self.raza}, de color {self.color}, tiene {self.edad} años y pesa {self.peso} kg."
        print(mensaje)
        archivo.write(mensaje + "\n")


# primero()
# segundo()
# tercero()
archivo.close()