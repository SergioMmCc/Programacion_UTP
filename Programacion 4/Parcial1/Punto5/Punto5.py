# Implementar el algoritmo de cifrado y descifrado cesar haciendo uso de
# POO, archivos y listas. Solo minúsculas.

# Importamos la libreria para trabajar con archivos
import os

# Clase Cesar
class Cesar:
    # Constructor
    def __init__(self):
        # Atributos
        self.abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                           'u', 'v', 'w', 'x', 'y', 'z']
        self.cifrado = ''
        self.descifrado = ''
        self.texto = ''
        self.desplazamiento = 0

    # Metodo para cifrar
    def cifrar(self, texto, desplazamiento):
        # Guardamos el texto y el desplazamiento
        self.texto = texto
        self.desplazamiento = desplazamiento
        self.cifrado = ''
        
        # Recorremos el texto
        for letra in self.texto:
            # Si la letra es un espacio
            if letra == ' ':
                # Agregamos un espacio
                self.cifrado += ' '
            else:
                # Obtenemos la posicion de la letra
                posicion = self.abecedario.index(letra)
                # Calculamos la nueva posicion
                nueva_posicion = (posicion - self.desplazamiento + 26) % 26
                # Agregamos la letra cifrada
                self.cifrado += self.abecedario[nueva_posicion]
        
        # Retornamos la cadena cifrada
        return self.cifrado


    # Metodo para descifrar
    def descifrar(self, texto, desplazamiento):
        # Guardamos el texto y el desplazamiento
        self.texto = texto
        self.desplazamiento = desplazamiento
        self.descifrado = ''
        
        # Recorremos el texto
        for letra in self.texto:
            # Si la letra es un espacio
            if letra == ' ':
                # Agregamos un espacio
                self.descifrado += ' '
            else:
                # Obtenemos la posicion de la letra
                posicion = self.abecedario.index(letra)
                # Calculamos la nueva posicion
                nueva_posicion = (posicion + self.desplazamiento) % 26
                # Agregamos la letra descifrada
                self.descifrado += self.abecedario[nueva_posicion]
        
        # Retornamos la cadena descifrada
        return self.descifrado
    

    # Metodo para guardar el texto cifrado en un archivo
    def guardar_cifrado(self, cifrado):
        # Abrimos el archivo en modo escritura
        with open('cifrado.txt', 'a') as archivo:
            # Escribimos el texto cifrado
            archivo.write(cifrado)
            archivo.write('\n')
        # Mostramos un mensaje
        print('Texto cifrado guardado en cifrado.txt')


# Funcion principal
def main():
    os.system('cls' if os.name == 'nt' else 'clear') # Limpiar la consola
    # Creamos un objeto de la clase Cesar
    cesar = Cesar()
    
    while True:

        # Menú de opciones
        print('Cifrado y Descifrado Cesar')
        print('1. Cifrar')
        print('2. Descifrar')
        print('3. Salir')
        opcion = int(input('Seleccione una opción: '))

        # Si la opcion es 1
        if opcion == 1:
            # Solicitamos el texto a cifrar
            texto = input('Ingrese el texto a cifrar: ')
            # Solicitamos el desplazamiento
            desplazamiento = int(input('Ingrese el desplazamiento: '))
            # Ciframos el texto
            texto_cifrado = cesar.cifrar(texto, desplazamiento)
            # Mostramos el texto cifrado
            print('Texto cifrado:', texto_cifrado)
            # Guardamos el texto cifrado en un archivo
            cesar.guardar_cifrado(texto_cifrado)

        # Si la opcion es 2
        elif opcion == 2:
            # Solicitamos el texto a descifrar
            texto = input('Ingrese el texto a descifrar: ')
            # Solicitamos el desplazamiento
            desplazamiento = int(input('Ingrese el desplazamiento: '))
            
            # Desciframos el texto
            texto_descifrado = cesar.descifrar(texto, desplazamiento)
            
            # Mostramos el texto descifrado
            print('Texto descifrado:', texto_descifrado)

        # Si la opcion es 3
        elif opcion == 3:
            # Salimos del programa
            print('Saliendo del programa...')
            return

        # Si la opcion no es ninguna de las anteriores
        else:
            # Mostramos un mensaje de error
            print('Opción no válida')

        input("\nPresione Enter para continuar...") # Esperar a que el usuario presione Enter
        os.system('cls' if os.name == 'nt' else 'clear') # Limpiar la consola


# Llamamos a la funcion principal
main()