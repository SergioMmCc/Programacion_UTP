import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk() # cuando queramos mostrar un elemento dentro de ventana, tendremos que poner "ventana" como primer parametro

# Configurar el título de la ventana
ventana.title("Interfaz Gráfica")

# Configurar el tamaño de la ventana
ventana.geometry("400x300")

# Función que se ejecutará cuando se presione el botón
def saludar():
    label1.config(text="¡Hola, Mundo!")

# Crear un botón y asignarle la función saludar
# tk.button crea un boton
boton = tk.Button(ventana, text="Haz clic", command=saludar, font=("Arial", 16), bg="red")
boton.pack()
# command se utiliza para asignarle al boton una funcion que se ejecutara cuando este sea presionado

# Crear una etiqueta para mostrar el saludo
# tk.label crea una etiqueta para mostrar un texto
label1 = tk.Label(ventana, text="Haz click arriba para ver el mensaje", font=("Times New Roman", 16), fg="red", bg="blue")
label1.pack()

# Etiquetas para explicar algunas de las cosas que podemos hacer
label2 = tk.Label(ventana, text="Usamos text para mostrat texto")
label2.pack()
label3 = tk.Label(ventana, text="Usamos fg para darle color al texto y bg para darle color al fondo", fg="green", bg="orange")
label3.pack()
label4 = tk.Label(ventana, text="Usamos font para definir un estilo para el texto y su tamaño", font=("Helvetica", 10))
label4.pack()
label5 = tk.Label(ventana, text="Usamos .pack() para mostrar el componente en la ventana")
label5.pack()

# Iniciar el bucle de la interfaz gráfica, mantiene la ventana abierta y permite interactuar con los elementos
ventana.mainloop()
