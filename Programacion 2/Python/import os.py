#Python

''' 1) Area de un trapecio (procedimiento sin parametros)'''

def area_t():
    b1=int(input("\nIngrese la base superior: "))
    b2=int(input("Ingrese la base inferior: "))
    h=int(input("Ingrese la altura: "))
    a=((b1+b2)*h)/2
    print("El area del trapecio es %f\n"%(a))

#-------------------------------------------

''' 2) Euros a cop y a dolares (procedimiento con parametros)'''

def cambio (eu):
    cop=4432.76*eu
    dol=(4432.76*eu)/4463.33
    print("%f euros equivalen a %f pesos colombianos y a %f dolares\n"%(eu,cop,dol))

#---------------------------------------------

''' 3) Dias a horas (funcion sin parametros)'''

def tiempo ():
    d=int(input("\nIngrese la cantidad de dias: "))
    h=d*24
    return h

#---------------------------------------------

''' 4) Metros a pulgadas (funcion con parametros)'''

def medida (m):
    pulg=m*39.27
    return pulg

#------------------------------------------

def menu():
    print("\nIngrese 1 para calcular el area de un trapecio")
    print("Ingrese 2 para convertir euros a pesos colombianos y dolares")
    print("Ingrese 3 para averiguar las horas de varios dias")
    print("Ingrese 4 para calcular metros en pulgadas")
    print("Ingrese 5 para salir")
    op=int(input("Ingrese la opcion que desea: "))

    if (op==1):
        area_t()
        input("Presione enter para continuar...")
        menu()
    elif (op==2):
        eu=float(input("Ingrese el valor en euros: "))
        cambio (eu)
        input("Presione enter para continuar...")
        menu()
    elif (op==3):
        x=tiempo()
        print("El tiempo son %d horas\n"%(x))
        input("Presione enter para continuar...")
        menu()
    elif (op==4):
        m=float(input("Ingrese la medida en metros: "))
        x=medida(m)
        print("%f metros equivalen a %f pulgadas\n"%(m,x))
        input("Presione enter para continuar...")
        menu()

#----------------------------------

menu()