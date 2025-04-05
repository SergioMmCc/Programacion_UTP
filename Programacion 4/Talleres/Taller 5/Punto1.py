from datetime import datetime
import os

# Para el siguiente grafico diseñe un algoritmo implementando herencia
# múltiple:

    #    - PersonalUniversitario -
    #    |                        |
    # Profesor                Alumno
    #    |                        |
    #    ---- ProfesorAyudante ----

# a. Para cada clase debe diseñar al menos 6 atributos.
# b. Para las clases profesor debe realizar un método en donde se pueda
#    calcular el sueldo mensual dependiendo de las horas que trabaja y del
#    tipo de profesor que sea
# c. Debe de crear un método para calcular la antigüedad de todas las
#    entidades en el diseño.
# d. Dependiendo de cada tipo de profesor debe diseñar al menos tres
#    materias acordes con el rango de cada uno y se deben visualizar en
#    pantalla por medio de un método.
# e. Guarde la información que crea necesaria en un archivo para este
#    programa.

class PersonalUniversitario:
    def __init__(self, nombre, programa, dia, mes, anio):
        self.nombre = nombre
        self.programa = programa
        self.fecha_ingreso = datetime(anio, mes, dia)

    def calcular_antiguedad(self):
        hoy = datetime.now()
        return hoy.year - self.fecha_ingreso.year - (
            (hoy.month, hoy.day) < (self.fecha_ingreso.month, self.fecha_ingreso.day)
        )


class Profesor(PersonalUniversitario):
    def __init__(self, nombre, programa, dia, mes, anio, horas_trabajo, materias):
        super().__init__(nombre, programa, dia, mes, anio)
        self.horas_trabajo = horas_trabajo
        self.materias = materias

    def calcularSalario(self):
        return 40000 * self.horas_trabajo


class Alumno(PersonalUniversitario):
    def __init__(self, nombre, programa, dia, mes, anio, semestre):
        super().__init__(nombre, programa, dia, mes, anio)
        self.semestre = semestre


class ProfesorAyudante(Profesor, Alumno):
    def __init__(self, nombre, programa, dia, mes, anio, horas_trabajo, materias, tipo, semestre):
        self.tipo = tipo.lower()  # "profesor" o "alumno"

        if self.tipo == "profesor":
            Profesor.__init__(self, nombre, programa, dia, mes, anio, horas_trabajo, materias)
            self.semestre = ""
        elif self.tipo == "alumno":
            Alumno.__init__(self, nombre, programa, dia, mes, anio, semestre)
            self.horas_trabajo = horas_trabajo
            self.materias = materias
        else:
            raise ValueError("Tipo debe ser 'profesor' o 'alumno'")

    def calcularSalario(self):
        return 9500 * self.horas_trabajo



def guardar_datos(profesores, alumnos, ayudantes, archivo="datos.txt"):
    with open(archivo, "w") as f:
        for p in profesores:
            f.write(f"P|{p.nombre}|{p.programa}|{p.fecha_ingreso.day}|{p.fecha_ingreso.month}|{p.fecha_ingreso.year}|{p.horas_trabajo}|{','.join(p.materias)}\n")
        for a in alumnos:
            f.write(f"A|{a.nombre}|{a.programa}|{a.fecha_ingreso.day}|{a.fecha_ingreso.month}|{a.fecha_ingreso.year}|{a.semestre}\n")
        for pa in ayudantes:
            f.write(f"PA|{pa.nombre}|{pa.programa}|{pa.fecha_ingreso.day}|{pa.fecha_ingreso.month}|{pa.fecha_ingreso.year}|{pa.horas_trabajo}|{','.join(pa.materias)}|{pa.tipo}|{pa.semestre}\n")

def cargar_datos(archivo="datos.txt"):
    profesores, alumnos, ayudantes = [], [], []
    with open(archivo, "r") as f:
        for linea in f:
            datos = linea.strip().split("|")
            tipo = datos[0]
            if tipo == "P":
                nombre, programa, d, m, a, horas, materias = datos[1:]
                profesores.append(Profesor(nombre, programa, int(d), int(m), int(a), int(horas), materias.split(",")))
            elif tipo == "A":
                nombre, programa, d, m, a, semestre = datos[1:]
                alumnos.append(Alumno(nombre, programa, int(d), int(m), int(a), int(semestre)))
            elif tipo == "PA":
                nombre, programa, d, m, a, horas, materias, tipo_pa, semestre = datos[1:]
                ayudantes.append(ProfesorAyudante(nombre, programa, int(d), int(m), int(a), int(horas), materias.split(","), tipo_pa, semestre))
    return profesores, alumnos, ayudantes



