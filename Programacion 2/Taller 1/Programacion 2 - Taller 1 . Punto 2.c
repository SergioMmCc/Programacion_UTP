/* 2) De un estudiante se conoce los siguientes datos:
- Código
- Nombre
- Nota 1
- Nota 2
- Nota 3
Calcular y mostrar su promedio */

#include <stdio.h>

int main ()
{
	float nota1, nota2, nota3, promedio;
	char nombre[30];
	int codigo;
	
	//Entradas
	printf ("Ingrese la nota 1: ");
    scanf ("%f", &nota1);
    printf ("Ingrese la nota 2: ");
    scanf ("%f", &nota2);
    printf ("Ingrese la nota 3: ");
    scanf ("%f", &nota3);
    printf ("Ingrese el nombre del estudiante: ");
    scanf ("%s", &nombre);
    printf ("Ingrese el codigo del estudiante: ");
    scanf ("%d", &codigo);
	//Proceso
	promedio=(nota1+nota2+nota3)/3;
	//Salida
	printf("El promedio del estudiante %s (%d) es %f.\n", nombre, codigo, promedio);
	
	return 0;
}
