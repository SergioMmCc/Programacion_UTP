//Taller 3
// Funciones recursivas

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <stdbool.h>

/* 1) Hacer un procedimiento que muestre por pantalla
n veces el mensaje de texto “hola”. */

void hola (int n)
{
	if (n>0)
	{
		printf("Hola\n");
		hola (n-1);
	}
}

//-------------------------------------------------

/* 2) Hacer un procedimiento que escriba los primeros
N números enteros. */

void num (int i, int n)
{
	if (i<=n)
	{
		printf("%d ",i);
		num (i+1,n);
	}
}

//----------------------------------------------

/* 3) Hacer un procedimiento que muestre la tabla de
multiplicar de un número N. */

void tabla (int n, int aux)
{
	int r;
	if (aux<11)
	{
		r=n*aux;
		printf("%d * %d = %d\n",n,aux,r);
		tabla(n,aux+1);
	}
}

//----------------------------------------------

/* 4) Hacer un procedimiento que imprima las tablas
de multiplicar desde 1 hasta N. */

void tablas (int i, int n, int aux)
{
	int r;
	if(i<=n)
	{
		if (aux<11)
		{
			r=i*aux;
			printf("%d * %d = %d\n",i,aux,r);
			tablas(i,n,aux+1);
		}
		if(aux>10)
		{
			printf("\n");
			tablas(i+1,n,aux-11);
		}
	}
}

//----------------------------------------------

/* 5) Hacer una función que devuelva la sumatoria
para los números enteros hasta N. */

int sum (int n)
{
	int r;
	if (n>0)
	{
		r=n+sum(n-1);
	}
}

//----------------------------------------------

/* 6) Hacer una función que devuelva el factorial
de un número x. */

int fact (int n)
{
	int r=1;
	if (n>0)
	{
		r=n*fact(n-1);
	}
	return r;
}

//----------------------------------------------

/* 7) Hacer una función que devuelva la sumatoria
de los números dados por la expresión x^x. Para todos
los números entre 1 y n. */

long sumpot (int n)
{
	long r;
	if (n>0)
	{
		r=pow(n,n)+sumpot(n-1);
	}
	return r;
}

//----------------------------------------------

/* 8) Implementar una función que eleve un número
x a la y (siendo y un entero positivo). */

long pot (int x, int y)
{
	long r=1;
	if (y>0)
	{
		r=x*pot(x,y-1);
	}
	return r;
}

//----------------------------------------------

/* 9) Hacer un procedimiento que muestre por
pantalla los submúltiplos de x (entero positivo). */

void divi (int n, int aux)
{
	if (aux<=n)
	{
		if (n%aux==0)
		{
			printf("%d ", aux);
		}
		divi (n, aux+1);
	}
}

//----------------------------------------------

/* 10) Hacer una función booleana que indique si un
número es primo o no. */

bool primo (int n, int aux)
{
	if (aux<n)
	{
		if (n%aux==0)
		{
			return false;
		}
		else
		{
			primo (n,aux+1);
		}
	}
	else
	{
		return true;
	}
}

//----------------------------------------------

/* 11) Hacer una función que devuelva el n-ésimo
número de la serie de Fibonacci. */

int fibonacci (int n, int cont, int aux, int aux2)
{	
	if (cont==n)
	{
		return aux;
	}
	else
	{
		fibonacci (n, cont+1, aux2, aux+aux2);
	}
}

//----------------------------------------------

/* 12) Hacer un procedimiento que muestre por pantalla
los n primeros números de la serie de fibonacci. */

void fibo (int n, int cont, int aux, int aux2)
{
	if (cont<n)
	{
		printf("%d ", aux);
		fibo (n, cont+1, aux2, aux+aux2);
	}
}

//----------------------------------------------

/* 13) Hacer una función que encuentre y devuelva el
mínimo común múltiplo de dos números a y b
(enteros positivos). */

int mcm (int a, int b, int aux)
{
	if ((aux%a==0) && (aux%b==0))
	{
		return aux;
	}
	else
	{
		mcm (a, b, aux+1);
	}
}

//----------------------------------------------

/* 14) Hacer una función que encuentre y retorne
el máximo común divisor entre dos números a y b
(enteros positivos). */

int mcd (int a, int b, int aux)
{
	if (aux>0)
	{
		if ((a%aux==0) && (b%aux==0))
		{
			return aux;
		}
		else
		{
			mcd (a, b, aux-1);
		}
	}
}

//----------------------------------------------

