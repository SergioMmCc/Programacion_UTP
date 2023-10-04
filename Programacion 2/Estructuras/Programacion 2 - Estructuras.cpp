#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <windows.h>

void gotoxy(int x, int y)
{
	COORD coord;
	coord.X = x;
	coord.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

struct Estudiante
{
	char Codigo [6];
	char Nombre [20];
	float Nota1, Nota2, Nota3;
};

void leer (Estudiante e [])
{
	float Promedio[5], suma=0;
	for (int i=0; i<5; i++)
	{
		printf ("Estudiante %d \n", i+1);
		printf ("Codigo: ");
		fflush (stdin);
		gets (e[i].Codigo);
		printf ("Nombre: ");
		fflush (stdin);
		gets(e[i].Nombre);
		printf ("Nota 1: ");
		scanf ("%f", &e[i].Nota1);
		printf ("Nota 2: ");
		scanf ("%f", &e[i].Nota2);
		printf ("Nota 3: ");
		scanf ("%f", &e[i].Nota3);
		Promedio[i]=(e[i].Nota1+e[i].Nota2+e[i].Nota3)/3;
		printf ("Promedio: %.2f\n\n", Promedio[i]);
		suma=suma+Promedio[i];
	}
	suma=suma/5;
	printf ("El promedio del grupo es %.2f\n\n", suma);
	
	system ("pause");
	system ("cls");
	gotoxy (2, 1);
	printf ("Codigo");
	gotoxy (22, 1);
	printf ("Nombre");
	gotoxy (42, 1);
	printf ("Nota 1");
	gotoxy (62, 1);
	printf ("Nota 2");
	gotoxy (82, 1);
	printf ("Nota 3");
	gotoxy (102, 1);
	printf ("Definitiva");
	for (int i=0; i<5; i++)
	{
		gotoxy (2, 2+i);
		printf ("%s", e[i].Codigo);
		gotoxy (22, 2+i);
		printf ("%s", e[i].Nombre);
		gotoxy (42, 2+i);
		printf ("%.2f", e[i].Nota1);
		gotoxy (62, 2+i);
		printf ("%.2f", e[i].Nota2);
		gotoxy (82, 2+i);
		printf ("%.2f", e[i].Nota3);
		gotoxy (102, 2+i);
		printf ("%.2f", Promedio[i]);
	}
	gotoxy (80, 7);
	printf ("Promedio del grupo: %.2f", suma);
}

main ()
{
	Estudiante e [5];
	leer (e);
}
