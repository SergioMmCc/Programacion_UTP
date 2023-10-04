#Phyton

import os

def clean ():
    os.system("cls")

''' 1) Hacer un procedimiento que muestre por pantalla
n veces el mensaje de texto “hola”. '''

def hola (n):
    if (n>0):
        print("Hola")
        hola (n-1)

#-------------------------------------------------------

''' 2) Hacer un procedimiento que escriba los primeros
N números enteros. '''

def numeros (n, aux):
    if (aux<=n):
        print("%d"%(aux))
        numeros (n, aux+1)

#-------------------------------------------------------

''' 3) Hacer un procedimiento que muestre la tabla de
multiplicar de un número N. '''

def tabla (n, aux):
    if (aux<=10):
        r=n*aux
        print("%d * %d = %d"%(n, aux, r))
        tabla (n, aux+1)

#-------------------------------------------------------

''' 4) Hacer un procedimiento que imprima las tablas
de multiplicar desde 1 hasta N. '''

def tablas (n, aux, aux2):
    if (aux2<=n):
        if (aux<=10):
            r=aux2*aux
            print("%d * %d = %d"%(aux2, aux, r))
            tablas (n, aux+1, aux2)
        else:
            tablas (n, aux-10, aux2+1)

#-------------------------------------------------------

''' 5) Hacer una funcion que devuelva la sumatoria
para los numeros enteros hasta N. '''

def sumatoria (n):
    if (n<1):
        return 0
    r=n+sumatoria(n-1)
    return r

#-------------------------------------------------------

''' 6) Hacer una funcion que devuelva el factorial
de un numero x. '''

def factorial (n):
    if (n<=1):
        return 1
    r=n*factorial(n-1)
    return r

#-------------------------------------------------------

''' 7) Hacer una funcion que devuelva la sumatoria
de los numeros dados por la expresion x^x. Para todos
los numeros entre 1 y n. '''

def sumax (n):
    if (n<1):
        return 0
    r=(n**n)+sumax(n-1)
    return r

#-------------------------------------------------------

''' 8) Implementar una funcion que eleve un numero x
a la y (siendo y un entero positivo). '''

def potencia (x, y):
    if (y<1):
        return 1
    r=x*potencia(x, y-1)
    return r

#-------------------------------------------------------

''' 9) Hacer un procedimiento que muestre por pantalla
los submúltiplos de x (entero positivo). '''

def multiplos (x, aux):
    if (aux<=x):
        if (x%aux==0):
            print("%d"%(aux))
        multiplos (x, aux+1)

#-------------------------------------------------------

''' 10) Hacer una función booleana que indique si un
número es primo o no. '''

def primo (n, aux):
    if (aux<n):
        if (n%aux==0):
            return False
        else:
            return primo (n, aux+1)
    else:
        return True
    
#-------------------------------------------------------
    
''' 11) Hacer una función que devuelva el n-ésimo
número de la serie de Fibonacci. '''

def fibonacci1 (n, cont, aux, aux2):
    if (cont==n):
        return aux
    else:
        return fibonacci1 (n, cont+1, aux2, aux+aux2)

#-------------------------------------------------------

''' 12) Hacer un procedimiento que muestre por
pantalla los n primeros números de la serie de
fibonacci. '''

def fibonacci2 (n, cont, aux, aux2):
    if cont<=n:
        print ("%d"%aux)
        fibonacci2 (n, cont+1, aux2, aux+aux2)

#-------------------------------------------------------

''' 13) Hacer una función que encuentre y devuelva
el mínimo común múltiplo de dos números a y b
(enteros positivos). '''

def mcm (a, b, aux):
    if ((aux%a==0) and (aux%b==0)):
        return aux
    else:
        return mcm(a, b, aux+1)
    
#-------------------------------------------------------

''' 14) Hacer una función que encuentre y retorne el
máximo común divisor entre dos números a y b
(enteros positivos). '''

def mcd (a, b, aux, cont):
    if (cont==1):
        return mcd (a, b, aux+a, cont+1)
    else:
        if ((a%aux==0) and (b%aux==0)):
            return aux
        else:
            return mcd (a, b, aux-1, cont)

#-------------------------------------------------------

