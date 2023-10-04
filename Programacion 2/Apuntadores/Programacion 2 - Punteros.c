// Taller Vectores

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 1) Realice una función sqr(&n) que reciba una dirección a un numero entero,
	  eleve el numero al cuadrado y deje el resultado en el mismo número. */

float own_sqrt (float *num)
{
    if (num == 0 || num == 1) {
        return *num;
    }

    float aprox = *num;
    float epsilon = 0.000001; // Precisión deseada

    while ((aprox - *num / aprox) > epsilon)
	{
        aprox = (aprox + *num / aprox) / 2;
    }

    return aprox;
}
//--------------------------------------------------------------------------
/* 2) Elabore una funcion que reciba dos variables puntero y con ellas
	  calcule la potencia entre esos dos numeros */
	  
long Potencia (long *x, long *y)
{
	long p=1;
	long i=1;
	while (i<=*y)
	{
		p=p* *x;
		i++;
	}
	return p;
}
//--------------------------------------------------------------------------
/* 3) Elabore una funcion que reciba en una variable puntero la primera
	  posicion de los datos de un vcetor y el numero de datos. La funcion
	  debe retornar la suma de los elementos del vector */
	
int SumaV (int *v, int t)
{
	int i;
	int s=0;
	for (i=0; i<t; i++)
	{
		s= s+ *(v+i);
	}
	return s;
}
//--------------------------------------------------------------------------
/* 4) Elaborar un procedimiento que reciba un vector y el numero de datos
	  de datos de dicho vector. El procedimiento debe imprimir los datos
	  del vector */
	  
void PrintVector (int *v, int t)
{
	int i;
	printf ("[");
	for (i=0; i<t; i++)
	{
		printf ("%d ", *(v+i));
	}
	printf ("]");
}
//--------------------------------------------------------------------------
/* 6) Escriba una función str_busca(str, c) que reciba un apuntador a una
	  cadena de caracteres str, y un carácter c. Busque el carácter en la
	  cadena y regrese la posición en que se encuentra el carácter en la 
	  cadena o un -1 si no se encuentra utilizando apuntadores. */
	  
int str_busca (char *str, char c)
{
	int i, cont=0;
	for (i=0; *(str+i)!='\0'; i++)
	{
		if (*(str+i)==c)
		{
			cont++;
			return i;
			break;
		}
	}
	if (cont==0)
	{
		return (-1);
	}
}
//--------------------------------------------------------------------------
 
int main()
{
    float x, y;
    printf ("Ingrese un numero: ");
    scanf ("%f", &x);
    y=own_sqrt (&x);
    printf ("%.2f\n\n", y);
    
	long x1, y1;
    x1=2;
    y1=13;
    printf ("%d ^ %d = %d\n\n", x1, y1, Potencia (&x1, &y1));
    
    int d[5]={4, 10, 2, 3, 5};
    printf ("%d\n\n", SumaV(d, 5));
    PrintVector (d, 5);
    
    char cad [10];
    int b;
    strcpy (cad, "esternocleidomastoideo");
    b=str_busca (cad, 'd');
    printf ("\n\n%d\n\n", b);
}
