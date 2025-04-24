from objetos import *

# Función para mostrar productos agrupados
def mostrar_productos():
    print("\n=== Productos Electrónicos ===")
    for p in electronicos:
        print(f"- {p.getNombre()}, ${p.getPrecio()}, stock: {p.getCantidad()}, garantía: {p.getGarantia()} meses")

    print("\n=== Productos de Ropa ===")
    for p in ropa:
        print(f"- {p.getNombre()}, ${p.getPrecio()}, stock: {p.getCantidad()}, talla: {p.getTalla()}")

    print("\n=== Alimentos ===")
    for p in alimentos:
        print(f"- {p.getNombre()}, ${p.getPrecio()}, stock: {p.getCantidad()}, caduca: {p.getCaducidad()}")

# Función para realizar pedido
def realizar_pedido(nombre_producto, cantidad):
    for lista in [electronicos, ropa, alimentos]:
        for producto in lista:
            if producto.getNombre().lower() == nombre_producto.lower():
                if producto.getCantidad() >= cantidad:
                    producto.setCantidad(producto.getCantidad() - cantidad)
                    precio = producto.getPrecio() * cantidad
                    if cantidad >= 5:
                        precio *= 0.9 # Descuento del 10%
                    return f"Pedido exitoso: {cantidad} unidad(es) de {producto.getNombre()} por ${precio:.2f}"
                else:
                    return f"No hay suficiente stock de {producto.getNombre()}"
    return "Producto no encontrado"

