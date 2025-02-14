import random

# 1. Realice un algoritmo para sumar los valores numéricos de la
# siguiente lista sin ordenarla:

def primero():
    Lista = [2, 8, " hola", "programación", 10, "utp", 85, 82, 100, "mundo"]

    suma = 0
    for elemento in Lista:
        if isinstance(elemento, int):
            suma += elemento

    print(f"La suma total es: {suma}")

# 2. Dada la siguiente lista, Una todas las palabras de la lista en 
# una sola cadena separadas por espacio o algún carácter especial.
def segundo():
    palabras = ["Hola", "mundo", "esto", "es", "Python"]

    frase = ""
    for palabra in palabras:
        frase += palabra + " "

    print(frase)

# 3. Escribir un programa que almacene las asignaturas de un curso
# en una lista, pida al usuario las 4 notas de cada materia y en
# pantalla mostrar el promedio que ha sacado en cada materia y si
# alguna materia queda por debajo de la nota 3 debe salir en
# pantalla “asignatura perdida”, luego se deben calcular el
# promedio general de todas las materias si el promedio está por
# debajo de 3 debe imprimir “semestre perdido”, si esta entre 3 y 4
# debe imprimir “buen trabajo”, si el promedio esta entre 4 y 5
# debe imprimir “felicidades serás becado”.
def tercero():
    promedioSemestre = 0
    materias = []
    numeroMaterias = int(input("Ingrese el numero de materias: "))
    for indexMateria in range (numeroMaterias):
        materia = []
        nombreMateria = input(f"Ingrese el nombre de la materia {indexMateria + 1}: ")
        materia.append(nombreMateria)
        promedio = 0
        for indexNota in range (4):
            nota = float(input(f"Ingrese la nota {indexNota + 1}: "))
            promedio += nota
            materia.append(nota)
        promedio /= 4
        promedioSemestre += promedio
        materia.append(promedio)
        materias.append(materia)
        print()

    promedioSemestre /= numeroMaterias
    for materia in materias:
        print(materia[0], " - ", end = "")
        for indexNota in range (1, 4):
            print("nota", indexNota, ": ", materia[indexNota], ", ", end = "")
        print("nota4: ", materia[4])
        print("Promedio de ", materia[0], ": ", materia[5], end = "")
        print(" - asignatura perdida" if materia[5] < 3 else " - asignatura ganada")
        print()

    print(f"Promedio general: {promedioSemestre:.1f}", end = "")
    if promedioSemestre < 3:
        print(" - Semestre perdido")
    elif promedioSemestre <= 4:
        print(" - buen trabajo")
    else:
        print(" - felicidades serás becado")

# 4. Escriba un programa que pida al usuario la cantidad que desea
# de la lista, luego el usuario debe ingresar valores numéricos
# enteros hasta llenar la lista, luego de ingresarlos se debe
# imprimir en pantalla cada número ingresado por el usuario y al
# lado debe aparecer ese mismo número al cuadrado y al lado ese
# mismo número al cubo.
def cuarto():
    totalNumeros = int(input("Ingrese la cantidad que desea: "))
    numeros = []
    for indexNumero in range (totalNumeros):
        numero = int(input("Ingrese un numero: "))
        numeros.append(numero)
    
    for indexNumero in range (totalNumeros):
        numero = numeros[indexNumero]
        print(f"{numero} - {numero * numero} - {numero * numero * numero}")

