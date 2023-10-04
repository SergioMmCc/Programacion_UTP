/* 3. Dado el radio de una circunferencia se pide calcular e imprimir su area
Area = pi* (r al cuadrado)*/

#include <stdio.h>
#include <math.h>

int main ()
{
   float r, area;
   
   //Entradas
   printf ("Ingrese el radio de la circunferencia : ");
   scanf ("%f", &r);
   //Proceso
    area=M_PI*pow(r,2);
    //salida
    printf ("El area de la circunferencia es : %f \n",area);
    
    return 0;
}
