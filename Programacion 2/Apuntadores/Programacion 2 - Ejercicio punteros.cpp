/* Programa: NOMBRES. CDesc.: manejo de memoria dinámica, arreglo de apuntadores */

#include <stdio.h>
#include <stdlib.h>/* malloc(), free() */
#include <string.h>
#include <conio.h>

#define LIMITE 5

int main()
{
	char str[255], *nombre [LIMITE];
	int i;
	system ("cls");
	printf("\n\t\tIngresa una lista de nombres\n");
	for (i=0; i < LIMITE; i++)
	{
		printf("%2d.-Nombre ? ", 1);
		gets (str);
		nombre[i] = (char *)malloc(strlen(str) +1); /* Asigna memoria a nombre*/
		strcpy (nombre[i], str); /*Copia str a nombre */
	}
	printf("\n\t\tLista de nombres: \n");
	for (i=0; i < LIMITE; i++)
		printf("\n%2d.- %s \n", i, nombre[i]);/* desaloja la memoria */
	for (i=0; i < LIMITE; i++)
		free (nombre[i]);
	system ("pause");
	return 0;	
}
