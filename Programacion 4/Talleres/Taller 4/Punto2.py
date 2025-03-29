class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"{self.__class__.__name__} (Color: {self.color}, Ruedas: {self.ruedas})"


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f", Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f", Tipo: {self.tipo}"


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + f", Carga: {self.carga} kg"


class Motocicleta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas, velocidad, cilindrada)

    def __str__(self):
        return super().__str__()


def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos_filtrados = [v for v in vehiculos if v.ruedas == ruedas]
        print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
        for vehiculo in vehiculos_filtrados:
            print(vehiculo)
    else:
        for vehiculo in vehiculos:
            print(vehiculo)


# Crear objetos de cada subclase
vehiculos = [
    Coche("Rojo", 4, 120, 1500),
    Bicicleta("Azul", 2, "Urbana"),
    Camioneta("Blanco", 4, 100, 2000, 500),
    Motocicleta("Negro", 2, 180, 600)
]

# Probar la función catalogar
print("Catálogo completo:")
catalogar(vehiculos)

print("\nCatálogo con 0 ruedas:")
catalogar(vehiculos, 0)

print("\nCatálogo con 2 ruedas:")
catalogar(vehiculos, 2)

print("\nCatálogo con 4 ruedas:")
catalogar(vehiculos, 4)