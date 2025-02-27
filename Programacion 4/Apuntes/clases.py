# class ejemplo: # Recomendable que la primera letra sea mayuscula

#     # atributos
#     asignatura = "Programacion"
#     num_horas = 4

#     def conteo_horas(self): 
#         # El self no es un parametro, es una referencia a la instancia de la clase
#         # Asi que cuando se llama a un metodo de la clase, se pasa automaticamente
#         # sin necesidad de pasarle un valor
#         pass
#     def cantidad_horas(self):
#         pass

class Estudiante:
    # Atributos
    nombre = ""
    edad = 0
    carrera = ""

    # Metodos
    def mostrar_datos(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nCarrera: {self.carrera}\n"

    def ingresar_datos(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input(f"Ingrese la edad de {self.nombre}: "))
        self.carrera = input("Ingrese la carrera: ")
        print()

pepito = Estudiante() # Pepito es un objeto de la clase Estudiante
pepito.ingresar_datos()
print(pepito.mostrar_datos())