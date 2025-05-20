import os
from controladores import (
    crear_pasajero,
    crear_avion,
    crear_vuelo,
    crear_reserva,
    cambiar_a_ejecutiva,

    consultar_vuelos,
    consultar_vuelo_por_id,
    consultar_vuelos_por_ruta,

    consultar_reserva_por_id,
    consultar_reservas_activas,
    consultar_reservas_por_pasajero,

    consultar_pasajero,
    mostrar_pasajeros_vuelo,
    consultar_avion_por_id,
    consultar_todos_los_aviones,
)
from vistas import (
    datos_pasajero_desde_input,
    datos_avion_desde_input,
    datos_vuelo_desde_input,
    datos_reserva_desde_input,
    id_reserva_para_cambio_desde_input,

    pedir_id_avion,
    pedir_id_pasajero,
    pedir_id_reserva,
    pedir_id_vuelo,
    pedir_origen_y_destino,
)


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear pasajero")
        print("2. Crear avión")
        print("3. Crear vuelo")
        print("4. Crear reserva")
        print("5. Cambiar reserva a clase ejecutiva")
        print("6. Consultar todos los vuelos")
        print("7. Consultar vuelo por ID")
        print("8. Consultar vuelos por ruta")
        print("9. Consultar reserva por ID")
        print("10. Consultar reservas activas")
        print("11. Consultar reservas por pasajero")
        print("12. Consultar pasajero por ID")
        print("13. Mostrar pasajeros de un vuelo")
        print("14. Consultar avión por ID")
        print("15. Consultar todos los aviones")
        print("16. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            datos = datos_pasajero_desde_input()
            if datos:
                crear_pasajero(*datos)

        elif opcion == "2":
            datos = datos_avion_desde_input()
            if datos:
                crear_avion(*datos)

        elif opcion == "3":
            datos = datos_vuelo_desde_input()
            if datos:
                crear_vuelo(*datos)

        elif opcion == "4":
            datos = datos_reserva_desde_input()
            if datos:
                crear_reserva(*datos)

        elif opcion == "5":
            id_reserva = id_reserva_para_cambio_desde_input()
            if id_reserva is not None:
                cambiar_a_ejecutiva(id_reserva)

        elif opcion == "6":
            consultar_vuelos()

        elif opcion == "7":
            id_vuelo = pedir_id_vuelo()
            if id_vuelo is not None:
                consultar_vuelo_por_id(id_vuelo)

        elif opcion == "8":
            origen, destino = pedir_origen_y_destino()
            consultar_vuelos_por_ruta(origen, destino)

        elif opcion == "9":
            id_reserva = pedir_id_reserva()
            if id_reserva is not None:
                consultar_reserva_por_id(id_reserva)

        elif opcion == "10":
            consultar_reservas_activas()

        elif opcion == "11":
            id_pasajero = pedir_id_pasajero()
            if id_pasajero is not None:
                consultar_reservas_por_pasajero(id_pasajero)

        elif opcion == "12":
            id_pasajero = pedir_id_pasajero()
            if id_pasajero is not None:
                consultar_pasajero(id_pasajero)

        elif opcion == "13":
            id_vuelo = pedir_id_vuelo()
            if id_vuelo is not None:
                mostrar_pasajeros_vuelo(id_vuelo)

        elif opcion == "14":
            id_avion = pedir_id_avion()
            if id_avion is not None:
                consultar_avion_por_id(id_avion)

        elif opcion == "15":
            consultar_todos_los_aviones()

        elif opcion == "16":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

        input("\nPresione enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')