def menu():
    os.system('cls' if os.name == 'nt' else 'clear') # Limpiar la consola
    profesores, alumnos, ayudantes = cargar_datos()

    def agregar_profesor():
        nombre = input("Nombre: ")
        programa = input("Programa: ")
        dia = int(input("Día ingreso: "))
        mes = int(input("Mes ingreso: "))
        anio = int(input("Año ingreso: "))
        horas = int(input("Horas trabajo: "))
        materias = input("Materias (separadas por coma): ").split(",")
        profesores.append(Profesor(nombre, programa, dia, mes, anio, horas, materias))

    def agregar_alumno():
        nombre = input("Nombre: ")
        programa = input("Programa: ")
        dia = int(input("Día ingreso: "))
        mes = int(input("Mes ingreso: "))
        anio = int(input("Año ingreso: "))
        semestre = int(input("Semestre actual: "))
        alumno = Alumno(nombre, programa, dia, mes, anio, semestre)
        alumnos.append(alumno)

    def agregar_ayudante():
        nombre = input("Nombre: ")
        programa = input("Programa: ")
        dia = int(input("Día ingreso: "))
        mes = int(input("Mes ingreso: "))
        anio = int(input("Año ingreso: "))
        horas = int(input("Horas trabajo: "))
        materias = input("Materias (separadas por coma): ").split(",")
        semestre = int(input("Semestre (si es alumno, si no, pon 0): "))
        tipo = ""
        if semestre == 0:
            tipo = "profesor"
        else:
            tipo = "alumno"
        ayudante = ProfesorAyudante(nombre, programa, dia, mes, anio, horas, materias, tipo, semestre)
        ayudantes.append(ayudante)

    def salario_profesor():
        nombre = input("Nombre del profesor: ")
        for p in profesores:
            if p.nombre == nombre:
                print(f"Salario de {p.nombre}: ${p.calcularSalario():,}")
                return
        print("Profesor no encontrado")

    def salario_ayudante():
        nombre = input("Nombre del profesor ayudante: ")
        for pa in ayudantes:
            if pa.nombre == nombre:
                print(f"Salario de {pa.nombre}: ${pa.calcularSalario():,}")
                return
        print("Profesor Ayudante no encontrado")

    def mostrar_datos():
        print("\n--- Profesores ---")
        for p in profesores:
            print(vars(p))
        print("\n--- Alumnos ---")
        for a in alumnos:
            print(vars(a))
        print("\n--- Profesores Ayudantes ---")
        for pa in ayudantes:
            print(vars(pa))

    def averiguar_antiguedad():
        nombre = input("Nombre de la persona: ")
        for persona in profesores + alumnos + ayudantes:
            if persona.nombre == nombre:
                print(f"Antigüedad de {nombre}: {persona.calcular_antiguedad()} años")
                return
        print("No se encontró a esa persona")

    # Menú principal
    while True:
        print("\n--- Menú ---")
        print("1. Agregar Profesor")
        print("2. Agregar Alumno")
        print("3. Agregar Profesor Ayudante")
        print("4. Ver salario de Profesor")
        print("5. Ver salario de Profesor Ayudante")
        print("6. Mostrar todos los datos")
        print("7. Averiguar antigüedad")
        print("8. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            agregar_profesor()
        elif opcion == "2":
            agregar_alumno()
        elif opcion == "3":
            agregar_ayudante()
        elif opcion == "4":
            salario_profesor()
        elif opcion == "5":
            salario_ayudante()
        elif opcion == "6":
            mostrar_datos()
        elif opcion == "7":
            averiguar_antiguedad()
        elif opcion == "8":
            guardar_datos(profesores, alumnos, ayudantes)
            print("Datos guardados. Saliendo...")
            break
        else:
            print("Opción no válida")

        input("\nPresione Enter para continuar...") # Esperar a que el usuario presione Enter
        os.system('cls' if os.name == 'nt' else 'clear') # Limpiar la consola

menu()