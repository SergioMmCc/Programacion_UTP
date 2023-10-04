#Python
#Taller ciclos - While

''' 1)  Implementar un algoritmo que muestre todos los multiplos
de 7 comprendidos entre 1 y 1000. '''

def multiplos ():
    for i in range (1,1001):
        if (i%7==0):
            print(i)

#----------------------------------------------------

''' 2) Implementar un algoritmo que calcule la siguiente suma:
3(1)+3(2)+3(3)+3(4)+...+3(n), ingresar n por teclado mostrar el
resultado de dicha suma. '''

def suma (n):
    r=0
    for i in range (1, n+1):
        r=r+(3*i)
    return r

#----------------------------------------------------

''' 3)  Leer por teclado cuatro notas de un estudiante en una
sola variable, cada vez el acumulado se debe guardar en una
variable llamada total. Cuando se lean las cuatro determinar
el promedio, si el promedio es mayor o igual a tres, imprimir
ganaste de lo contrario imprimir perdiste.'''

def notas ():
    r=0
    for i in range (1, 5):
        nota=float(input("Ingrese la nota: "))
        r=r+nota
    if (r/4>=3.0):
        print("Ganaste")
    else:
        print("Perdiste")

#----------------------------------------------------

''' 4) Un entero positivo n se llama perfecto si n es igual a
la suma de todos sus divisores diferentes de el. Por ejemplo,
6 es perfecto porque 6 = 1 + 2 + 3. Escriba un programa que lea
por teclado un numero entero positivo, y nos indique si este es
perfecto o no. Ademas, el programa debe imprimir todos los
divisores del numero. '''

def perfecto (n):
    i=1
    r=0
    print("Los divisores de %d son:"%(n))
    while (i<n):
        if (n%i==0):
            r=r+i
            print(i)
        i+=1
    if (r==n):
        print("%d es un numero perfecto"%(n))
    else:
        print("%d no es un numero perfecto"%(n))

#----------------------------------------------------

''' 5) Leer dos numeros enteros por teclado y determinar si
estos son numeros amigos (Dos numeros amigos son dos enteros
positivos a y b tales que a es la suma de los divisores propios
de b, y b es la suma de los divisores propios de a. la unidad 
e considera divisor propio, pero no lo es el mismo numero). '''

def amigos (a, b):
    i1=1
    i2=1
    r1=0
    r2=0
    while (i1<a):
        if (a%i1==0):
            r1=r1+i1
        i1+=1
    while (i2<b):
        if (b%i2==0):
            r2=r2+i2
        i2+=1
    if (a==r2 and b==r1):
        print ("%d y %d son numeros amigos"%(a,b))
    else:
        print ("%d y %d no son numeros amigos"%(a,b))

#----------------------------------------------------

''' 6) Leer un numero entero positivo n por teclado y mostrar
por pantalla la secuencia de fibonacci con n terminos.(ejemplo:
si se lee un 3 se debe mostrar la serie hasta el tercer numero
1,1,2. Si se lee un 5, se debe mostrar la serie hasta el quinto
numero 1,1,2,3,5). '''

def fibonacci (n):
    i1=1
    i2=1
    aux=0
    cont=1
    while (cont<=n):
        print(i1)
        aux=i1
        i1=i2
        i2=i2+aux
        cont+=1

#----------------------------------------------------

''' 7) Leer un entero n por teclado y calcular su factorial,
n!=1*2*3*4*....*n. '''

def factorial (n):
    i=1
    r=1
    while (i<=n):
        r=r*i
        i+=1
    print (r)

#----------------------------------------------------

''' 8) Implementar un algoritmo que diga cuantos numeros
perfectos hay entre 1 y 10000. '''

def perfectos ():
    n=1
    cont=0
    while (n<=10000):
        i=1
        r=0
        while (i<n):
            if (n%i==0):
                r=r+i
            i+=1
        if (n==r):
            cont+=1
        n+=1
    print ("Entre 1 y 10000 hay %d numeros perfectos"%(cont))

#----------------------------------------------------

''' 9) Implementar un algoritmo que diga cuales numeros
primos hay entre 1 y 1000 (debe mostrar los numeros). '''

def primos ():
    n=2
    while (n<=1000):
        i=2
        cont=0
        while (i<n):
            if (n%i==0):
                cont+=1
            i+=1
        if (cont==0):
            print(n)
        n+=1

#----------------------------------------------------

''' 10) Hacer un programa que muestre los factoriales
de los primeros 10 enteros '''

def factoriales ():
    n=1
    while (n<=10):
        i=1
        r=1
        while (i<=n):
            r=r*i
            i+=1
        print ("Factorial de %d: %d"%(n, r))
        n+=1

#----------------------------------------------------

''' 11) Implementar las tablas de multiplicar del 10 al 20. '''

def tablas ():
    n=10
    while (n<=20):
        i=1
        while (i<=10):
            r=n*i
            print ("%d * %d = %d"%(n,i,r))
            i+=1
        n+=1

#----------------------------------------------------

#multiplos ()
''' n=int(input("Ingrese el numero hasta el que desea calcular la sumatoria: "))
r=suma(n)
print("El resultado de la sumatoria hasta el termino %d es %d"%(n,r)) '''
notas ()
#perfecto (6)
#amigos (220, 284)
#fibonacci (6)
#factorial (7)
#perfectos ()
#primos ()
#factoriales ()
#tablas ()