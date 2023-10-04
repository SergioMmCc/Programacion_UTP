/* Triqui
Sergio Moncada Muñoz -> 1089380570
Juan Camilo Moreno Rojas -> 1088241470
Programacion 2 - Grupo 4 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define fil 3
#define col 3

//Matriz para almacenar los movimientos
char matriz [fil][col];

//Inicialmente la matriz se llena con espacios vacios para mostrarla en pantalla
void cmatriz ()
{
	int i, j;
	for (i=0; i<fil; i++)
	{
		for (j=0; j<col; j++)
		{
			matriz [i][j]=' ';
		}
	}
}

//Funcion para ubicar X o O en la posicion que desea el usuario
void mmatriz (int posx, int posy, char c)
{
	int i, j;
	matriz [posx][posy]= c;
	for (i=0; i<fil; i++)
	{
		for (j=0; j<col; j++)
		{
			printf ("%c ", matriz [i][j]);
		}
		printf ("\n");
	}
}

//Funcion para dar las instrucciones al usuario y revisar si hay un ganador
void triqui ()
{
	system ("cls");
	int jugadas, i, j, rep;
	jugadas=0;
	cmatriz (3, 3);
	printf ("Bienvenidos, vamos a jugar triqui\n");
	printf ("El jugador 1 sera X y el jugador 2 sera O\n");
	while (jugadas<=9)
	{
		if (matriz[0][0]=='X' && matriz[0][1]=='X' && matriz[0][2]=='X')
		{
			printf ("\nGana el jugador 1");
			break;
		}
		if (matriz[1][0]=='X' && matriz[1][1]=='X' && matriz[1][2]=='X')
		{
			printf ("\nGana el jugador 1");
			break;
		}
		if (matriz[2][0]=='X' && matriz[2][1]=='X' && matriz[2][2]=='X')
		{
			printf ("\nGana el jugador 1");
			break;
		}
		if (matriz[0][0]=='X' && matriz[1][0]=='X' && matriz[2][0]=='X')
		{
			printf ("\nGana el jugador 1");
			break;
		}
		if (matriz[0][1]=='X' && matriz[1][1]=='X' && matriz[2][1]=='X')
		{
			printf ("\nGana el jugador 1");
			break;
		}
		if (matriz[0][2]=='X' && matriz[1][2]=='X' && matriz[2][2]=='X')
		{
			printf ("\nGana el jugador 1");
			break;
		}
		if (matriz[0][0]=='X' && matriz[1][1]=='X' && matriz[2][2]=='X')
		{
			printf ("\nGana el jugador 1");
			break;
		}
		if (matriz[0][2]=='X' && matriz[1][1]=='X' && matriz[2][0]=='X')
		{
			printf ("\nGana el jugador 1");
			break;
		}
		if (matriz[0][0]=='O' && matriz[0][1]=='O' && matriz[0][2]=='O')
		{
			printf ("\nGana el jugador 2");
			break;
		}
		if (matriz[1][0]=='O' && matriz[1][1]=='O' && matriz[1][2]=='O')
		{
			printf ("\nGana el jugador 2");
			break;
		}
		if (matriz[2][0]=='O' && matriz[2][1]=='O' && matriz[2][2]=='O')
		{
			printf ("\nGana el jugador 2");
			break;
		}
		if (matriz[0][0]=='O' && matriz[1][0]=='O' && matriz[2][0]=='O')
		{
			printf ("\nGana el jugador 2");
			break;
		}
		if (matriz[0][1]=='O' && matriz[1][1]=='O' && matriz[2][1]=='O')
		{
			printf ("\nGana el jugador 2");
			break;
		}
		if (matriz[0][2]=='O' && matriz[1][2]=='O' && matriz[2][2]=='O')
		{
			printf ("\nGana el jugador 2");
			break;
		}
		if (matriz[0][0]=='O' && matriz[1][1]=='O' && matriz[2][2]=='O')
		{
			printf ("\nGana el jugador 2");
			break;
		}
		if (matriz[0][2]=='O' && matriz[1][1]=='O' && matriz[2][0]=='O')
		{
			printf ("\nGana el jugador 2");
			break;
		}
		if (jugadas==9)
		{
			printf ("\nEmpate");
			break;
		}
		if (jugadas%2==0)
		{
			printf ("\nJugador 1, ingrese la fila en la que desea marcar X (0-2): ");
			scanf ("%d", &i);
			printf ("Jugador 1, ingrese la columna en la que desea marcar X (0-2): ");
			scanf ("%d", &j);
			if (matriz[i][j]==' ' && i<3 && j<3)
			{
				mmatriz (i, j, 'X');
				jugadas++;
			}
			else
			{
				printf ("\nPor favor elija una casilla valida\n");
			}
		}
		else
		{
			printf ("\nJugador 2, ingrese la fila en la que desea marcar O (0-2): ");
			scanf ("%d", &i);
			printf ("Jugador 2, ingrese la columna en la que desea marcar O (0-2): ");
			scanf ("%d", &j);
			if (matriz[i][j]==' ' && i<3 && j<3)
			{
				mmatriz (i, j, 'O');
				jugadas++;
			}
			else
			{
				printf ("\nPor favor elija una casilla valida\n");
			}
		}
		
	}
	printf ("\n\nIngrese 1 para volver a jugar o 2 para salir: ");
	scanf ("%d", &rep);
	if (rep==1)
	{
		system ("pause");
		triqui ();
	}
}

main ()
{
	triqui ();
}
