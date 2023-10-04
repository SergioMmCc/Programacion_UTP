#include <stdio.h>

void saludo ()
{
	int i, n;
	i=0;
	printf("Ingrese la cantidad de veces que desea imprimir hola: ");
	scanf("%d",&n);
	while (i<n)
	{
		printf ("Hola\n");
		i=i+1;
	}
}

int factorial (int n)
{
	int r;
	r=1;
	while (n>0)
	{
		r=r*n;
		n=n-1;
	}
	return (r);
}

void numeros (int n)
{
	int r;
	r=1;
	while (r<=n)
	{
		printf ("%d ", r);
		r=r+1;
	}
}

void multiplos7 ()
{
	int i;
	i=1;
	while (i<=1000)
	{
		if (i%7==0)
		{
			printf ("%d ", i);
		}
		i=i+1;
	}
}

int suma (int n)
{
	int i, r;
	i=1;
	while (i<=n)
	{
		r=r+(3*i);
		i=i+1;
	}
	return r;
}

main ()
{
	int r, n;
	// saludo ();
	/* r=factorial (5);
	printf("%d",r); */
	// numeros (10);
	// multiplos7 ();
	printf("Ingrese el numero hasta el que desea calcular la sumatoria: ");
	scanf ("%d", &n);
	r=suma (n);
	printf("El resultado de la sumatoria es %d", r);
}

