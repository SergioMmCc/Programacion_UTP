/* 1) Calcular y mostrar la suma, resta, multiplicación, división, potencia de dos números. */

#include <stdio.h>
#include <math.h>

int main ()
{
	float a, b, suma, resta, mult, div, pot;
	 
	 //Entradas
	 printf("Ingrese el primer numero: ");
	 scanf("%f", &a);
	 printf("Ingrese el segundo numero: ");
	 scanf("%f", &b);
	 //Proceso
	 suma=a+b;
	 printf("%f + %f = %f.\n", a, b, suma);
	 resta=a-b;
	 printf("%f - %f = %f.\n", a, b, resta);
	 mult=a*b;
	 printf("%f * %f = %f.\n", a, b, mult);
	 div=a/b;
	 printf("%f / %f = %f.\n", a, b, div);
	 pot=pow(a,b);
	 printf("%f ^ %f = %f.\n", a, b, pot);
	 
	 return 0;
}

