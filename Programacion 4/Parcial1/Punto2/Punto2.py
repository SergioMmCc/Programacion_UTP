import os

# Clase Empleado:

# • Atributos:
#   o Nombre (cadena de texto)
#   o ID (entero)
#   o Salario Base (flotante)
#   o Años de Experiencia (entero)

# • Métodos:
#   o Constructor para inicializar todos los atributos.
#   o Un método calcular_salario() que retorne el salario total del
#     empleado. El salario total se calcula sumando un bono al salario
#     base que depende de los años de experiencia:
#     ▪ Entre 0 y 2 años: bono de 5% del salario base.
#     ▪ Entre 3 y 5 años: bono de 10% del salario base.
#     ▪ Más de 5 años: bono de 15% del salario base.
#   o Un método para representar al empleado en formato de texto.
class Empleado:
    def __init__(self, nombre, id, salario_base, años_experiencia):
        self.nombre = nombre
        self.id = id
        self.salario_base = salario_base
        self.años_experiencia = años_experiencia

    def calcular_salario(self):
        if self.años_experiencia <= 2:
            bono = self.salario_base * 0.05
        elif self.años_experiencia <= 5:
            bono = self.salario_base * 0.10
        else:
            bono = self.salario_base * 0.15
        return self.salario_base + bono

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id}, Salario: {self.calcular_salario()}"


# Clase GestorEmpleados:

# • Atributos:
#   o Una lista de empleados.

# • Métodos:
#   o agregar_empleado(empleado: Empleado): Agrega un empleado a
#     la lista.
#   o eliminar_empleado(id: int): Elimina un empleado de la lista según
#     su ID.
#   o buscar_empleado(id: int): Busca y devuelve un empleado por su
#     ID.
#   o editar_empleado(id: int): Busca un empleado y deja editar la
#     informacion que se quiera del empleado, luego se debe actualizar
#     el archivo donde esta guardada la información.
#     o mostrar_empleados(): Muestra todos los empleados de la lista
#     junto con sus salarios totales.
#   o guardar_empleados(archivo: str): Guarda la lista de empleados
#     en un archivo.
#   o cargar_empleados(archivo: str): Carga la lista de empleados
#     desde un archivo.
class GestorEmpleados:
    def __init__(self):
        self.lista_empleados = []

    def agregar_empleado(self, empleado):
        self.lista_empleados.append(empleado)

    def eliminar_empleado(self, id):
        for empleado in self.lista_empleados:
            if empleado.id == id:
                self.lista_empleados.remove(empleado)
                print("Empleado eliminado con éxito") # Mensaje de confirmación
                return
        print("Empleado no encontrado") # Mensaje de error
            
    def buscar_empleado(self, id):
        for empleado in self.lista_empleados:
            if empleado.id == id:
                return empleado # Devolver el empleado encontrado
        return None # Devolver None si no se encontró el empleado
    
    def editar_empleado(self, id):
        empleado = self.buscar_empleado(id)
        if empleado:
            print("\nDatos anteriores:") # Mostrar los datos anteriores del empleado
            print(empleado)
            print("\nIngrese los nuevos datos:")

            # Solicitar los nuevos datos del empleado
            nombre = input("Nombre: ")
            salario_base = float(input("Salario Base: "))
            años_experiencia = int(input("Años de Experiencia: "))
            empleado.nombre = nombre
            empleado.salario_base = salario_base
            empleado.años_experiencia = años_experiencia
            return True
        return False
    
    def mostrar_empleados(self):
        # Mostrar los empleados de la lista
        for empleado in self.lista_empleados:
            print(empleado)

    # Guardar los empleados en un archivo
    def guardar_empleados(self, archivo):
        with open(archivo, "w") as file:
            for empleado in self.lista_empleados:
                file.write(f"{empleado.nombre},{empleado.id},{empleado.salario_base},{empleado.años_experiencia}\n")

    # Cargar los empleados desde un archivo
    def cargar_empleados(self, archivo):
        with open(archivo, "r") as file:
            for line in file:
                nombre, id, salario_base, años_experiencia = line.strip().split(",")
                empleado = Empleado(nombre, int(id), float(salario_base), int(años_experiencia))
                self.lista_empleados.append(empleado)


# Menú de la aplicación:
def menu():
    os.system('cls' if os.name == 'nt' else 'clear') # Limpiar la consola
    gestor = GestorEmpleados() # Crear un gestor de empleados
    gestor.cargar_empleados("empleados.txt") # Cargar los empleados desde un archivo
    while True:

        # Menú de opciones de la aplicación
        print("Menú de Opciones")
        print("\n1. Agregar Empleado")
        print("2. Eliminar Empleado")
        print("3. Buscar Empleado")
        print("4. Editar Empleado")
        print("5. Mostrar Empleados")
        print("6. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            id = int(input("ID: "))
            salario_base = float(input("Salario Base: "))
            años_experiencia = int(input("Años de Experiencia: "))
            empleado = Empleado(nombre, id, salario_base, años_experiencia)
            gestor.agregar_empleado(empleado)
            print("Empleado agregado con éxito") # Mensaje de confirmación
        
        elif opcion == "2":
            id = int(input("ID: ")) # Solicitar el ID del empleado a eliminar
            gestor.eliminar_empleado(id)
        
        elif opcion == "3":
            id = int(input("ID: ")) # Solicitar el ID del empleado a buscar
            empleado = gestor.buscar_empleado(id)
            print()
            if empleado:
                print(empleado)
            else:
                print("Empleado no encontrado") # Mensaje de error
        
        elif opcion == "4":
            id = int(input("ID: ")) # Solicitar el ID del empleado a editar
            if not gestor.editar_empleado(id):
                print("Empleado no encontrado") # Mensaje de error
            else:
                print("Empleado editado con éxito") # Mensaje de confirmación
        
        elif opcion == "5":
            print()
            gestor.mostrar_empleados()
        
        elif opcion == "6":
            gestor.guardar_empleados("empleados.txt") # Guardar los empleados en un archivo
            os.system('cls' if os.name == 'nt' else 'clear') # Limpiar la consola
            break
        
        else: # Opción inválida
            print("Opción inválida") # Mensaje de error

        input("\nPresione Enter para continuar...") # Esperar a que el usuario presione Enter
        os.system('cls' if os.name == 'nt' else 'clear') # Limpiar la consola


menu()