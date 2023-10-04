#Phyton

import os

def clean ():
    os.system("cls")

''' 1) Hacer un procedimiento que muestre por pantalla
n veces el mensaje de texto “hola”. '''

def hola (n):
    if (n>0):
        print("Hola\n")
        hola (n-1)

#-------------------------------------------------------

def menu ():
    print("Ingrese 1 para imprimir n veces hola")
    op=int(input("Ingrese la opcion que desea (1-15): "))

if (op==1):
    n=int(input("Ingrese el numero de veces que desea imprimir hola: "))
    hola (n)
    input("Presione enter para continuar...")
    menu ()

#-------------------------------------------------------

menu ()