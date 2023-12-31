// Taller for

#include <stdio.h>

/* 1) Implementar un algoritmo que muestre todos los m�ltiplos de 7
comprendidos entre 1 y 1000. */

void multiplos7 ()
{
	int i;
	for (i=1; i<=1000; i++)
	{
		if (i%7==0)
		{
			printf ("%d ", i);
		}
	}
}

/* 2) Implementar un algoritmo que calcule la siguiente suma:
3(1)+3(2)+3(3)+3(4)+�..+3(n), ingresar n por teclado mostrar el
resultado de dicha suma. */

int suma (int n)
{
	int i, r;
	for (i=1; i<=n; i++)
	{
		r=r+(3*i);
	}
	return r;
}

/* 3) Leer por teclado cuatro notas de un estudiante en una sola
variable, cada vez el acumulado se debe guardar en una variable
llamada total. Cuando se lean las cuatro determinar el promedio,
si el promedio es mayor o igual a tres, imprimir �ganaste� de lo
contrario imprimir �perdiste�. */

void notas ()
{
	int n;
	float total, nota;
	for (n=0; n<4; n++)
	{
		printf ("Ingrese la nota: ");
		scanf("%f",&nota);
		total=total+nota;
	}
	if (total/4>=3.0)
	{
		printf ("Ganaste");
	}
	else
	{
		printf ("Perdiste");
	}
}

/* 4) Un entero positivo n se llama perfecto si n es igual a la suma de
todos sus divisores diferentes de �l. Por ejemplo, 6 es perfecto porque
6 = 1 + 2 + 3. Escriba un programa que lea por teclado un n�mero entero
positivo, y nos indique si �ste es perfecto o no. Adem�s, el programa debe
imprimir todos los divisores del n�mero. */

void perfecto (int n)
{
	int i, r;
	r=0;
	printf ("Los divisores de %d son: ", n);
	for (i=1; i<n; i++)
	{
		if (n%i==0)
		{
			printf ("%d ", i);
			r=r+i;
		}
	}
	if (r==n)
	{
		printf ("\n%d es un numero perfecto\n", n);
	}
	else
	{
		printf ("\n%d no es un  numero perfecto\n", n);
	}
}

//------------------------------------------------------------------------

/* 5) Leer dos n�meros enteros por teclado y determinar si �stos son n�meros
amigos(Dos n�meros amigos son dos enteros positivos a y b tales que a es la
suma de los divisores propios de b, y b es la suma de los divisores propios
de a. la unidad se considera divisor propio, pero no lo es el mismo n�mero). */

void amigos (int a, int b)
{
	int r1, r2, i1, i2;
	r1=0;
	r2=0;
	for (i1=1; i1<a; i1++)
	{
		if (a%i1==0)
		{
			r1=r1+i1;
		}
	}
	for (i2=1; i2<b; i2++)
	{
		if (b%i2==0)
		{
			r2=r2+i2;
		}
	}
	if (r2==a && r1==b)
	{
		printf ("%d y %d son numeros amigos\n", a, b);
	}
	else
	{
		printf("%d y %d no son numeros amigos\n", a, b);
	}
}

//------------------------------------------------------------------------

/* 6) Leer un n�mero entero positivo n por teclado y mostrar por pantalla
la secuencia de fibonacci con n terminos.(ejemplo: si se lee un 3 se debe
mostrar la serie hasta el tercer n�mero 1,1,2. Si se lee un 5, se debe mostrar
la serie hasta el quinto n�mero 1,1,2,3,5). */

int fibonacci (int n)
{
	int aux, aux2, aux3, i;
	aux=1;
	aux2=1;
	for (i=1; i<=n; i++)
	{
		printf ("%d ", aux);
		aux3=aux;
		aux=aux2;
		aux2=aux3+aux2;
	}
}

//------------------------------------------------------------------------

/* 7) Leer un entero n por teclado y calcular su factorial, n!=1*2*3*4*....*n. */

void factorial (int n)
{
	int i, r;
	r=1;
	for (i=1; i<=n; i++)
	{
		r=r*i;
	}
	printf ("El factorial de %d es %d\n", n, r);
}

//------------------------------------------------------------------------

/* 8) Implementar un algoritmo que diga cuantos n�meros perfectos hay entre 1 y 1000. */

void contador ()
{
	int i, cont, n, r;
	cont=0;
	for (i=1; i<=1000; i++)
	{
		r=0;
		for (n=1; n<i; n++)
		{
			if (i%n==0)
			{
				r=r+n;
			}
		}
		if (r==i)
			cont=cont+1;
	}
	printf ("Entre 1 y 1000 hay %d numeros perfectos\n", cont);
}

//------------------------------------------------------------------------

/* 9) Implementar un algoritmo que diga cuales n�meros primos hay entre 1 y 1000
(debe mostrar los numeros) */

void primos ()
{
	int i, n, cont;
	for (i=2; i<=1000; i++)
	{
		cont=0;
		for (n=2; n<i; n++)
		{
			if (i%n==0)
				cont=cont+1;
		}
		if (cont==0)
			printf ("%d ", i);
	}
}

//------------------------------------------------------------------------

/* 10) Hacer un programa que muestre los factoriales de los primeros 10 enteros */

void factorial2 ()
{
	int i, n, r;
	for (n=1; n<=10; n++)
	{
		r=1;
		for (i=1; i<=n; i++)
		{
			r=r*i;
		}
		printf ("Factorial de %d: %d\n", n, r);
	}
}

//------------------------------------------------------------------------

/* 11) Implementar las tablas de multiplicar del 10 al 20. */

void tablas ()
{
	int i, n, r;
	for (n=10; n<=20; n++)
	{
		for (i=1; i<=10; i++)
		{
			r=n*i;
			printf ("%d * %d = %d\n", n, i, r);
		}
		putchar ('\n');
	}
}

//------------------------------------------------------------------------

main ()
{
	int a, b, n, r;
	// multiplos7 ();
	/* printf("Ingrese el numero hasta el que desea calcular la sumatoria: ");
	scanf ("%d", &n);
	r=suma (n);
	printf("El resultado de la sumatoria es %d", r); */
	// notas ();
	// perfecto (28);
	/* printf ("Ingrese el primer numero: ");
	scanf("%d", &a);
	printf("Ingrese el segundo numero: ");
	scanf("%d", &b);
	amigos (a, b); */
	/* printf ("Ingrese el numero hasta el que desea calcular fibonacci: ");
	scanf("%d",&n);
	fibonacci (n); */
	// factorial (6);
	// contador ();
	// primos ();
	// factorial2 ();
	// tablas ();
}
