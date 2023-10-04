/* 5. Dado los valore A, B, C se pide calcular y mostrar dichos resultados

- El cuadrado de la suma
- El producto de los valores leidos
- El cubo del producto
- La diferencia entre el cuadrado de la suma con rexspecto al cubo del producto
*/

#include <stdio.h>
#include <math.h>

int main()
{
    int A, B, C, suma_cuadrado, producto, cubo_producto, diferencia;
    //Entradas
    printf ("Ingrese A: ");
    scanf ("%d", &A);
    printf ("Ingrese B: ");
    scanf ("%d", &B);
    printf ("Ingrese C: ");
    scanf ("%d", &C);
    //Procesos
    suma_cuadrado=pow(A+B+C,2);
    producto=A*B*C;
    cubo_producto=pow(producto,3);
    diferencia=(suma_cuadrado-cubo_producto);
    //salidas
    printf ("Cuadrado de la suma : %d \n",suma_cuadrado);
    printf ("Producto de los valores : %d \n",producto);
    printf ("Cubo del producto : %d \n",cubo_producto);
    printf ("Diferencia del cuadrado de la suma con respectpo al cubo del producto : %d \n",diferencia);

    return 0;
}