# 5. Realice un programa que almacene una cantidad de cadenas
# dictaminadas por el usuario, en pantalla se debe mostrar la
# cadena que más caracteres contenga y la cadena que menos
# caracteres contenga.
def quinto():
    numeroCadenas = int(input("Ingrese el numero de cadenas que desea evaluar: "))
    primeraCadena = input("Ingrese una cadena: ")
    lenPrimeraCadena = len(primeraCadena)
    cadenaMayor = primeraCadena
    cadenaMenor = primeraCadena

    lenCadenaMayor = lenPrimeraCadena
    lenCadenaMenor = lenPrimeraCadena
    for indexCadena in range (numeroCadenas - 1):
        nuevaCadena = input("Ingrese una cadena: ")
        lenNuevaCadena = len(nuevaCadena)

        if lenNuevaCadena > lenCadenaMayor:
            cadenaMayor = nuevaCadena
            lenCadenaMayor = lenNuevaCadena
        if lenNuevaCadena < lenCadenaMenor:
            cadenaMenor = nuevaCadena
            lenCadenaMenor = lenNuevaCadena

    print(f"Cadena mayor = {cadenaMayor}")
    print(f"Cadena menor = {cadenaMenor}")

# 6. Realice un programa en el que el usuario ingrese un valor
# entero, luego debe mostrar en pantalla las cadenas cuya longitud
# sea igual al número ingresado
def sexto():
    Lista = ["oso", "casa2", "murciélago", "ventana", "programación", 
             "objetos", "listas", "métodos", "utp"]
    longitud = int(input("Ingrese la longitud de las palabras que quiera ver: "))
    print(f"Las palabras de longitud {longitud} son: ")
    for palabra in Lista:
        if len(palabra) == longitud:
            print(palabra)

# 7. Realizar un programa que pida al usuario un carácter, luego se
# debe mostrar las cadenas que contengan dicho carácter
def septimo():
    Lista = ["oso", "casa2", "murciélago", "ventana", "programación", 
             "objetos", "listas", "métodos", "utp"]
    caracter = input("Ingrese un caracter: ")
    palabrasConCaracter = []
    for palabra in Lista:
        if caracter in palabra:
            print(f"{palabra}", end = "")
            if len(palabra) % 2:
                print(" -> impar")
            else:
                print(" -> par")
    
# 8. Realizar un programa que haga conteo de todos los caracteres
# que no sean vocales en una lista de 10 cadenas.
def octavo():
    vocales = "aeiouAEIOU"
    cuenta = 0
    for indexCadena in range(1, 11):
        cadena = input(f"Ingrese la cadena {indexCadena}: ")
        for letra in cadena:
            if letra not in vocales:
                cuenta += 1
    
    print(f"La lista tiene {cuenta} caracteres que no son consonantes")

# 9. Realizar un programa que inicialice una lista con 15 valores
# aleatorios y posteriormente muestre en pantalla cada elemento
# de la lista junto con su cuadrado y su cubo.
def noveno():
    Lista = [random.randint(1, 100) for _ in range(15)]
    for numero in Lista:
        print(f"numero: {numero}, \t al cuadrado: {numero*numero}, \t al cubo: {numero*numero*numero}")

# 10. Elabore un programa para ingresar la siguiente lista.
# Lista= [“casa”, “programación”, “utp”, “universidad”, “utp, “casa”,
# “casa”,” thj”, “vbh”, “456”, “987”]
# a. Borre los elementos repetidos que tengamos en la lista
# b. Borre las cadenas que NO contengan vocales.
# c. Ordene la lista en orden alfabético respecto al primer
# elemento de la cadena.
def decimo():
    Lista= ["casa", "programación", "utp", "universidad", "utp", "casa",
            "casa", "thj", "vbh", "456", "987"]
    vocales = "aeiouAEIOU"

    sinRepetidos = set(Lista)
    listaAuxiliar = []
    for cadena in sinRepetidos:
        tieneVocales = 0
        for caracter in cadena:
            if caracter in vocales:
                tieneVocales = 1
        if not tieneVocales:
            listaAuxiliar.append(cadena)

    for cadena in listaAuxiliar:
        sinRepetidos.remove(cadena)
    
    listaOrdenada = list(sinRepetidos)
    listaOrdenada = sorted(listaOrdenada)

    print("Lista despues del proceso: ")
    for elemento in listaOrdenada:
        print(elemento)

# primero()
# segundo()
# tercero()
# cuarto()
# quinto()
# sexto()
# septimo()
# octavo()
# noveno()
decimo()