# Clase Producto
class Producto:
    def __init__(self, nombre, id_producto, precio, cantidad):
        self.nombre = nombre
        self.id_producto = id_producto
        self.precio = precio
        self.cantidad = cantidad

    def disminuir_inventario(self, cantidad: int):
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad
        else:
            print(f"No hay suficiente stock de {self.nombre}.")

    def aumentar_inventario(self, cantidad: int):
        self.cantidad += cantidad

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}, ID: {self.id_producto}, Precio: ${self.precio}, Stock: {self.cantidad}")


# Clase Cliente
class Cliente:
    def __init__(self, nombre, id_cliente, saldo):
        self.nombre = nombre
        self.id_cliente = id_cliente
        self.saldo = saldo

    def realizar_compra(self, producto, cantidad: int):
        total = producto.precio * cantidad

        # Verificar si el cliente tiene saldo suficiente y hay stock disponible
        if self.saldo >= total and producto.cantidad >= cantidad:
            self.saldo -= total
            producto.disminuir_inventario(cantidad)
            print(f"Compra exitosa: {cantidad}x {producto.nombre} por ${total}.")
        else:
            print(f"Saldo insuficiente o stock agotado.")

    def mostrar_informacion(self):
        print(f"Cliente: {self.nombre}, ID: {self.id_cliente}, Saldo: ${self.saldo}")


# Clase Tienda
class Tienda:
    def __init__(self):
        #Inicializa una tienda vacía con listas.
        self.productos = []  # Lista para almacenar productos
        self.clientes = []   # Lista para almacenar clientes

    def agregar_producto(self, producto): #Metodo para agregar un producto a la tienda.
        # Verificar si el producto ya existe por su ID
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                print(f"Error: Ya existe un producto con ID {producto.id_producto}.")
                return
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado.")

    def agregar_cliente(self, cliente): #Agregar un cliente a la tienda.
        # Verificar si el cliente ya existe por su ID
        if any(c.id_cliente == cliente.id_cliente for c in self.clientes):
            print(f"Error: Ya existe un cliente con ID {cliente.id_cliente}.")
        else:
            self.clientes.append(cliente)
            print(f"Cliente '{cliente.nombre}' agregado con éxito.")

    def realizar_venta(self, id_cliente, id_producto, cantidad): #Realizar una venta de un producto a un cliente.

        #Valida la existencia del cliente y del producto, y si es posible realiza la venta.
        # Validar que la cantidad sea un valor positivo
        if cantidad <= 0:
            print("Error: La cantidad debe ser mayor que cero.")
            return

        # Buscar el cliente por su ID
        cliente = next((c for c in self.clientes if c.id_cliente == id_cliente), None)

        # Buscar el producto por su ID
        producto = next((p for p in self.productos if p.id_producto == id_producto), None)

        # Validar existencia de cliente y producto
        if not cliente:
            print(f"Error: No se encontró un cliente con ID {id_cliente}.")
            return

        if not producto:
            print(f"Error: No se encontró un producto con ID {id_producto}.")
            return

        # Intentar realizar la compra
        cliente.realizar_compra(producto, cantidad)

    def mostrar_productos(self): #Muestra todos los productos disponibles en la tienda.
        if not self.productos:
            print("No hay productos disponibles.")
        else:
            print("\nProductos disponibles:")
            for producto in self.productos:
                producto.mostrar_informacion()

    def mostrar_clientes(self):
        #Muestra todos los clientes registrados en la tienda.
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            print("\nClientes registrados:")
            for cliente in self.clientes:
                cliente.mostrar_informacion()

    def guardar_datos(self, archivo):
        with open(archivo, "w") as f:
            # Guardar productos
            f.write("PRODUCTOS:\n")
            for producto in self.productos:
                f.write(f"{producto.nombre},{producto.id_producto},{producto.precio},{producto.cantidad}\n")

            # Guardar clientes
            f.write("CLIENTES:\n")
            for cliente in self.clientes:
                f.write(f"{cliente.nombre},{cliente.id_cliente},{cliente.saldo}\n")

        print(f"\nDatos guardados en '{archivo}'.")


    def cargar_datos(self, archivo):
        try:
            with open(archivo, "r") as f:
                lineas = f.readlines()

            modo = None
            for linea in lineas:
                linea = linea.strip()

                if linea == "PRODUCTOS:":
                    modo = "productos"
                    continue
                elif linea == "CLIENTES:":
                    modo = "clientes"
                    continue

                if modo == "productos":
                    nombre, id_producto, precio, cantidad = linea.split(",")
                    nuevo_producto = Producto(nombre, int(id_producto), float(precio), int(cantidad))
                    self.productos.append(nuevo_producto)

                elif modo == "clientes":
                    nombre, id_cliente, saldo = linea.split(",")
                    nuevo_cliente = Cliente(nombre, int(id_cliente), float(saldo))
                    self.clientes.append(nuevo_cliente)

            print(f"Datos cargados desde '{archivo}'.\n")

        except FileNotFoundError:
            print(f"Error: El archivo '{archivo}' no existe.")

            print(f"Datos cargados desde '{archivo}'.")
        except FileNotFoundError:
            print(f"Error: El archivo '{archivo}' no existe.")


# Cargar los datos
tienda = Tienda()
tienda.cargar_datos("datos_tienda.txt")

# Agregar productos y clientes
tienda.realizar_venta(102,3,1)

# Guardar en el archivo
tienda.guardar_datos("datos_tienda.txt")

# Mostrar productos y clientes
tienda.mostrar_productos()
tienda.mostrar_clientes()