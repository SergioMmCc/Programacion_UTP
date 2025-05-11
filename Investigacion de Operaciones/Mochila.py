# Algoritmo para resolver el problema de la mochila, el cual consiste en 
# que tenemos n elementos con cieerto peso y cierto valor, una mochila 
# con cierta capacidad y queremos maximizar la suma del valor de los 
# elementos que ingresamos a la mochila, sin superar su capacidad.
# Utilizaremos programacion dinamica para resolver este ejercicio
# Complejidad O(n * capacidad)
def mochila():
    # Lectura de datos
    capacidad = int(input("Ingrese la capacidad de la mochila: "))
    n = int(input("Ingrese la cantidad de elementos disponibles: "))

    elementos = []
    for i in range(n):
        peso = int(input("Ingreso el peso del objeto: "))
        valor = int(input("Ingrese el valor del objeto: "))
        elementos.append((peso, valor))

    # Proceso
    # Inicializar la tabla
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]

    for i in range (1, n + 1):
        # Cargar los valores del elemento i-1 (ya que el arreglo de los elementos es 0-index mientras que el for es 0-index)
        pesoAux = elementos[i-1][0]
        valorAux = elementos[i-1][1]
        for j in range (1, capacidad + 1):
            dp[i][j] = dp[i-1][j] # Valor sin tomar el elemento i-1
            if j - pesoAux >= 0: # Si el peso del elemento i-1 es mayor que j saltamos
                # Comparar si es mejor tomar el elemento i-1 o no
                dp[i][j] = max(dp[i][j], dp[i-1][j - pesoAux] + valorAux)


    return dp[n][capacidad] # Retornamos el valor maximo de la mochila con toda su capacidad y tras analizar todos los elementos

print(f"El valor máximo de la mochila es: {mochila()}")