def menu ():
    clean ()
    print("Ingrese 1 para imprimir n veces hola")
    print("Ingrese 2 para imprimir los numeros hasta n")
    print("Ingrese 3 para averiguar la tabla de multiplicar de n")
    print("Ingrese 4 para averiguar las tablas de multiplicar hasta n")
    print("Ingrese 5 para la sumanoria de 1 hasta n")
    print("Ingrese 6 para averiguar el factorial de un numero")
    print("Ingrese 7 para sumatoria de x^x")
    print("Ingrese 8 para potencia de un numero")
    print("Ingrese 9 para averiguar los multiplos de un numero")
    print("Ingrese 10 para averiguar si un numero es primo")
    print("Ingrese 11 para averiguar el n-esimo termino de fibonacci")
    print("Ingrese 12 para ver los primeros n terminos de fibonacci")
    print("Ingrese 13 para averiguar el minimo comun multiplo de dos numeros")
    print("Ingrese 14 para averiguar el maximo comun divisor de dos numeros")
    op=int(input("Ingrese la opcion que desea (1-14): "))

    if (op==1):
        n=int(input("Ingrese el numero de veces que desea imprimir hola: "))
        hola (n)
        input("Presione enter para continuar...")
        menu ()
    if (op==2):
        n=int(input("Ingrese el numero hasta el que desea imprimir: "))
        numeros (n, 1)
        input("Presione enter para continuar...")
        menu()
    if (op==3):
        n=int(input("Ingrese el numero cuya tabla de multiplicar desea averiguar: "))
        tabla (n, 1)
        input("Presione enter para continuar...")
        menu()
    if (op==4):
        n=int(input("Ingrese el numero hasta el que desea conocer las tablas de multiplicar: "))
        tablas (n, 1, 1)
        input("Presione enter para continuar...")
        menu()
    if (op==5):
        n=int(input("Ingrese el numero hasta el que desea calcular la sumatoria: "))
        r=sumatoria(n)
        print("El resultado de la sumatoria de 1 hasta %d es %d"%(n, r))
        input("Presione enter para continuar...")
        menu ()
    if (op==6):
        n=int(input("Ingrese el numero cuyo factorial desea conocer: "))
        r=factorial (n)
        print("El factorial de %d es %d"%(n, r))
        input ("Presione enter para comtinuar...")
        menu()
    if (op==7):
        n=int(input("Ingrese el numero hasta el que desea calular la sumatoria: "))
        r=sumax (n)
        print("El resultado de la sumatoria hasta el termino %d es %d"%(n, r))
        input("Presione enter para continuar...")
        menu ()
    if (op==8):
        x=int(input("Ingrese la base: "))
        y=int(input("Ingrese el exponente: "))
        r=potencia (x, y)
        print("%d ^ %d = %d"%(x, y, r))
        input("Presione enter para continuar...")
        menu ()
    if (op==9):
        x=int(input("Ingrese el numero cuyos multiplos desea averiguar: "))
        multiplos (x, 1)
        input("Presione eneter para continuar...")
        menu ()
    if (op==10):
        n = int(input("Ingrese el número que desea averiguar si es primo: "))
        r = primo(n, 2)
        if r == True:
            print("%d es un número primo" % n)
        else:
            print("%d no es un número primo" % n)
        input("Presione enter para continuar...")
        menu()
    if (op==11):
        n=int(input("Ingrese el termino de fibonacci que desea averiguar: "))
        r=fibonacci1(n, 1, 0, 1)
        print("El termino %d de fibonacci es %d"%(n, r))
        input("Presione enter para continuar...")
        menu()
    if (op==12):
        n=int(input("Ingrese el termino hasta el que desea averiguar fibonacci: "))
        fibonacci2 (n, 1, 0, 1)
        input("Presione enter para continuar...")
        menu ()
    if (op==13):
        a=int(input("Ingrese el primer numero: "))
        b=int(input("Ingrese el segundo numero: "))
        r=mcm(a, b, 1)
        print("El minimo comun multiplo de %d y %d es %d"%(a, b, r))
        input("Presione enter para continuar...")
        menu()
    if (op==14):
        a=int(input("Ingrese el primer numero: "))
        b=int(input("Ingrese el segundo numero: "))
        r=mcd(a, b, 0, 1)
        print("El maximo comun divisor de %d y %d es %d"%(a, b, r))
        input("Presione enter para continuar...")
        menu()

#-------------------------------------------------------

menu ()