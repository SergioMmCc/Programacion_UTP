import json

class Libro:
    def __init__(self, titulo, autor, fecha, genero):
        self.titulo = titulo
        self.autor = autor
        self.fecha = fecha
        self.genero = genero

    def jsonStruct(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "fecha": self.fecha,
            "genero": self.genero
        }

class LibroJSONManager:
    def __init__(self, direccion_archivo):
        self.direccion_archivo = direccion_archivo
        self.libros = []

    def agregar_libro(self, libro):
        for existente in self.libros:
            if existente.titulo.lower() == libro.titulo.lower() and existente.autor.lower() == libro.autor.lower():
                print("El libro ya está en la coleccion.")
                return False
        self.libros.append(libro)
        return True

    def guardar_en_json(self):
        try:
            with open(self.direccion_archivo, 'w') as archivo:
                json.dump([libro.jsonStruct() for libro in self.libros], archivo, indent=4)
            print("Libros guardados exitosamente.")
        except Exception as e:
            print(f"Error al guardar: {e}")

    def cargar_desde_json(self):
        try:
            with open(self.direccion_archivo, 'r') as archivo:
                libros_data = json.load(archivo)
                self.libros = [Libro(**datos) for datos in libros_data]
                print("Libros cargados desde archivo.")
        except FileNotFoundError:
            print("Archivo no encontrado, comenzando con lista vacia.")
        except Exception as e:
            print(f"Error al cargar: {e}")

    def mostrar_libros(self):
        for libro in self.libros:
            print(f"- {libro.titulo} por {libro.autor} ({libro.fecha}) [{libro.genero}]")
