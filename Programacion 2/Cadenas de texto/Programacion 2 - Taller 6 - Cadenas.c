// Taller 6 - Cadenas de Caracteres

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 1) Hacer una función que reciba una cadena de
caracteres y devuelva la longitud de esta. Es decir,
implemente la función strlen. */

int longitud (char cad [])
{
	int i=0;
	while (cad [i]!= '\0')
	{
		i++;
	}
	return(i);
}
//---------------------------------------------------
/* 2) Hacer una función que reciba una cadena de
caracteres y devuelva una copia en otra con el
contenido de la primera. Es decir implemente la
función strcpy. */

void cambio (char cad [])
{
	int i, x;
	x=longitud (cad);
	char cad2[x];
	for (i=0; i<=x; i+1)
	{
		cad2[i]=cad[i];
		i++;
	}
	printf ("%s\n", cad2);
}

//---------------------------------------------------
/* 3) Hacer una función que reciba un entero N y
devuelva una cadena de longitud N, leyendo por
pantalla cada uno de los N caracteres de la cadena. */

void LeerCadena (int t)
{
	int i;
	char cad[t];
	for (i=0; i<t; i++)
	{
		printf("Pos [%d]: ", i);
		scanf("%s",&cad[i]);
		fflush(stdin);
	}
	printf("%s\n",cad);
}

//---------------------------------------------------
/* 4) Haga una función que reciba una cadena de caracteres
y un carácter, debe devolver la cadena con el caracter
adicionado al final. Por ejemplo si la cadena inicial es
“casa” y el caracter es ´s´, debe devolver “casas”. */

void UnirC (char cad[], char c)
{
	int x;
	x=longitud (cad);
	char cad2[x+2];
	int i=0;
	while (cad[i]!='\0')
	{
		cad2[i]=cad[i];
		i++;
	}
	cad2[i] = c;
	cad2 [i+1] ='\0'; //Agregar el terminador de cadena al final
	printf ("%s\n", cad2);
}
//------------------------------------------------------
/* 5) Hacer una función que reciba una cadena de caracteres
y la invierta en ella misma. */

void invertir1 (char cad[])
{
	int i, x;
	float j;
	char c;
	x=longitud (cad);
	i=0;
	j=(x/2);
	while (i<j)
	{
		c=cad[i];
		cad[i]=cad[x-1];
		cad[x-1]=c;
		i++;
		x--;
	}
	printf ("%s\n", cad);
}
//------------------------------------------------------
/* 6) Hacer una función que reciba una cadena de caracteres y
devuelva otra cadena invirtiendo todos los caracteres de la
primera. */

void invertir (char cad[])
{
	int x, j, i;
	x=longitud (cad);
	char cad2[x];
	j=0;
	for (i=x-1; i>=0; i--)
	{
		cad2[j]=cad[i];
		j++;
	}
	printf ("%s --> %s\n", cad, cad2);
}
//---------------------------------------------------
/* 7) Haga una función que reciba dos cadenas de caracteres
y devuelva otra cadena con la concatenación de las dos primeras.
Es decir implemente la función concat. */

void concatenar (char cad[], char cad2[])
{
	int x, y, i, j;
	x=longitud(cad);
	y=longitud(cad2);
	char cad3[x+y];
	for (i=0; i<=x; i+1)
	{
		cad3[i]=cad[i];
		i++;
	}
	for (j=0; j<=y; j+1)
	{
		cad3[j+x]=cad2[j];
		j++;
	}
	printf ("%s\n", cad3);
}
//---------------------------------------------------
/* 8) Hacer una función que reciba una cadena de caracteres y
cuente cuantas vocales tiene. */

void contar (char cad [])
{
	int cont, j, x;
	char vocales[5]="aeiou";
	char c, a, e, i, o, u;
	a=vocales[0];
	e=vocales[1];
	i=vocales[2];
	o=vocales[3];
	u=vocales[4];
	x=longitud (cad);
	for (j=0; j<=x; j++)
	{
		c=cad[j];
		if (c==a || c==e || c==i || c==o || c==u)
		{
			cont++;
		}
	}
	printf ("%s tiene %d vocales\n", cad, cont);
}
//---------------------------------------------------
/* 9) Hacer una función que reciba una cadena de caracteres y
devuelva otra sin las vocales. */

