# 2. Desarrolle un sistema para gestionar las reservas de habitaciones en un hotel. El hotel
#    tiene diferentes tipos de habitaciones: Habitación Simple, Habitación Doble y Suite. Todas
#    las habitaciones tienen un número, un precio y un estado (disponible o reservado). Las
#    habitaciones dobles y las suites permiten agregar servicios adicionales, como desayuno o
#    spa.
#    Requerimientos:
#    a. Crear una clase base Habitación con atributos encapsulados (numero, precio,
#       estado).
#    b. Crear las clases derivadas HabitacionSimple, HabitacionDoble y Suite, con la
#       posibilidad de agregar servicios adicionales en HabitacionDoble y Suite.
#    c. Crear un sistema para reservar habitaciones, donde el número de la habitación
#       sea la clave y el valor sea el objeto Habitación.
#    d. Implementar funciones para mostrar todas las habitaciones disponibles, reservar
#       una habitación y calcular el precio total con servicios incluidos en las habitaciones
#       dobles y suites.


import os
from funcionesUsuario import *

################################ MENU ####################################
def menu():
    cargar()

    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 32)
    print("  Bienvenido al Hotel del Café  ")
    print("=" * 32)


    while True:
        print("Menú:")
        print("1. Consultar habitaciones disponibles")
        print("2. Reservar")
        print("3. Salir")

        op = input("Elija la opción que desee: ")

        if op == "1":
            mostrarDisponibles()

        elif op == "2":
            try:
                numeroHabitacion = int(input("Ingrese el número de la habitación que desea reservar: "))
                if numeroHabitacion < 1:
                    print("Debe ingresar un número positivo")
                else:
                    print(reservar(numeroHabitacion))
            except ValueError:
                print("Debe ingresar un número válido")

        elif op == "3":
            if guardar():
                print("Datos guardados correctamente")
            print("Gracias por visitarnos")
            break

        else:
            print("La opción que ingreso no es válida")

        input("\nPresione enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

menu()