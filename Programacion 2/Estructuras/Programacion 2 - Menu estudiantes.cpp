#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

//Menu estudiantes

/**************************
Nombre de subrutina: void gotoxy (int x, int y)
Objetivo: Procedimiento para ubicar los datos en una posicion especifica en la pantalla
Parametros: x -> Coordenada X en la que se imprimen los datos
			y -> Cooredenada Y en la que se imprimen los datos
Ejemplo de uso:			gotoxy (5, 6);
						printf ("Hola mundo");
*/

void gotoxy(int x, int y)
{
	COORD coord;
	coord.X = x;
	coord.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

/**************************
Nombre de estructura: estudiante
Objetivo: Representar un estudinate asignando su codigo, nombre, nota 1,
nota 2 y nota 3
codigo -> Codigo derl estudiante
nombre -> Nombre del estudiante
n1 -> Nota 1 del estudiante
n2 -> Nota 2 del estudiante
n3 -> Nota 3 del estudiante
*/

struct estudiante
{
	char codigo [6];
	char nombre [20]; 
	float n1, n2, n3; 
}; estudiante e [10];

//Variables globales
int contest=0;
float promediot, promedio [10];


//Agregar estudiante
/**************************
Nombre de la subrutina: void agregar (estudiante e [])
Objetivo: Agregar un estudinate a una lista de estudiantes
Parametros: e -> Llama la estructura estudiantes
Ejemplo de uso: 	Codigo: 123
					Nombre: Sergio
					Nota 1: 5
					Nota 2: 4.5
					Nota 3: 4.7	
*/

void agregar (estudiante e [])
{
	system ("cls");
	printf ("Estudiante #%d\n\n", contest+1);
	printf ("Codigo: ");
	fflush (stdin);
	gets (e[contest].codigo);
	printf ("Nombre: ");
	fflush (stdin);
	gets (e[contest].nombre);
	printf ("Nota 1: ");
	scanf ("%f", &e[contest].n1);
	printf ("Nota 2: ");
	scanf ("%f", &e[contest].n2);
	printf ("Nota 3: ");
	scanf ("%f", &e[contest].n3);
	promedio[contest]=(e[contest].n1+e[contest].n2+e[contest].n3)/3;
	printf ("\nPromedio: %.2f\n\n", promedio [contest]);
	promediot=0;
	for (int i=0; i<=contest; i++)
	{
		promediot=promediot+promedio[i];
	}
	contest++;
	promediot=promediot/contest;	
}


//Buscar estudiante
/************************
Nombre de la subrutina: void buscar (estudiante e [], char cod[])
Objetivo: Mostrar en pantalla los datos de un estudiante solicitado
		  por el ususario
Prametros: e -> Llama la estructura estudiantes
		   cod -> Codigo del estudiante que busca el usuario
Ejemplo de uso: 	estudiante e = e;
					cod = 123;
					estudiante:		Codigo: 123
									Nombre: Sergio
									Nota 1: 5
									Nota 2: 4
									Nota 3: 4.5
									Promedio: 4.5
*/

void buscar (estudiante e[], char cod[])
{
	int cont=0;
	for (int i=0; i<=contest; i++)
	{
		if (strcmp (e[i].codigo, cod) == 0)
		{
			system ("cls");
			printf ("Estudiante %d\n\n", i+1);
			printf ("Codigo: %s\n", e[i].codigo);
			printf ("Nombre: %s\n", e[i].nombre);
			printf ("Nota 1: %.2f\n", e[i].n1);
			printf ("Nota 2: %.2f\n", e[i].n2);
			printf ("Nota 3: %.2f\n", e[i].n3);
			printf ("Promedio: %.2f\n\n", promedio[i]);
			cont++;
			break;
		}
	}
	if (cont==0)
	{
		printf ("\nEl codigo no corresponde a ningun estudiante\n\n");
	}
}


//Modificar datos
/**************************
Nombre de la subrutina: void cambiar (estudiante e[], char cod[])
Objetivo: Cambiar alguno de los datos de un estudiante
Parametros: e -> Llama la estructura estudiantes
			cod -> Codigo del estudiante cuyos datos desea cambiar
				   el usuario
Ejemplo de uso: estudiante e - e;
				codigo - 123;
				Ingrese 1 para modificar el codigo del estudiante
				Ingrese 2 para modificar el nombre del estudiante
				Ingrese 3 para modificar la nota 1 del estudiante
				Ingrese 4 para modificar la nota 2 del estudiante
				Ingrese 5 para modificar la nota 3 del estudiante
				Ingrese 6 para salir
				Ingrese la opcion que desea:
*/

void cambiar (estudiante e[], char cod[])
{
	int que, cont=0;
	for (int i=0; i<=contest; i++)
	{
		if (strcmp (e[i].codigo, cod) == 0)
		{
			printf ("\nIngrese 1 para modificar el codigo del estudiante\n");
			printf ("Ingrese 2 para modificar el nombre del estudiante\n");
			printf ("Ingrese 3 para modificar la nota 1 del estudiante\n");
			printf ("Ingrese 4 para modificar la nota 2 del estudiante\n");
			printf ("Ingrese 5 para modificar la nota 3 del estudiante\n");
			printf ("Ingrese 6 para salir\n");
			printf ("Ingrese la opcion que desea: ");
			scanf ("%d", &que);
			if (que==1)
			{
				system ("pause");
				system ("cls");
				printf ("Actual codigo del estudiante: %s\n", e[i].codigo);
				printf ("Ingrese el nuevo codigo del estudiante: ");
				fflush (stdin);
				gets (e[i].codigo);
				printf ("\nEl nuevo codigo del estudiante es: %s\n\n", e[i].codigo);
			}
			if (que==2)
			{
				system ("pause");
				system ("cls");
				printf ("Actual nombre del estudiante: %s\n", e[i].nombre);
				printf ("Ingrese el nuevo nombre del estudiante: ");
				fflush (stdin);
				gets (e[i].nombre);
				printf ("\nEl nuevo nombre del estudiante es: %s\n\n", e[i].nombre);
			}
			if (que==3)
			{
				system ("pause");
				system ("cls");
				printf ("Actual nota 1 del estudiante: %.2f\n", e[i].n1);
				printf ("Ingrese la nueva nota 1 del estudiante: ");
				scanf ("%f", &e[i].n1);
				printf ("\nLa nueva nota 1 del estudiante es: %.2f\n\n", e[i].n1);
			}
			if (que==4)
			{
				system ("pause");
				system ("cls");
				printf ("Actual nota 2 del estudiante: %.2f\n", e[i].n2);
				printf ("Ingrese la nueva nota 2 del estudiante: ");
				scanf ("%f", &e[i].n2);
				printf ("\nLa nueva nota 2 del estudiante es: %.2f\n\n", e[i].n2);
			}
			if (que==5)
			{
				system ("pause");
				system ("cls");
				printf ("Actual nota 3 del estudiante: %.2f\n", e[i].n3);
				printf ("Ingrese la nueva nota 3 del estudiante: ");
				scanf ("%f", &e[i].n3);
				printf ("\nLa nueva nota 3 del estudiante es: %.2f\n\n", e[i].n3);
			}
			promedio[i]=(e[i].n1+e[i].n2+e[i].n3)/3;
			promediot=0;
			for (int j=0; j<=contest; j++)
			{
				promediot=promediot+promedio[j];
			}
			promediot=promediot/contest;
			cont++;
			break;
		}
	}
	if (cont==0)
	{
		printf ("\nEl codigo no corresponde a ningun estudiante\n\n");
	}
}

//Mostrar lista de estudiantes
/**********************************
Nombre de la subrutina: void mostrar (estudiante e[])
Objetivo: Imprimir una lista con todos los datos de
		  los estudiantes que han sido agregados
Parametros: e -> Llama la estructura estudiantes
Ejemplo de uso: estudiante e - e
*/

void mostrar (estudiante e[])
{
	system ("pause");
	system ("cls");
	if (contest==0)
	{
		gotoxy (2, 1);
		printf ("Aun no hay ningun estudiante en la lista\n\n");
	}
	else
	{
		gotoxy (2, 1);
		printf ("Codigo");
		gotoxy (17, 1);
		printf ("Nombre");
		gotoxy (32, 1);
		printf ("Nota 1");
		gotoxy (47, 1);
		printf ("Nota 2");
		gotoxy (62, 1);
		printf ("Nota 3");
		gotoxy (77, 1);
		printf ("Definitiva");
		for (int i=0; i<contest; i++)
		{
			gotoxy (2, 2+i);
			printf ("%s", e[i].codigo);
			gotoxy (17, 2+i);
			printf ("%s", e[i].nombre);
			gotoxy (32, 2+i);
			printf ("%.2f", e[i].n1);
			gotoxy (47, 2+i);
			printf ("%.2f", e[i].n2);
			gotoxy (62, 2+i);
			printf ("%.2f", e[i].n3);
			gotoxy (77, 2+i);
			printf ("%.2f", promedio[i]);
		}
		gotoxy (2, contest+3);
		printf ("Promedio del grupo: %.2f\n\n", promediot);	
	}
	
}

//Menu de opciones
/***************************
Nombre de la subrutina: void menu ()
Objetivo: Abrir un menu en el que el usuario elige entre
		  5 opciones:
					1. Adicionar estudiantes
					2. Buscar estudiante por codigo
					3. Modificar datos
					4. Lista de estudiantes
					5. Salir
					Ingrese la opcion que desea:
*/

void menu ()
{
	int op;
	system ("cls");
	printf ("1. Adicionar estudiantes\n");
	printf ("2. Buscar estudiante por codigo\n");
	printf ("3. Modificar datos\n");
	printf ("4. Lista de estudiantes\n");
	printf ("5. Salir\n\n");
	printf ("Ingrese la opcion que desea: ");
	scanf ("%d", &op);
	if (op==1)
	{
		agregar (e);
		system ("pause");
		menu ();
	}
	if (op==2)
	{
		system ("pause");
		system ("cls");
		char cod[6];
		printf ("Ingrese el codigo del estudiante que desea buscar: ");
		fflush (stdin);
		gets (cod);
		buscar (e, cod);
		system ("pause");
		menu ();
	}
	if (op==3)
	{
		system ("pause");
		system ("cls");
		char cod[6];
		printf ("Ingrese el codigo del estudiante que desea modificar: ");
		fflush (stdin);
		gets (cod);
		cambiar (e, cod);
		system ("pause");
		menu ();
	}
	if (op==4)
	{
		mostrar (e);
		system ("pause");
		menu ();
	}
}

main ()
{
	menu ();
}