void menu ()
{
	int op, n, x, b, e, a;
	long y;
	system("cls");
	printf("Ingrese 1 para imprimir Hola n veces\n");
	printf("Ingrese 2 para imprimir los primero n numeros enteros\n");
	printf("Ingrese 3 para tabla de multiplicar de un numero\n");
	printf("Ingrese 4 para tablas de multiplicar desde 1 hasta n\n");
	printf("Ingrese 5 para sumatoria de los enteros hasta n\n");
	printf("Ingrese 6 para el factorial de un numero\n");
	printf("Ingrese 7 para la sumatoria de x^x\n");
	printf("Ingrese 8 para la potencia de un numero\n");
	printf("Ingrese 9 para averiguar los divisores de un numero\n");
	printf("Ingrese 10 para averiguar si un numero es primo\n");
	printf("Ingrese 11 para el enesimo termino de fibonacci\n");
	printf("Ingrese 12 para imprimir fibonacci hasta n\n");
	printf("Ingrese 13 para averiguar el minimo comun multiplo de dos numeros\n");
	printf("Ingrese 14 para averiguar el maximo comun divisior de dos numeros\n");
	printf("Ingrese 15 para salir\n");
	printf("Ingrese la opcion que desea (1-14): ");
	scanf("%d",&op);
	
	if (op==1)
	{
		printf("Ingrese la cantidad de veces que desea imprimir hola: ");
		scanf("%d",&n);
		hola (n);
		system("pause");
		menu();
	}
	if (op==2)
	{
		printf("Ingrese el numero hasta el que desea escribir: ");
		scanf("%d",&n);
		num (1, n);
		system("pause");
		menu();
	}
	if (op==3)
	{
		printf("Ingrese el numero cuya tabla de multiplicar desea conocer: ");
		scanf("%d",&n);
		tabla (n, 1);
		system("pause");
		menu();
	}
	if(op==4)
	{
		printf("Ingrese el numero hasta el que desea conocer las tablas de multiplicar: ");
		scanf("%d",&n);
		tablas (1, n, 1);
		system ("pause");
		menu ();
	}
	if (op==5)
	{
		printf("Ingrese el numero hasta el que desea hacer la sumatoria: ");
		scanf("%d",&n);
		x=sum(n);
		printf("El resultado de la sumatoria de los numeros hasta n es %d\n", x);
		system("pause");
		menu();
	}
	if (op==6)
	{
		printf("Ingrese el numero cuyo factorial desea averiguar: ");
		scanf("%d",&n);
		x=fact (n);
		printf("El factorial de %d es %d\n", n, x);
		system("pause");
		menu();
	}
	if (op==7)
	{
		printf ("Ingresde el numero hasta el que desea calcular la sumatoria: ");
		scanf("%d",&n);
		y=sumpot(n);
		printf("El resultado de la sumatoria es %ld\n", y);
		system("pause");
		menu();
	}
	if (op==8)
	{
		printf("Ingrese la base: ");
		scanf("%d",&b);
		printf("Ingrese el exponente: ");
		scanf("%d",&e);
		y=pot(b,e);
		printf("%d ^ %d = %ld\n", b, e, y);
		system("pause");
		menu ();
	}
	if (op==9)
	{
		printf("Ingrese el numero cuyos divisores desea conocer: ");
		scanf("%d",&n);
		divi (n, 1);
		system ("pause");
		menu ();
	}
	if (op==10)
	{
		printf ("Ingrese el numero que desea saber si es primo: ");
		scanf("%d",&n);
		bool pri=primo (n, 2);
		if (pri)
		{
			printf("%d es primo\n", n);
		}
		else 
		{
			printf ("%d no es primo\n", n);
		}
		system ("pause");
		menu ();
	}
	if (op==11)
	{
		printf("Ingrese el termino que desea conocer de fibonacci: ");
		scanf("%d",&n);
		x=fibonacci (n, 1, 0, 1);
		printf("El %d termino de fibonacci es %d\n", n, x);
		system ("pause");
		menu ();
	}
	if (op==12)
	{
		printf("Ingrese el numero hasta el que desea calcular fibonacci: ");
		scanf("%d", &n);
		fibo (n, 0, 0, 1);
		system("pause");
		menu ();
	}
	if (op==13)
	{
		printf("Ingrese el primer numero: ");
		scanf ("%d",&a);
		printf("Ingrese el segundo numero: ");
		scanf("%d",&b);
		x=mcm (a, b, 1);
		printf("El minimo comun multiplo de %d y %d es %d\n", a, b, x);
		system("pause");
		menu ();
	}
	if (op==14)
	{
		printf("Ingrese el primer numero: ");
		scanf("%d",&a);
		printf("Ingrese el segundo numero: ");
		scanf("%d",&b);
		x=mcd(a,b,a);
		printf("El maximo comun divisor de %d y %d es %d\n", a, b, x);
		system ("pause");
		menu ();
	}
}

//--------------------------------------------

main()
{
	menu ();
}
