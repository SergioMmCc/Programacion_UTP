from gestor import Libro, LibroJSONManager

def menu():
    archivo = "libros.json"
    manager = LibroJSONManager(archivo)
    manager.cargar_desde_json()

    while True:
        print("\nMenu de libros")
        print("1. Agregar libro")
        print("2. Ver libros")
        print("3. Guardar")
        print("4. Salir sin guardar")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            anio = int(input("Año: "))
            genero = input("Género: ")
            nuevo_libro = Libro(titulo, autor, anio, genero)
            fue_agregado = manager.agregar_libro(nuevo_libro)
            if fue_agregado:
                print("Libro agregado.")
            else:
                print("Intente con un título o autor diferente.")
        elif opcion == "2":
            print("\nLista de libros:")
            manager.mostrar_libros()
        elif opcion == "3":
            manager.guardar_en_json()
            print("Datos guardados exitosamente.")
        elif opcion == "4":
            print("Hasta luego")
            break
        else:
            print("Opción inválida")

menu()