void takev (char cad[])
{
	int ii, x, j;
	char vocales [5] = "aeiou";
	char c, a, e, i, o, u;
	a=vocales[0];
	e=vocales[1];
	i=vocales[2];
	o=vocales[3];
	u=vocales[4];
	x=longitud (cad);
	j=0;
	char cad2 [x];
	for (ii=0; ii<=x; ii++)
	{
		c=cad[ii];
		if (c!=a && c!=e && c!=i && c!=o && c!=u)
		{
			cad2 [j] = cad[ii];
			j++;
		}
	}
	printf ("%s\n", cad2);
}
//---------------------------------------------------
/* 10) Hacer una función que lea un string con solo caracteres
numéricos y devuelva el número que representa. */

int num (char cad[])
{
	int x, i, n;
	n=0;
	x=longitud (cad);
	for (i=0; i<=x; i++)
	{
		if (cad[i]>='0' && cad[i]<='9')
		{
			n=n*10+cad[i]-'0';
		}
		else
		{
			break;
		}
	}
	return n;
}
//---------------------------------------------------
/* 11) Hacer una función que reciba una cadena de caracteres e
indique si es palíndrome. */

void palindrome (char cad [])
{
	int x, i, cont;
	float y;
	x=longitud (cad);
	cont=0;
	y=x/2;
	for (i=0; i<=y; i++)
	{
		if (cad[i]!=cad[x-1])
		{
			cont++;
		}
		x--;
	}
	if (cont==0)
	{
		printf ("%s es palindrome\n", cad);
	}
	else
	{
		printf ("%s no es palindrome\n", cad);
	}
}
//---------------------------------------------------
/* 12) Hacer una función boolean que reciba dos cadenas
de caracteres e indique si son iguales. Es decir 
implemente la función srtcmp. */

void iguales (char cad[], char cad2[])
{
    int i, j, x, y, cont;
    x=longitud(cad);
    y=longitud(cad2);
    cont=0;
    if (x!=y)
    {
        printf ("Las cadenas no son iguales\n");
    }
    else
    {
        for (i=0; i<=x; i++)
        {
            if (cad[i]!=cad2[i])
            {
                cont++;
            }
        }
        if (cont==0)
        {
            printf ("Las cadenas de texto son iguales\n");
        }
        else
        {
            printf ("Las cadenas de texto no son iguales\n");
        }
    }
}
//---------------------------------------------------
/* 13) Hacer una función que reciba dos cadenas de
caracteres e indique si la segunda está incluida en
la primera (es decir si es substring). */

