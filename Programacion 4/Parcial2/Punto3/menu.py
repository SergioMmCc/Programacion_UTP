from funcionesUsuario import *
import os

# ------------------- MENÚ ----------------------
def menu():
    cargar_productos()

    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("\n1. Mostrar productos")
        print("2. Realizar pedido")
        print("3. Salir")
        op = input("Seleccione una opción: ")

        if op == "1":
            mostrar_productos()

        elif op == "2":
            nombre = input("Ingrese el nombre del producto: ")
            try:
                cantidad = int(input("Ingrese la cantidad a pedir: "))
                print(realizar_pedido(nombre, cantidad))
            except ValueError:
                print("Cantidad inválida.")

        elif op == "3":
            guardar_productos()
            print("Gracias por su compra.")
            break
        
        else:
            print("Opción inválida.")

        input("Presione enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

menu()