from objetos import *

# ===================== MENÚ =====================

def menu():
    cargar_todo()
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("\n🐾 Menú de Tienda de Mascotas 🐾")
        print("1. Agregar cliente")
        print("2. Agregar mascota")
        print("3. Mostrar clientes")
        print("4. Mostrar mascotas")
        print("5. Hacer adopción")
        print("6. Mostrar adopciones")
        print("7. Ejecutar métodos especiales")
        print("8. Guardar datos")
        print("9. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            agregar_mascota()
        elif opcion == "3":
            if len(clientes) == 0:
                print("No hay ningun cliente registrado")
            else:
                for c in clientes:
                    print(c.mostrar_info())
        elif opcion == "4":
            if len(animales) == 0:
                print("No hay ningun animal registrado")
            else:
                for a in animales:
                    print(a.mostrar_info())
        elif opcion == "5":
            hacer_adopcion()
        elif opcion == "6":
            if len(adopciones) == 0:
                print("No hay ninguna adopcion registrada")
            else:
                for a in adopciones:
                    print(a.resumen_adopcion())
        elif opcion == "7":
            ejecutar_metodos()
        elif opcion == "8":
            guardar_todo()
        elif opcion == "9":
            guardar_todo()
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")

        
        input("\nPresione Enter para continuar...") # Esperar a que el usuario presione Enter
        os.system('cls' if os.name == 'nt' else 'clear')


# Funciones adicionales

def agregar_cliente():
    tipo = input("¿Cliente frecuente (F) o VIP (V)?: ").upper()
    nombre = input("Nombre: ")
    cedula = input("Cédula: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")

    if tipo == "F":
        puntos = int(input("Puntos iniciales: "))
        cliente = ClienteFrecuente(nombre, cedula, direccion, telefono, correo, puntos)
    elif tipo == "V":
        descuento = float(input("Descuento (ej. 0.1 para 10%): "))
        cliente = ClienteVIP(nombre, cedula, direccion, telefono, correo, descuento)
    else:
        print("Tipo no válido.")
        return

    clientes.append(cliente)
    print("Cliente agregado.")

def agregar_mascota():
    tipo = input("¿Perro (P), Gato (G) o Pez (Z)?: ").upper()
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    color = input("Color: ")
    peso = float(input("Peso (kg): "))

    if tipo == "P":
        raza = input("Raza: ")
        animal = Perro(nombre, edad, color, peso, raza)
    elif tipo == "G":
        pelaje = input("Tipo de pelaje: ")
        animal = Gato(nombre, edad, color, peso, pelaje)
    elif tipo == "Z":
        tipo_agua = input("¿Agua dulce o salada?: ")
        animal = Pez(nombre, edad, color, peso, tipo_agua)
    else:
        print("Tipo no válido.")
        return

    animales.append(animal)
    print("Mascota agregada.")

def hacer_adopcion():
    if not clientes or not animales:
        print("Primero debes agregar clientes y mascotas.")
        return

    print("Clientes disponibles:")
    for i, c in enumerate(clientes):
        print(f"{i}. {c.getNombre()}")

    print("Animales disponibles:")
    for j, a in enumerate(animales):
        print(f"{j}. {a.getNombre()} ({a.getEspecie()})")

    i = int(input("Seleccione cliente (número): "))
    j = int(input("Seleccione animal (número): "))
    fecha = input("Fecha de adopción (YYYY-MM-DD): ")

    adopcion = Adopcion(animales[j], clientes[i], fecha)
    adopciones.append(adopcion)
    print("Adopción registrada.")

def ejecutar_metodos():
    for animal in animales:
        if isinstance(animal, Perro):
            print(animal.ladrar())
        elif isinstance(animal, Gato):
            print(animal.maullar())
        elif isinstance(animal, Pez):
            print(animal.nadar())

    for cliente in clientes:
        if isinstance(cliente, ClienteFrecuente):
            print(cliente.acumular_puntos(10))
        elif isinstance(cliente, ClienteVIP):
            print(cliente.aplicar_descuento(100))

# ===================== EJECUCIÓN =====================

menu()
