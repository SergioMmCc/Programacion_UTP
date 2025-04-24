from objetos import *

###################### FUNCIONES PARA RESERVA Y CONSULTA #################
def reservar(numero):
    for h in simples:
        if h.getNumero() == numero:
            if h.getEstado() == "disponible":
                h.setEstado("reservado")
                return f"Se confirma su reserva de la habitación {h.getNumero()}. El valor a pagar será ${h.getPrecio()}"
            else:
                return f"La habitación {h.getNumero()} no se encuentra disponible"
            
    for h in dobles:
        if h.getNumero() == numero:
            if h.getEstado() == "disponible":
                precioTotal = h.getPrecio()
                reservarDesayuno = input("¿Desea incluir desayuno por un costo adicional de $15000? (1 para incluir, 0 para no incluir): ")
                if reservarDesayuno != "1":
                    h.setDesayuno(False)
                else:
                    h.setDesayuno(True)
                    precioTotal += 15000

                reservarSpa = input("¿Desea incluir servicio de SPA por un costo adicional de $30000? (1 para incluir, 0 para no incluir): ")
                if reservarSpa != "1":
                    h.setSpa(False)
                else:
                    h.setSpa(True)
                    precioTotal += 30000


                h.setEstado("reservado")
                return f"Se confirma su reserva de la habitación {h.getNumero()}, el valor a pagar será ${precioTotal}"
            else:
                return f"La habitación {h.getNumero()} no se encuentra disponible"
            
    for h in suites:
        if h.getNumero() == numero:
            if h.getEstado() == "disponible":
                precioTotal = h.getPrecio()
                reservarDesayuno = input("¿Desea incluir desayuno por un costo adicional de $10000? (1 para incluir, 0 para no incluir): ")
                if reservarDesayuno != "1":
                    h.setDesayuno(False)
                else:
                    h.setDesayuno(True)
                    precioTotal += 10000

                reservarSpa = input("¿Desea incluir servicio de SPA por un costo adicional de $25000? (1 para incluir, 0 para no incluir): ")
                if reservarSpa != "1":
                    h.setSpa(False)
                else:
                    h.setSpa(True)
                    precioTotal += 25000

                reservarGym = input("¿Desea incluir reserva de gimnasio por un costo adicional de $5000? (1 para incluir, 0 para no incluir): ")
                if reservarGym != "1":
                    h.setGym(False)
                else:
                    h.setGym(True)
                    precioTotal += 5000


                h.setEstado("reservado")
                return f"Se confirma su reserva de la habitación {h.getNumero()}, el valor a pagar será ${precioTotal}"
            else:
                return f"La habitación {h.getNumero()} no se encuentra disponible"
            

    # En caso de que no se encuentre el numero de habiatacion
    return f"No tenemos ninguna habitación con el número {numero}"


def mostrarDisponibles():
    print("Tenemos las siguientes habitaciones simples:")
    count = 0
    for h in simples:
        if h.getEstado() == "disponible":
            count += 1
            print(f"Número: {h.getNumero()}, precio: ${h.getPrecio()}")
    if count == 0:
        print("¡Oh!, Parece que no nos quedan habitaciones simples disponibles")

    print("\nTenemos las siguientes habitaciones dobles:")
    count = 0
    for h in dobles:
        if h.getEstado() == "disponible":
            count += 1
            print(f"Número: {h.getNumero()}, precio con todos los servicios extra incluidos: ${h.getPrecio() + 45000}, precio sin servicios extra: ${h.getPrecio()}")
    if count == 0:
        print("¡Oh!, Parece que no nos quedan habitaciones dobles disponibles")

    print("\nTenemos las siguientes suites:")
    count = 0
    for h in suites:
        if h.getEstado() == "disponible":
            count += 1
            print(f"Número: {h.getNumero()}, precio con todos los servicios extra incluidos: ${h.getPrecio() + 40000}, precio sin servicios extra: ${h.getPrecio()}")
    if count == 0:
        print("¡Oh!, Parece que no nos quedan suites disponibles")