void comp (char cad [], char cad2 [])
{
	int x, y, i, j;
	j=0;
	x=longitud (cad);
	y=longitud (cad2);
	if (y>x)
	{
		printf ("%s no esta incluida en %s\n", cad2, cad);
	}
	else
	{
		for (i=0; i<x; i++)
		{
			if (j==y)
			{
				break;
			}
			else
			{
				if (cad[i]==cad2[j] || cad2[j]==cad[x])
				{
					j++;
				}
				else
				{
					j=0;
				}
			}
		}
		if (j==y)
		{
			printf ("%s esta incluida en %s\n", cad2, cad);
		}
		else
		{
			printf ("%s no esta incluida en %s\n", cad2, cad);
		}
	}
}
//---------------------------------------------------
void menu ()
{
	int op, n;
	system ("cls");
	printf ("Ingrese 1 para averiguar la longitud de una palabra\n");
	printf ("Ingrese 2 para imprimir una cadena de texto en otra\n");
	printf ("Ingrese 3 para imprimir una cadena de longitud n\n");
	printf ("Ingrese 4 para agregar un caracter a una cadena de texto\n");
	printf ("Ingrese 5 para invertir una cadena de texto en si misma\n");
	printf ("Ingrese 6 para invertir una cadena de texto en otra\n");
	printf ("Ingrese 7 para concatenar dos cadenas de texto\n");
	printf ("Ingrese 8 para contar las vocales que tiene una cadena de texto\n");
	printf ("Ingrese 9 para quitar las vocales de una cadena de texto\n");
	printf ("Ingrese 10 para convertir una cadena con solo caracteres numericos en un numero\n");
	printf ("Ingrese 11 para averiguar sin una cadena de texto es un palindromo\n");
	printf ("Ingrese 12 para averiguar si dos cadenas de texto son iguales\n");
	printf ("Ingrese 13 para averiguar si una cadena esta incluida en otra\n");
	printf ("Ingrese 14 para salir\n");
	printf ("Ingrese la opcion que desea (1-14): ");
	scanf ("%d", &op);
	fflush(stdin);
	
	if (op==1)
	{
	    char palabra [20];
		printf ("Ingrese cualquier palabra: ");
		gets (palabra);
		n=longitud (palabra);
		printf ("%s tiene %d caracteres\n", palabra, n);
		system ("pause");
		menu ();
	}
	if (op==2)
	{
		char cad[20];
		printf ("Ingrese una cadena de texto: ");
		gets (cad);
		cambio (cad);
		system ("pause");
		menu ();
	}
	if (op==3)
	{
		printf ("Ingrese un numero: ");
		scanf ("%d", &n);
		LeerCadena (n);
		system ("pause");
		menu ();
	}
	if (op==4)
	{
		char cad [20];
		printf ("Ingrese cualquier palabra: ");
		gets (cad);
		char c;
		printf ("Ingrese una letra: ");
		scanf ("%c", &c);
		UnirC (cad, c);
		system ("pause");
		menu ();
	}
	if (op==5)
	{
		char cad [20];
		printf ("Ingrese la cadena de texto: ");
		gets (cad);
		invertir1 (cad);
		system ("pause");
		menu ();
	}
	if (op==6)
	{
		char cad[20];
		printf ("Ingrese la cadena de texto: ");
		gets (cad);
		invertir (cad);
		system ("pause");
		menu ();
	}
	if (op==7)
	{
		char cad [20];
		printf ("Ingrese la primera cadena de texto: ");
		gets (cad);
		char cad2 [20];
		printf ("Ingrese la segunda cadena de texto: ");
		gets (cad2);
		concatenar (cad, cad2);
		system ("pause");
		menu ();
	}
	if (op==8)
	{
		char cad [20];
		printf ("Ingrese una cadena de texto: ");
		gets (cad);
		contar (cad);
		system ("pause");
		menu ();
	}
	if (op==9)
	{
		char cad [20];
		printf ("Ingrese la cadena de texto: ");
		gets (cad);
		takev (cad);
		system ("pause");
		menu ();
	}
	if (op==10)
	{
		char cad [20];
		printf ("Ingrese la cadena de caracteres numericos: ");
		gets (cad);
		n=num (cad);
		printf ("%d\n", n);
		system ("pause");
		menu ();
	}
	if (op==11)
	{
		char cad[20];
		printf ("Ingrese la cadena de texto: ");
		gets (cad);
		palindrome (cad);
		system ("pause");
		menu ();
	}
	if (op==12)
	{
	    char cad [20];
	    printf ("Ingrese la primera cadena de texto: ");
	    gets (cad);
	    char cad2 [20];
	    printf ("Ingrese la segunda cadena de texto: ");
	    gets (cad2);
	    iguales (cad, cad2);
	    system ("pause");
	    menu ();
	}
	if (op==13)
	{
		char cad [20];
		printf ("Ingrese la primera cadena de texto: ");
		gets (cad);
		char cad2 [20];
		printf ("Ingrese la segunda cadena de texto: ");
		gets (cad2);
		comp (cad, cad2);
		system ("pause");
		menu ();
	}
}
//-------------------------------------------------
main ()
{
    menu ();
}
