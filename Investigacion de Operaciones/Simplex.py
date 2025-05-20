"""
Método Simplex para Maximización

Este programa implementa el algoritmo del método simplex para resolver
problemas de programación lineal de maximización con restricciones lineales
en forma estándar (desigualdades tipo ≤ y variables no negativas).

El algoritmo construye una tabla simplex, agrega variables de holgura
y realiza iteraciones para encontrar la solución óptima, si existe.

Limitaciones:
- Solo admite restricciones del tipo '≤'.
- Todas las variables deben ser no negativas.
- El problema debe tener solución acotada.

Cabe resaltar que la solución podrá tener como coeficientes números decimales,
es decir, no está limitada a entregar solo enteros.

Ejemplo de uso:
Maximizar Z = 3x + 5y
Sujeto a:
    2x + 3y ≤ 8
    2x +  y ≤ 6
    x, y ≥ 0

La solución óptima será:
    x = 0, y = 8/3, Z = 40/3 ≈ 13.33
"""

import numpy as np

def simplex(c, A, b):
    """
    Aplica el método simplex para resolver un problema de maximización.

    Parámetros:
    - c: array de coeficientes de la función objetivo (longitud n).
    - A: matriz de coeficientes de las restricciones (dimensión m x n).
    - b: array de términos independientes de las restricciones (longitud m).

    Retorna:
    - x: solución óptima (valores de las variables).
    - z: valor máximo de la función objetivo.
    """
    m, n = A.shape
    tableau = np.zeros((m + 1, n + m + 1))

    # Construcción del tableau
    tableau[:m, :n] = A                     # Coeficientes de variables originales
    tableau[:m, n:n + m] = np.eye(m)        # Variables de holgura
    tableau[:m, -1] = b                     # Lado derecho
    tableau[-1, :n] = -c                    # Función objetivo (negada)

    # Iteraciones del método simplex
    while True:
        col = np.argmin(tableau[-1, :-1])   # Buscar columna pivote (más negativa)
        if tableau[-1, col] >= 0:
            break  # Óptimo alcanzado

        # Determinar fila pivote (mínima razón)
        ratios = []
        for i in range(m):
            if tableau[i, col] > 0:
                ratios.append(tableau[i, -1] / tableau[i, col])
            else:
                ratios.append(np.inf)
        row = np.argmin(ratios)
        if ratios[row] == np.inf:
            raise Exception("Solución no acotada")

        # Operaciones para hacer el pivote igual a 1 y anular el resto de la columna
        pivot = tableau[row, col]
        tableau[row, :] /= pivot
        for i in range(m + 1):
            if i != row:
                tableau[i, :] -= tableau[i, col] * tableau[row, :]

    # Extraer solución
    x = np.zeros(n)
    for j in range(n):
        col = tableau[:m, j]
        if np.count_nonzero(col) == 1 and 1 in col:
            row = np.where(col == 1)[0][0]
            x[j] = tableau[row, -1]
    z = tableau[-1, -1]
    return x, z


def pedir_datos():
    """
    Solicita al usuario los datos necesarios para formular el problema:
    - número de variables
    - número de restricciones
    - coeficientes de la función objetivo
    - coeficientes y términos independientes de las restricciones

    Retorna:
    - c: array de coeficientes de la función objetivo
    - A: matriz de coeficientes de restricciones
    - b: array de términos independientes
    """
    n = int(input("Número de variables: "))
    m = int(input("Número de restricciones: "))

    print("\nIngrese los coeficientes de la función objetivo (Z = ...):")
    c = np.array([float(input(f"Coeficiente de x{i+1}: ")) for i in range(n)])

    A = []
    b = []
    print("\nIngrese los coeficientes de las restricciones (formato: a1 x1 + a2 x2 + ... ≤ b):")
    for i in range(m):
        print(f"\nRestricción {i+1}:")
        fila = [float(input(f"Coeficiente de x{j+1}: ")) for j in range(n)]
        A.append(fila)
        b_i = float(input("Término independiente (lado derecho): "))
        b.append(b_i)

    return c, np.array(A), np.array(b)


# Ejecución principal
if __name__ == "__main__":
    c, A, b = pedir_datos()
    sol, z_max = simplex(c, A, b)
    print("\nSolución óptima encontrada:")
    for i, val in enumerate(sol):
        print(f"x{i+1} = {val}")
    print(f"Z máximo = {z_max}")
