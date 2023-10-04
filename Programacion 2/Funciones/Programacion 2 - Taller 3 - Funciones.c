#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/* 1) Devolver el valor de la expresion al resolver la expresion n^2 + 10,
para cualquier valor de n enetero.  (Procedimiento con parametros) */

void expresion (int n)
{
	int r;
	r=(pow(n,2)+10);
	printf("%d^2 +10 = %d \n\n", n, r);
}

//--------------------------------------

/* 2) Medir la longitud de la circunferencia, dado el radio. 
(Función con parametros) */

float long_circ(int ra)
{
	float l;
	l=(2*M_PI)*ra;
	return l;
}

//--------------------------------------

/* 3) Dado un valor de temperatura en grados Celsius, convertirla 
a grados Fahrenheit. (función sin parámetros) */

float temp ()
{
	int grados_c;
	float grados_f;
	printf("\nIngrese la temperatura en grados celsius: ");
	scanf("%d",&grados_c);
	grados_f= (grados_c/0.55)+32;
	return grados_f;
}

//--------------------------------------

/* 4) Calcular el área de un trapecio isóceles
(lados no paralelos son iguales).(procedimiento sin parámetros) */

void area_t ()
{
	float b1, b2, h, a;
	printf("\nIngrese la base inferior del trapecio: ");
	scanf("%f",&b1);
	printf("Ingrese la base superior del trapecio: ");
	scanf("%f",&b2);
	printf("Ingrese la altura del trapecio: ");
	scanf("%f",&h);
	a=((b1+b2)*h)/2;
	printf("El area del trapecio es %.2f \n\n", a);
}

//--------------------------------------

// 5) Calcular el volumen de una esfera. (función con parámetros)

float ve (int r)
{
	float v;
	v=(0.75*M_PI)*(pow(r,3));
	return v;
}

//--------------------------------------

/* 6) Calcular el área de la superficie de un cilindro. 
(procedimiento con parámetros) */

void asc (int r, int h)
{
	float a;
	a=((2*M_PI)*r*h)+((2*M_PI)*(pow(r,2)));
	printf("El area de la superficie del cilindro es %.2f \n\n",a);
}

//--------------------------------------

/* 7) Dadas cantidades de billetes recibidos en denominaciones
de $1.000, $2.000, $5.000, $10.000, $20.000 y $50.000, obtener
como resultado el valor de del conjunto de todos los billetes.
(función con parametros) */

int dinero (int b1, int b2, int b5, int b10, int b20, int b50)
{
	int total;
	total=(b1*1000)+(b2*2000)+(b5*5000)+(b10*10000)+(b20*20000)+(b50*50000);
	return total;
}

//--------------------------------------

/* 8) Dado un salario en pesos colombianos (cop) convertir el
valor dado a dolares */

float salario (int sc)
{
	float sd;
	sd=sc/4851.26;
	return sd;
}

//--------------------------------------

/* 9) Dadas 3 notas, averiguar si un estudiante paso el curso
o no */

float curso (float n1, float n2, float n3)
{
	float promedio;
	promedio=(n1+n2+n3)/3;
	return promedio;
}

//--------------------------------------

/* 10) Dada una estatura en metros (m), averiguar esta misma
en pies (ft)*/

float estatura (float em)
{
	float ep;
	ep=em*3.28084;
	return ep;
}

//--------------------------------------

void menu ()
{
	int op, n, rc, c, re, rci, hci, b1, b2, b5, b10, b20, b50, t, sc;
	float x, n1, n2, n3, em;
	system ("cls");
	printf("Ingrese 1 para la expresion n^2 +10 \n");
	printf("Ingrese 2 para calcular la longitud de una circunferencia \n");
	printf("Ingrese 3 para covertir una temperatura de grados celsius a fahrenheit \n");
	printf("Ingrese 4 para calcular el area de un trapecio isosceles \n");
	printf("Ingrese 5 para calcular el volumen de una esfera \n");
	printf("Ingrese 6 para calcular el area de la superficie de un cilindro \n");
	printf("Ingrese 7 para calcular el total de dinero \n");
	printf("Ingrese 8 para conertir salario en pesos colombianos a dolares\n");
	printf("Ingrese 9 para averiguar si un estudiante aprobo un curso o no\n");
	printf("Ingrese 10 para averiguar una estatura en pies (ft)\n");
	printf("Ingrese 11 para salir \n\n");
	printf("Elija la opcion que desea (1-11): ");
	scanf("%d",&op);
	
	if(op==1)
	{
		printf("\nIngrese el valor de n: ");
		scanf("%d",&n);
		expresion(n);
		system("pause");
		menu();
	}
	if(op==2)
	{
		printf("\nIngrese el radio de la circunferencia: ");
		scanf("%d",&rc);
		x=long_circ(rc);
		printf("La longitud de la circunferencia con radio igual a %d es %.2f \n\n",rc,x);
		system("pause");
		menu ();
	}
	if(op==3)
	{
		x=temp();
		printf("La temperatura en grados fahrenheit es %.2f \n\n",x);
		system("pause");
		menu ();
	}
	if(op==4)
	{
		area_t ();
		system("pause");
		menu ();
	}
	if(op==5)
	{
		printf("\nIngrese el radio de la esfera: ");
		scanf("%d",&re);
		x=ve(re);
		printf("El volumen de la esfera es igual a %.2f \n\n",x);
		system("pause");
		menu ();
	}
	if(op==6)
	{
		printf("\nIngrese el radio del cilindro: ");
		scanf("%d",&rci);
		printf("Ingrese la altura del cilindro: ");
		scanf("%d",&hci);
		asc(rci, hci);
		system("pause");
		menu();
	}
	if(op==7)
	{
		printf("\n%cCuantos billetes de 1000 desea contar?: ",168);
		scanf("%d",&b1);
		printf("%cCuantos billetes de 2000 desea contar?: ",168);
		scanf("%d",&b2);
		printf("%cCuantos billetes de 5000 desea contar?: ",168);
		scanf("%d",&b5);
		printf("%cCuantos billetes de 10000 desea contar?: ",168);
		scanf("%d",&b10);
		printf("%cCuantos billetes de 20000 desea contar?: ",168);
		scanf("%d",&b20);
		printf("%cCuantos billetes de 50000 desea contar?: ",168);
		scanf("%d",&b50);
		t=dinero(b1,b2,b5,b10,b20,b50);
		printf("El total de dinero es %d \n\n", t);
		system("pause");
		menu();
	}
	if(op==8)
	{
		printf("\nIngrese su salario en pesos colombianos: ");
		scanf("%d",&sc);
		x=salario(sc);
		printf("Su salario es de %f dolares\n\n",x);
		system("pause");
		menu();
	}
	if(op==9)
	{
		printf("\Ingrese la nota 1: ");
		scanf("%f",&n1);
		printf("\Ingrese la nota 2: ");
		scanf("%f",&n2);
		printf("\Ingrese la nota 3: ");
		scanf("%f",&n3);
		x=curso(n1,n2,n3);
		if(x>=3)
		{
			printf("El estudiante aprobo el curso\n\n");
		}
		else
		{
			printf("El estudiante no aprobo el curso\n\n");
		}
		system("pause");
		menu ();
	}
	if (op==10)
	{
		printf("Ingrese su estatura en metros (m): ");
		scanf("%f", &em);
		x=estatura(em);
		printf("Su estatura es %.2f pies\n\n",x);
		system("pause");
		menu();
	}
}

//--------------------------------
main()
{
	menu();
}
