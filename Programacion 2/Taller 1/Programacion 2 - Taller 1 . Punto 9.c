/* 9. En una planta se realizan 3 mediciones de temperatura de una
caldera (oC): a las 6 AM, a las 2 PM  y a las 10 PM. Determinar cuando
se dio la mayor (mañana, tarde o noche) */

#include <stdio.h>

int main ()
{
    float t1, t2, t3;
    
    /* Entradas */
    printf("Ingrese la temperatura de la caldera a las 6 AM: ");
    scanf("%f", &t1);
    printf("Ingrese la temperatura de la caldera a las 2 PM: ");
    scanf("%f", &t2);
    printf("Ingrese la temperatura de la caldera a las 10 PM: ");
    scanf("%f", &t3);
    
    /* Proceso */
    if (t1 >= t2 && t1 >= t3)
    {
        printf("La mayor temperatura (%f) se dio en la mañana", t1);
    }
    else
    {
        if (t2 > t1 && t2> t3)
        {
            printf("La mayor temperatura (%f) se dio en la tarde", t2);
        }
        else
        {
            if (t3 > t1 && t3 > t2)
            {
                printf("La mayor temperatura (%f) se dio en la noche", t3);
            }
        }
    }
}
