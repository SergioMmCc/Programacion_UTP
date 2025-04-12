import os
import json
from clases import Cliente, ClienteFrecuente, ClienteVIP, Animal, Perro, Gato, Pez, Adopcion

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
            "nombre": c.getNombre(),
            "cedula": c.getCedula(),
            "direccion": c.getDireccion(),
            "telefono": c.getTelefono(),
            "correo": c.getCorreo()
        }
        if isinstance(c, ClienteFrecuente):
            base["puntos"] = c.getPuntos()
        elif isinstance(c, ClienteVIP):
            base["descuento"] = c.getDescuento()
        data.append(base)
    with open("clientes.json", "w") as f:
        json.dump(data, f, indent=4)

def guardar_mascotas():
    data = []
    for a in animales:
        base = {
            "tipo": a.__class__.__name__,
            "nombre": a.getNombre(),
            "edad": a.getEdad(),
            "color": a.getColor(),
            "peso": a.getPeso()
        }
        if isinstance(a, Perro):
            base["raza"] = a.getRaza()
        elif isinstance(a, Gato):
            base["pelaje"] = a.getPelaje()
        elif isinstance(a, Pez):
            base["tipo_agua"] = a.getTipo_agua()
        data.append(base)
    with open("mascotas.json", "w") as f:
        json.dump(data, f, indent=4)

def guardar_adopciones():
    data = []
    for a in adopciones:
        data.append({
            "cliente": a.getCliente().getNombre(),
            "animal": a.getAnimal().getNombre(),
            "fecha": a.getFecha()
        })
    with open("adopciones.json", "w") as f:
        json.dump(data, f, indent=4)

def guardar_todo():
    guardar_clientes()
    guardar_mascotas()
    guardar_adopciones()
    print("Datos guardados correctamente.")

# ===================== FUNCIONES CARGA =====================

def cargar_clientes():
    if not os.path.exists("clientes.json"):
        return
    with open("clientes.json", "r") as f:
        data = json.load(f)
    
    clientes.clear()  # Limpia la lista antes de cargar
    
    for c in data:
        if c["tipo"] == "ClienteFrecuente":
            clientes.append(ClienteFrecuente(c["nombre"], c["cedula"], c["direccion"], c["telefono"], c["correo"], c["puntos"]))
        elif c["tipo"] == "ClienteVIP":
            clientes.append(ClienteVIP(c["nombre"], c["cedula"], c["direccion"], c["telefono"], c["correo"], c["descuento"]))
        elif c["tipo"] == "Cliente":
            clientes.append(Cliente(c["nombre"], c["cedula"], c["direccion"], c["telefono"], c["correo"]))

def cargar_mascotas():
    if not os.path.exists("mascotas.json"):
        return
    with open("mascotas.json", "r") as f:
        data = json.load(f)
    
    animales.clear()  # Limpia antes de cargar
    
    for a in data:
        if a["tipo"] == "Perro":
            animales.append(Perro(a["nombre"], a["edad"], a["color"], a["peso"], a["raza"]))
        elif a["tipo"] == "Gato":
            animales.append(Gato(a["nombre"], a["edad"], a["color"], a["peso"], a["pelaje"]))
        elif a["tipo"] == "Pez":
            animales.append(Pez(a["nombre"], a["edad"], a["color"], a["peso"], a["tipo_agua"]))
        elif a["tipo"] == "Animal":
            animales.append(Animal(a["nombre"], a["edad"], a["color"], a["peso"]))

def cargar_adopciones():
    if not os.path.exists("adopciones.json"):
        return
    with open("adopciones.json", "r") as f:
        data = json.load(f)
    
    adopciones.clear()  # Limpiar antes de cargar
    
    for a in data:
        cliente = next((c for c in clientes if c.nombre == a["cliente"]), None)
        animal = next((m for m in animales if m.nombre == a["animal"]), None)
        if cliente and animal:
            adopciones.append(Adopcion(animal, cliente, a["fecha"]))
        else:
            print(f"⚠️ No se encontró cliente o animal para la adopción: {a}")


def cargar_todo():
    cargar_clientes()
    cargar_mascotas()
    cargar_adopciones()