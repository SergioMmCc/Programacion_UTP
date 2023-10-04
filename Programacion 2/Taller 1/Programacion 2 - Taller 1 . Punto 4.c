/* 4. Dada la temperatura en grados Fahrenheit (f) convertirla a grados
centigrados (c)
c = 0,55 * (f-32) */

#include <stdio.h>
#include <math.h>

int main ()
{
   float f, c;
   
   //Entradas
   printf ("Ingrese la temperatura : ");
   scanf ("%f", &f);
   //Proceso
   c=0.55*(f-32);
   //Salida
   printf ("La temperatura en grados centigrados es : %f \n", c);
    
    return 0;
    
}
