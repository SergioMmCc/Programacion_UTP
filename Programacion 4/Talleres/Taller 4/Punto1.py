import os

class Vehiculo:
    def __init__(self, id, tipo, color, ruedas, marca_llantas, velocidad=None, cilindrada=None):
        self.id = id
        self.tipo = tipo.lower()
        self.color = color
        self.ruedas = ruedas
        self.marca_llantas = marca_llantas.lower()
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def duracion_llantas(self):
        duraciones = {
            "camion": {"bridgestone": 3, "irelli": 2, "firestone": 1},
            "moto": {"bridgestone": 9, "irelli": 7, "firestone": 5},
            "automovil": {"bridgestone": 7, "irelli": 6, "firestone": 4},
        }
        return duraciones.get(self.tipo, {}).get(self.marca_llantas, "Desconocido")

    def tipo_combustible(self):
        combustibles = {
            "camion": "ACPM",
            "moto": "Corriente",
            "automovil": "Extra",
        }
        return combustibles.get(self.tipo, "No se reconoce ese tipo de vehículo")

    def gasto(self):
        if self.cilindrada:
            consumo = max(10, 50000 / self.cilindrada)
            galones_necesarios = 1000 / consumo
            precio_por_galon = 16000
            return round(galones_necesarios * precio_por_galon, 2)
        return "No aplica"
    
    def tiempo_viaje(self, destino):
        if not self.velocidad:
            return "No aplica"
        distancias = {
            "medellin": 240,
            "bogota": 317,
            "cartagena": 943,
            "manizales": 53,
            "dosquebradas": 10,
        }
        return round(distancias.get(destino.lower(), 0) / self.velocidad, 2)

class GestorVehiculos:
    def __init__(self):
        self.lista_vehiculos = []

    def agregar_vehiculo(self, id, tipo, color, ruedas, marca_llantas, velocidad=None, cilindrada=None):
        vehiculo = Vehiculo(id, tipo, color, ruedas, marca_llantas, velocidad, cilindrada)
        self.lista_vehiculos.append(vehiculo)
        print("Vehículo agregado con éxito.")

    def mostrar_vehiculos(self):
        for vehiculo in self.lista_vehiculos:
            print(f"\nID: {vehiculo.id} Tipo: {vehiculo.tipo.capitalize()}, Color: {vehiculo.color}, Ruedas: {vehiculo.ruedas}, Llantas: {vehiculo.marca_llantas.capitalize()}")
            print(f"Duración estimada de llantas: {vehiculo.duracion_llantas()} años")
            print(f"Combustible recomendado: {vehiculo.tipo_combustible()}")
            if vehiculo.velocidad:
                print(f"Velocidad: {vehiculo.velocidad} km/h, Cilindrada: {vehiculo.cilindrada} cc")
                print(f"Gasto mensual en combustible: ${vehiculo.gasto()} COP")

    def guardar_vehiculos(self, archivo):
        with open(archivo, "w") as file:
            for vehiculo in self.lista_vehiculos:
                file.write(f"{vehiculo.id},{vehiculo.tipo},{vehiculo.color},{vehiculo.ruedas},{vehiculo.marca_llantas},{vehiculo.velocidad or ''},{vehiculo.cilindrada or ''}\n")

    def cargar_vehiculos(self, archivo):
        try:
            with open(archivo, "r") as file:
                for line in file:
                    datos = line.strip().split(",")
                    id, tipo, color, ruedas, marca_llantas, velocidad, cilindrada = datos + [None] * (7 - len(datos))
                    self.lista_vehiculos.append(Vehiculo(id, tipo, color, int(ruedas), marca_llantas, int(velocidad) if velocidad else None, int(cilindrada) if cilindrada else None))
        except FileNotFoundError:
            print("El archivo no existe, iniciando con una lista vacía.")


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    gestor = GestorVehiculos()
    gestor.cargar_vehiculos("vehiculos.txt")

    while True:
        print("\nMenú de Opciones")
        print("1. Agregar Vehículo")
        print("2. Mostrar Vehículos")
        print("3. Calcular Tiempo de Viaje")
        print("4. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            id = int(input("ID del vehiculo: "))
            tipo = input("Tipo de vehículo (Automóvil, Camión, Moto): ").strip().lower()
            color = input("Color: ").strip()
            ruedas = int(input("Número de ruedas: "))
            marca_llantas = input("Marca de llantas (Bridgestone, Irelli, Firestone): ").strip().lower()
            velocidad = cilindrada = None
            
            if tipo == "automovil":
                velocidad = int(input("Velocidad máxima (km/h): "))
                cilindrada = int(input("Cilindrada (cc): "))
                
            gestor.agregar_vehiculo(id, tipo, color, ruedas, marca_llantas, velocidad, cilindrada)

        elif opcion == "2":
            print("\nLista de Vehículos:")
            gestor.mostrar_vehiculos()

        elif opcion == "3":
            id = int(input("Ingrese el ID del vehiculo: "))
            destino = input("Ingrese el destino (Medellin, Bogota, Cartagena, Manizales, Dosquebradas): ").strip()
            for vehiculo in gestor.lista_vehiculos:
                if vehiculo.id == id:
                    print(f"Tiempo estimado de viaje: {vehiculo.tiempo_viaje(destino)} horas")
                    break
            else:
                print("Vehículo no encontrado.")

        elif opcion == "4":
            gestor.guardar_vehiculos("vehiculos.txt")
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        else:
            print("Opción inválida.")

        input("\nPresione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

menu()
