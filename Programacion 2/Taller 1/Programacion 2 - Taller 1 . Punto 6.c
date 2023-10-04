/* 6. Lea tres numeros y escriba un mensaje si los datos se escribieron en
forma ordenada (ya sea descendente o ascendentemente) y si no es asi que
muestre el respectivo mensaje */

#include <stdio.h>

int main ()
{
    float a, b, c;
    
    //Entradas
    printf("Ingrese el primer numero: ");
    scanf("%f", &a);
    printf("Ingrese el segundo numero: ");
    scanf("%f", &b);
    printf("Ingrese el tercer numero: ");
    scanf("%f", &c);
    
    //Proceso
    if (a>b && b>c)
    {
    printf("Los datos se escribieron de forma ordenada descendentemente");
    }
    else
    {
        if (a<b && b<c)
        {
        printf("Los datos se escribieron de forma ordenada ascendentemente");
        }
        else
        {
        printf("Los datos no se escribieron de forma ordenada");
        }
    }
    
    return 0;
}
