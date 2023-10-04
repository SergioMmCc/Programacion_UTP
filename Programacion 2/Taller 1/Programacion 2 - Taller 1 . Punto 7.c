/* 7. Leer un numero entero y si es multiplo de 4 mostrar en pantalla su mitad,
si es multiplo de 5 mostrar en pantalla su cuadrado y si es multiplo de 6
mostrar en pantalla su cubo. Validar que el numero no sea mayor que 100 */

#include <stdio.h>
#include <math.h>

int main ()
{
    int a, resultado;
    
    /* Entrada */
   printf("Ingrese un numero (que no sea mayor que 100): ");
   scanf("%d", &a);
   /* Proceso */
   if (a>100)
   {
       printf("El numero que ingreso es mayor que 100");
   }
   else
   {
       if (a%4 == 0)
       {
           resultado = a/2;
           printf("La mitad de %d es %d", a, resultado);
       }
       else
       {
           if (a%5 == 0)
           {
               resultado = pow(a,2);
               printf("El cuadrado de %d es %d", a, resultado);
           }
           else
           {
               if (a%6 == 0)
               {
                   resultado = pow(a,3);
                   printf("El cubo de %d es %d", a, resultado);
               }
               else
               {
                   printf("El numero que ingreso no es multiplo de 4, 5 ni 6");
               }
           }
       }
   }
   
   return 0;
}
