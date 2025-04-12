import tkinter as tk

def mostrar_nombre():
    nombre = entry.get()  # Obtener el texto del Entry
    label.config(text=f"¡Hola, {nombre}!")

def cambiar_color_fondo():
    label.config(bg="blue")

def cambiar_color_letra():
    label.config(fg="red")

ventana = tk.Tk()
ventana.title("Interfaz de Usuario")
ventana.geometry("400x400")

# Etiqueta
label = tk.Label(ventana, text="Introduce tu nombre:", font=("Times New Roman", 16), fg="gray")
label.pack()

# Campo de entrada (Entry)
# tk.Entry crea un campo de texto
entry = tk.Entry(ventana)
entry.pack()

# Botón para mostrar el saludo
boton_saludar = tk.Button(ventana, text="Saludar", command=mostrar_nombre, font=("Times New Roman", 16), fg="gray")
boton_saludar.pack()

# Boton para cambiar el color de fondo
boton_cambiar_fondo = tk.Button(ventana, text="Cambiar color de fondo", comman=cambiar_color_fondo, font=("Times New Roman", 16), fg="gray")
boton_cambiar_fondo.pack()

# Boton para cambiar el color de la letra
boton_cambiar_letra = tk.Button(ventana, text="Cambiar color de letra", comman=cambiar_color_letra, font=("Times New Roman", 16), fg="gray")
boton_cambiar_letra.pack()

ventana.mainloop()
