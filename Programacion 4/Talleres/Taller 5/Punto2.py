import json
import os

# ===================== CLASES =====================

class Animal:
    def __init__(self, nombre, especie, edad, color, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.color = color
        self.peso = peso

    def mostrar_info(self):
        return f"{self.nombre}, {self.especie}, {self.edad} años, {self.color}, {self.peso} kg"

class Cliente:
    def __init__(self, nombre, cedula, direccion, telefono, correo):
        self.nombre = nombre
        self.cedula = cedula
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    def mostrar_info(self):
        return f"{self.nombre}, C.C: {self.cedula}, {self.telefono}, {self.correo}"

# Subclases de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, color, peso, raza):
        super().__init__(nombre, "Perro", edad, color, peso)
        self.raza = raza

    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau!"

class Gato(Animal):
    def __init__(self, nombre, edad, color, peso, pelaje):
        super().__init__(nombre, "Gato", edad, color, peso)
        self.pelaje = pelaje

    def maullar(self):
        return f"{self.nombre} dice: Miau"

class Pez(Animal):
    def __init__(self, nombre, edad, color, peso, tipo_agua):
        super().__init__(nombre, "Pez", edad, color, peso)
        self.tipo_agua = tipo_agua

    def nadar(self):
        return f"{self.nombre} nada en agua {self.tipo_agua}"

# Subclases de Cliente
class ClienteFrecuente(Cliente):
    def __init__(self, nombre, cedula, direccion, telefono, correo, puntos):
        super().__init__(nombre, cedula, direccion, telefono, correo)
        self.puntos = puntos

    def acumular_puntos(self, cantidad):
        self.puntos += cantidad
        return f"{self.nombre} ahora tiene {self.puntos} puntos."

class ClienteVIP(Cliente):
    def __init__(self, nombre, cedula, direccion, telefono, correo, descuento):
        super().__init__(nombre, cedula, direccion, telefono, correo)
        self.descuento = descuento

    def aplicar_descuento(self, precio):
        precio_final = precio * (1 - self.descuento)
        return f"Precio con descuento VIP: ${precio_final:.2f}"

class Adopcion:
    def __init__(self, animal, cliente, fecha):
        self.animal = animal
        self.cliente = cliente
        self.fecha = fecha

    def resumen_adopcion(self):
        return f"{self.cliente.nombre} adoptó a {self.animal.nombre} el {self.fecha}"

# ===================== LISTAS =====================

clientes = []
animales = []
adopciones = []

# ===================== FUNCIONES GUARDADO =====================

def guardar_clientes():
    data = []
    for c in clientes:
        base = {
            "tipo": c.__class__.__name__,
            "nombre": c.nombre,
            "cedula": c.cedula,
            "direccion": c.direccion,
            "telefono": c.telefono,
            "correo": c.correo
        }
        if isinstance(c, ClienteFrecuente):
            base["puntos"] = c.puntos
        elif isinstance(c, ClienteVIP):
            base["descuento"] = c.descuento
        data.append(base)
    with open("clientes.json", "w") as f:
        json.dump(data, f, indent=4)

def guardar_mascotas():
    data = []
    for a in animales:
        base = {
            "tipo": a.__class__.__name__,
            "nombre": a.nombre,
            "edad": a.edad,
            "color": a.color,
            "peso": a.peso
        }
        if isinstance(a, Perro):
            base["raza"] = a.raza
        elif isinstance(a, Gato):
            base["pelaje"] = a.pelaje
        elif isinstance(a, Pez):
            base["tipo_agua"] = a.tipo_agua
        data.append(base)
    with open("mascotas.json", "w") as f:
        json.dump(data, f, indent=4)

def guardar_adopciones():
    data = []
    for a in adopciones:
        data.append({
            "cliente": a.cliente.nombre,
            "animal": a.animal.nombre,
            "fecha": a.fecha
        })
    with open("adopciones.json", "w") as f:
        json.dump(data, f, indent=4)

def guardar_todo():
    guardar_clientes()
    guardar_mascotas()
    guardar_adopciones()
    print("✅ Datos guardados correctamente.")

# ===================== FUNCIONES CARGA =====================

def cargar_clientes():
    if not os.path.exists("clientes.json"):
        return
    with open("clientes.json", "r") as f:
        data = json.load(f)
    for c in data:
        if c["tipo"] == "ClienteFrecuente":
            clientes.append(ClienteFrecuente(c["nombre"], c["cedula"], c["direccion"], c["telefono"], c["correo"], c["puntos"]))
        elif c["tipo"] == "ClienteVIP":
            clientes.append(ClienteVIP(c["nombre"], c["cedula"], c["direccion"], c["telefono"], c["correo"], c["descuento"]))

def cargar_mascotas():
    if not os.path.exists("mascotas.json"):
        return
    with open("mascotas.json", "r") as f:
        data = json.load(f)
    for a in data:
        if a["tipo"] == "Perro":
            animales.append(Perro(a["nombre"], a["edad"], a["color"], a["peso"], a["raza"]))
        elif a["tipo"] == "Gato":
            animales.append(Gato(a["nombre"], a["edad"], a["color"], a["peso"], a["pelaje"]))
        elif a["tipo"] == "Pez":
            animales.append(Pez(a["nombre"], a["edad"], a["color"], a["peso"], a["tipo_agua"]))

def cargar_adopciones():
    if not os.path.exists("adopciones.json"):
        return
    with open("adopciones.json", "r") as f:
        data = json.load(f)
    for a in data:
        cliente = next((c for c in clientes if c.nombre == a["cliente"]), None)
        animal = next((m for m in animales if m.nombre == a["animal"]), None)
        if cliente and animal:
            adopciones.append(Adopcion(animal, cliente, a["fecha"]))

def cargar_todo():
    cargar_clientes()
    cargar_mascotas()
    cargar_adopciones()

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
    print("✅ Cliente agregado.")

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
    print("✅ Mascota agregada.")

def hacer_adopcion():
    if not clientes or not animales:
        print("Primero debes agregar clientes y mascotas.")
        return

    print("Clientes disponibles:")
    for i, c in enumerate(clientes):
        print(f"{i}. {c.nombre}")

    print("Animales disponibles:")
    for j, a in enumerate(animales):
        print(f"{j}. {a.nombre} ({a.especie})")

    i = int(input("Seleccione cliente (número): "))
    j = int(input("Seleccione animal (número): "))
    fecha = input("Fecha de adopción (YYYY-MM-DD): ")

    adopcion = Adopcion(animales[j], clientes[i], fecha)
    adopciones.append(adopcion)
    print("✅ Adopción registrada.")

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
