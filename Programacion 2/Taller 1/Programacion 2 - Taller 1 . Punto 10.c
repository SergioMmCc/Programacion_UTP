/* 10. Leer un numero entero de 2 digitos y mostrar si un digito es multiplo del otro */

#include <stdio.h>

int main ()
{
    int a, d1, d2;
    
    /* Entrada */
    printf("Ingrese un numero de 2 digitos: ");
    scanf("%d", &a);
    
    /* Proceso */
    if (a<0)
    {
        printf("Por favor ingrese un numero positivo");
    }
    else
    {
        if ((a>99) || (a<10))
        {
            printf("El numero que ingreso no es de 2 digitos");
        }
        else
        {
            d1=a/10;
            d2=a%10;
            if (d1%d2==0)
            {
                printf("El primer digito de %d (%d) es multiplo de su segundo digito (%d)", a, d1, d2);
            }
            else
            {
                if (d2%d1==0)
                {
                    printf("El segundo digito de %d (%d) es multiplo de su primer digito (%d)", a, d2, d1);
                }
                else
                {
                    printf("Ninguno de los digitos de %d es multiplo del otro", a);
                }
            }
        }
    }
    
    return 0;
}
