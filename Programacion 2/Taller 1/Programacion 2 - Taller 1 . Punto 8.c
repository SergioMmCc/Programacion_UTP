/* 8. Leer un numero entero positivo y determinar si es e 1, 2, 3 o 4 digitos */

#include <stdio.h>

int main ()
{
    int a;
    
    /* Entrada */
    printf("Ingrese un numero de maximo 4 digitos: ");
    scanf("%d", &a);
    
    /* Proceso */
    if (a<0)
	{
		printf("Por favor ingrese un numero positivo");
	}
	else
	{
    	if (a>9999)
    	{
       		printf ("El numero que ingreso tiene mas de 4 cifras");
    	}
    	else
    	{
        	if (a/1000 >= 1)
        	{
        		printf("El numero %d tiene 4 digitos", a);
        	}
        	else
        	{
            	if ((a/100 >= 1) || (a/100 <=-1))
            	{
                printf("El numero %d tiene 3 digitos", a);
            	}
            	else
            	{
                	if ((a/10 >= 1) || (a/10 <= -1))
                	{
                    printf("El numero %d tiene 2 digitos", a);
                	}
                	else
                	{
                    	if ((a/1 >= 1) || (a/1 <= -1) || (a==0))
                    	{
                        printf("El numero %d tiene 1 digito", a);
                    	}
                	}
            	}
        	}
    	}
	}
}
