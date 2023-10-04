// Ahorcado

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void ahorcado ()
{
	system ("cls");
	int n, errores, i, cont, rep, dif;
	errores=10;
	char c;
	printf ("Bienvenidos a ahorcado\n\n");
	printf ("Instrucciones:\n");
	printf ("El jugador 1 ingresara una palabra y el jugador 2 tratara de adivinar cual es\n");
	printf ("escribiendo una letra que crea que se encuentra en la palabra, si acierta se\n");
	printf ("mostraran la(s) posicion(es) en que se encuentra dicha letra, sino se le sumara\n");
	printf ("un error. Cuando el jugador 2 cometa 10 errores, perdera el juego.\n\n");
	char cad [30];
	printf ("Jugador 1, ingrese la palabra que el jugador 2 tendra que adivinar: ");
	gets (cad);
	n=strlen(cad);
	printf ("\nLa palabra tiene %d letras\n", n);
	char cad2 [n];
	for (i=0; i<n; i++)
	{
		cad2[i]=cad[i];
	}
	char cad3 [n];
	for (i=0; i<n; i++)
	{
		cad3[i]=' ';
	}
	while (errores>0)
	{
		dif=0;
		for (i=0; i<n; i++)
		{
			if (cad2[i]!=cad3[i])
			{
				dif++;
			}
		}
		if (dif==0)
		{
			printf ("\nGano el jugador 2, la palabra es: %s\n\n", cad3);
			break;
		}
		else
		{
			printf("Le quedan %d errores\n", errores);
			printf ("\nJugador 2, ingrese una letra que crea que esta en la palabra: ");
			scanf (" %s", &c);
			for (i=0; i<n; i++)
			{
				if (c==cad2[i])
				{
					cad3[i]=c;
					cont++;
				}
			}
			if (cont==0)
			{
				errores--;
			}
			cont=0;
			printf ("Palabra: %s\n", cad3);
		}	
	}
	if (errores==0)
	{
		printf ("\nEl jugador 2 perdio, la palabra que eligio el jugador 1 es: %s\n\n", cad2);
	}
	
	if (rep==1)
	{
		system ("pause");
		ahorcado ();
	}
}
//--------------------------------------------
int main ()
{
	ahorcado();	
}
