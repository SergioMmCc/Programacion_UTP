/* Ahorcado
Sergio Moncada Muñoz -> 1089380570
Juan Camilo Moreno Rojas -> 1088241470
Programacion 2 - Grupo 4 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <ctype.h>

//El siguiente procedimiento lo usamos para ubicar la posicion del dibujo y los datos.

void gotoxy(int x, int y)
{
	COORD coord;
	coord.X = x;
	coord.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

//-------------------------------------------------------------------------------------------
//Variables globales

char palabras [30][10]=
{"manzana","pera","mango","fresa","frambuesa","maracuya","mandarina","lulo","kiwi","tomate",
"aguacate","guayaba","uva","mora","banano","sandia","melocoton","melon","coco","arandano",
"cereza","limon","guanabana","durazno","granadilla","naranja","papaya","ciruela","zapote","carambola"};

char P1 [10], P2 [10], Letras [30], printLetras [60];
int errores=6, t;

//Diseño
void dibujo ()
{
	int i;
	for (i=0; i<8; i++)
	{
		gotoxy (70+i, 1);
		printf ("%c",196);
	}
	for (i=0; i<8; i++)
	{
		gotoxy (70, i+2);
		printf ("%c",179);
	}
	for (i=0; i<2; i++)
	{
		gotoxy (77, i+2);
		printf ("%c", 179);
	}
	for (i=0; i<14; i++)
	{
		gotoxy (66+i, 9);
		printf ("%c", 196);
	}
	if (errores<6)
	{
		gotoxy (77, 4);
		printf ("O");
	}
	if (errores<5)
	{
		gotoxy (77, 5);
		printf ("%c", 179);
	}
	if (errores<4)
	{
		gotoxy (76, 5);
		printf ("/");
	}
	if (errores<3)
	{
		gotoxy (78, 5);
		printf ("\\");
	}
	if (errores<2)
	{
		gotoxy (76, 6);
		printf ("/");
	}
	if (errores<1)
	{
		gotoxy (78, 6);
		printf ("\\");
	}
}

// Funcion aleatorio
int aleatorio ()
{
	int num, c;
	srand (time(NULL));
	num=rand()%(29);
	return num;
}

//Funcion para elegir la palabra
void selectword ()
{
	int x, i;
	x=aleatorio ();
	for (i=0; i<10; i++)
	{
		P1 [i] = palabras [x][i];
	}
	t=strlen (P1);
	for (i=0; i<t; i++)
	{
		P2[i]='_';
	}
}

//Funcion para buscar una letra
void BuscarLetra ()
{
	int i, tl, cont, dif;
	char L;
	system("pause");
	system ("cls");
	dibujo ();
	gotoxy (0,0);
	printf ("Le quedan %d oportunidades\n", errores);
	printf ("%s\n", P2);
	printf ("Letras intentadas anteriormente: %s\n", printLetras);
	printf ("Ingrese una letra que crea que se encuentra en la palabra: ");
	scanf (" %c", &L);
	L=tolower(L);
	cont=0;
	dif=0;
	tl=strlen(Letras);
	for (i=0; i<tl; i++)
	{
		if (L==Letras[i])
		{
			printf ("\nYa intento esa letra anteriormente\n\n");
			dif++;
			break;
		}
	}
	if (dif==0)
	{
		Letras[tl]=L;
		printLetras[tl*2]=L;
		printLetras[(tl*2)+1]='-';
		for (i=0; i<t; i++)
		{
			if (L==P1[i])
			{
				cont++;
				P2[i] = P1[i];
			}
		}
		if (cont==0)
		{
			errores--;
		}	
	}
}

//Funcion para ver si el usuario ya gano
void Comparar ()
{
	int i, cont=0;
	for (i=0; i<t; i++)
	{
		if (P1[i]!=P2[i])
		{
			cont++;
			break;
		}
	}
	if (cont==0)
	{
		printf ("\n%s\n", P2);
		printf ("\nFelicidades, gano la partida. La palabra es: %s.\n", P1);
	}
	else
	{
		if (errores==0)
		{
			printf ("\n%s\n", P2);
			printf ("\nPerdio la partida. La palabra es: %s.\n", P1);
		}
		else
		{
			BuscarLetra ();
			Comparar ();
		}
	}
}

//Funcion para presentar el juego e invocar las demas funciones
void ahorcado ()
{
	printf ("Bienvenido, vamos a jugar ahorcado\n\n");
	printf ("Instrucciones:\n");
	printf ("Se seleccionara el nombre de una fruta aleatoriamente, el usuario debera ingresar una letra\n");
	printf ("que crea que se encuentra en el nombre de dicha fruta. En caso de acertar, se mostrara la(s)\n");
	printf ("posicion(es) de la palabra en que se dicha letra. En caso de fallo, perdera una oportunidad.\n");
	printf ("Si el usuario pierde todas sus oportunidades, perdera la partida. Si completa la palabra,\n");
	printf ("ganara la partida.\n\n");
	selectword ();
	BuscarLetra ();
	Comparar ();
}

//-------------------------------------------------------------
int main ()
{
	ahorcado ();
}
