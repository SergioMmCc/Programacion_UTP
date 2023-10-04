//Taller vectores y matrices

#include <stdio.h>
#include <stdlib.h>

/* 1) Hacer una función que reciba un entero N y devuelva
un vector de tamaño N, con enteros leídos por teclado. */

void vectorn (int n)
{
	int i;
	int vector [n];
	for (i=0; i<n; i++)
	{
		printf ("Ingrese un numero: ");
		scanf ("%d", &vector[i]);
	}
	for (i=0; i<n; i++)
	{
		printf ("%d ", vector[i]);
	}
	putchar ('\n');
}
//-------------------------------------------------------
/* 2) Hacer lo mismo que en el punto anterior, pero
generando los datos aleatoriamente. */

void vectorr (int n)
{
	int i;
	int vector [n];
	for (i=0; i<n; i++)
	{
		vector [i] = rand ();
	}
	for (i=0; i<n; i++)
	{
		printf ("%d ", vector[i]);
	}
	putchar ('\n');
}
//-------------------------------------------------------
/* 3) Dado un vector de enteros y un número X, devolver
el numero de veces que está X en el vector. */

void contar (int n, int x)
{
	int i, cont;
	cont=0;
	int vector [n];
	for (i=0; i<n; i++)
	{
		printf ("Ingrese un numero: ");
		scanf ("%d", &vector[i]);
	}
	for (i=0; i<n; i++)
	{
		if (vector [i]==x)
		{
			cont++;
		}
	}
	printf ("%d se encuentra %d veces en el vector\n", x, cont);
}
//-------------------------------------------------------
/* 4) Dada un vector, hacer una función que invierta sus
datos en el mismo y lo devuelva invertido. */

void invertir (int n)
{
	int i, j, x;
	j=n-1;
	int vector [n];
	for (i=0; i<n; i++)
	{
		printf ("Ingrese un numero: ");
		scanf ("%d", &vector[i]);
	}
	for (i=0; i<(n/2); i++)
	{
		x=vector [j];
		vector [j]=vector[i];
		vector [i]=x;
		j--;
	}
	for (i=0; i<n; i++)
	{
		printf ("%d ", vector [i]);
	}
}
//-------------------------------------------------------
/* 5) Hacer una función que reciba un vector, y devuelva
una copia en otra estructura similar. */

void copia (int n)
{
	int i;
	int vector [n];
	int vector2 [n];
	for (i=0; i<n; i++)
	{
		printf ("Ingrese un numero: ");
		scanf ("%d", &vector[i]);
	}
	for (i=0; i<n; i++)
	{
		vector2[i]=vector[i];
	}
	for (i=0; i<n; i++)
	{
		printf ("%d ", vector[i]);
	}
}
//-------------------------------------------------------
/* 6) Hacer una función que reciba un vector de enteros
y devuelva el promedio de los datos existentes. */

void promedio (int n)
{
	int i;
	float s, r;
	s=0;
	int vector [n];
	for (i=0; i<n; i++)
	{
		printf ("Ingrese un numero: ");
		scanf ("%d", &vector[i]);
		s=s+vector[i];
	}
	r=s/n;
	printf ("El promedio de los datos del vector es %f\n", r);
}
//-------------------------------------------------------
/* 7) Hacer una función que reciba un vector de enteros
y devuelva la posición del mayor valor de los datos
existentes. */

void mayor (int n)
{
	int i, pos, x, z;
	pos=0;
	int vector [n];
	for (i=0; i<n; i++)
	{
		printf ("Ingrese un numero: ");
		scanf ("%d", &vector[i]);
	}
	z=vector[0];
	for (i=0; i<n-1; i++)
	{
		x=vector[i+1];
		if (x>z)
		{
			z=x;
			pos=i+1;
		}
	}
	printf ("El valor mayor se encuentra en la posicion %d\n", pos);
}
//-------------------------------------------------------
/* 8) Hacer una función que reciba un vector de enteros
e indique si está ordenado ascendentemente. */

void orden (int n)
{
	int i, error;
	error=0;
	int vector [n];
	for (i=0; i<n; i++)
	{
		printf ("Ingrese un numero: ");
		scanf ("%d", &vector[i]);
	}
	for (i=0; i<n-1; i++)
	{
		if (vector[i]>vector[i+1])
		{
			error++;
			break;
		}
	}
	if (error==0)
	{
		printf ("El vector esta ordenado ascendentemente\n");
	}
	else
	{
		printf ("El vector no esta ordenado ascendentemente\n");
	}
}
//-------------------------------------------------------
void menu ()
{
	int op, n, x;
	system ("cls");
	printf ("Ingrese 1 para crear un vector de longitud n\n");
	printf ("Ingrese 2 para crear un vector con numeros aleatorios\n");
	printf ("Ingrese 3 para ver cuantas veces se encuentra en un numero en un vector\n");
	printf ("Ingrese 4 para invertir un vector\n");
	printf ("Ingrese 5 para copiar un vector en otro\n");
	printf ("Ingrese 6 para hallar el promedio de los datos de un vector\n");
	printf ("Ingrese 7 para averiguar la posicion del valor mayor de un vector\n");
	printf ("Ingrese 8 para averiguar si un vector esta ordenado ascendentemente\n");
	printf ("Ingrese 9 para salir\n");
	printf ("Ingrese la opcion que desea: ");
	scanf ("%d", &op);
	
	if (op==1)
	{
		printf ("Ingrese la longitud del vector: ");
		scanf ("%d", &n);
		vectorn (n);
		system ("pause");
		menu ();
	}
	if (op==2)
	{
		printf ("Ingrese la longitud del vector: ");
		scanf ("%d", &n);
		vectorr (n);
		system ("pause");
		menu ();
	}
	if (op==3)
	{
		printf ("Ingrese la longitud del vector: ");
		scanf ("%d", &n);
		printf ("Ingrese el numero que desea saber cuantas veces se encuentra en el vector: ");
		scanf ("%d", &x);
		contar (n, x);
		system ("pause");
		menu ();
	}
	if (op==4)
	{
		printf ("Ingrese la longitud del vector: ");
		scanf ("%d", &n);
		invertir (n);
		putchar ('\n');
		system ("pause");
		menu ();
	}
	if (op==5)
	{
		printf ("Ingrese la longitud del vector: ");
		scanf ("%d", &n);
		copia (n);
		putchar ('\n');
		system ("pause");
		menu ();
	}
	if (op==6)
	{
		printf ("Ingrese la longitud del vector: ");
		scanf ("%d", &n);
		promedio (n);
		system ("pause");
		menu ();
	}
	if (op==7)
	{
		printf ("Ingrese la longitud del vector: ");
		scanf ("%d", &n);
		mayor (n);
		system ("pause");
		menu ();
	}
	if (op==8)
	{
		printf ("Ingrese la longitud del vector: ");
		scanf ("%d", &n);
		orden (n);
		system ("pause");
		menu ();
	}
}
//--------------------------------------------------------
int main ()
{
	menu ();
}
