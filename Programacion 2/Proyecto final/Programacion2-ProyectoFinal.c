//Proyecto final
//Sergio Moncada Mu�oz - 1089380570
//Programacion 2 - Grupo 4

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <stdbool.h> 

//------------------------------------------------------------------
//Estructura Recibos
struct Recibo
{
	long valor;
	char numero [5], fecha[11], nombre[40], ciudad[25], concepto[50], numero_en_letras [100];	
}; 
struct Recibo recibos [50];
//------------------------------------------------------------------
//Variables globales
int numero_recibos;
char linea[150];
//------------------------------------------------------------------
/*
Nombre subrutina: gotoxy
Tipo: Procedimiento (void)
Objetivo: Mover el cursor de la consola a una posici�n espec�fica en las coordenadas (x, y).
Par�metros:	
	posicion_x: Entero que indica la posici�n horizontal (coordenada x) a la que se desea mover el cursor.
	posicion_y: Entero que indica la posici�n vertical (coordenada y) a la que se desea mover el cursor.
Retorno: Ninguno.
Ejemplo de uso:	
	int x = 10;
	int y = 5;
	gotoxy(x, y);
Notas: Esta funci�n utiliza funciones de la biblioteca de Windows para manipular la posici�n del cursor
en la consola. Aseg�rate de compilar y ejecutar el c�digo en un entorno que admita estas funciones, como
Microsoft Visual Studio en Windows.
*/
void gotoxy(int posicion_x, int posicion_y){
	COORD coord;
	coord.X = posicion_x;
	coord.Y = posicion_y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}
//------------------------------------------------------------------
/*
Nombre subrutina: esquina_1
Tipo: void
Objetivo: Dibujar la esquina superior izquierda en una posici�n espec�fica de la consola.
Par�metros:	
	posicion_x: Entero que indica la posici�n horizontal (coordenada x) de la esquina.
	posicion_y: Entero que indica la posici�n vertical (coordenada y) de la esquina.
Retorno: Ninguno.
Ejemplo de uso:	
	int x = 10;
	int y = 5;
	esquina_1(x, y);
Notas: Esta funci�n utiliza la funci�n "gotoxy" para mover el cursor a la posici�n especificada y
luego imprime el car�cter ASCII 218, que representa la esquina superior izquierda en la tabla de
caracteres.
*/
void esquina_1 (int posicion_x, int posicion_y)
{
	gotoxy (posicion_x, posicion_y);
	printf ("%c", 218);
}
//------------------------------------------------------------------
/*
Nombre subrutina: esquina_2
Tipo: void
Objetivo: Dibujar la esquina superior derecha en una posici�n espec�fica de la consola.
Par�metros:
	posicion_x: Entero que indica la posici�n horizontal (coordenada x) de la esquina.
	posicion_y: Entero que indica la posici�n vertical (coordenada y) de la esquina.
Retorno: Ninguno.
Ejemplo de uso:	
	int x = 20;
	int y = 5;
	esquina_2(x, y);
Notas: Esta funci�n utiliza la funci�n "gotoxy" para mover el cursor a la posici�n especificada y
luego imprime el car�cter ASCII 191, que representa la esquina superior derecha en la tabla de
caracteres.					
*/
void esquina_2 (int posicion_x, int posicion_y)
{
	gotoxy (posicion_x, posicion_y);
	printf ("%c", 191);
}
//------------------------------------------------------------------
/*
Nombre subrutina: esquina_3
Tipo: void
Objetivo: Dibujar la esquina inferior izquierda en una posici�n espec�fica de la consola.
Par�metros:
    posicion_x: Entero que indica la posici�n horizontal (coordenada x) de la esquina.
    posicion_y: Entero que indica la posici�n vertical (coordenada y) de la esquina.
Retorno: Ninguno.
Ejemplo de uso:
    int x = 30;
    int y = 10;
    esquina_3(x, y);
Notas: Esta funci�n utiliza la funci�n "gotoxy" para mover el cursor a la posici�n especificada y
luego imprime el car�cter ASCII 192, que representa la esquina inferior izquierda en la tabla de
caracteres.
*/
void esquina_3 (int posicion_x, int posicion_y)
{
	gotoxy (posicion_x, posicion_y);
	printf ("%c", 192);
}
//------------------------------------------------------------------
/*
Nombre subrutina: esquina_4
Tipo: void
Objetivo: Dibujar la esquina inferior derecha en una posici�n espec�fica de la consola.
Par�metros:
    posicion_x: Entero que indica la posici�n horizontal (coordenada x) de la esquina.
    posicion_y: Entero que indica la posici�n vertical (coordenada y) de la esquina.
Retorno: Ninguno.
Ejemplo de uso:
    int x = 40;
    int y = 15;
    esquina_4(x, y);
Notas: Esta funci�n utiliza la funci�n "gotoxy" para mover el cursor a la posici�n especificada y
luego imprime el car�cter ASCII 217, que representa la esquina inferior derecha en la tabla de
caracteres.
*/
void esquina_4 (int posicion_x, int posicion_y)
{
	gotoxy (posicion_x, posicion_y);
	printf ("%c", 217);
}
//------------------------------------------------------------------
/*
Nombre subrutina: linea_horizontal
Tipo: void
Objetivo: Dibujar una l�nea horizontal en una posici�n espec�fica de la consola.
Par�metros:
    posicion_x: Entero que indica la posici�n horizontal (coordenada x) de inicio de la l�nea.
    posicion_y: Entero que indica la posici�n vertical (coordenada y) de la l�nea.
    longitud: Entero que indica la longitud de la l�nea horizontal.
Retorno: Ninguno.
Ejemplo de uso:
    int x = 5;
    int y = 10;
    int longitud = 15;
    linea_horizontal(x, y, longitud);
Notas: Esta funci�n utiliza la funci�n "gotoxy" para mover el cursor a la posici�n especificada y
luego imprime el car�cter ASCII 196 repetidamente para dibujar la l�nea horizontal. La l�nea se
extender� desde la posici�n indicada hasta la posici�n indicada m�s la longitud especificada.
*/
void linea_horizontal (int posicion_x, int posicion_y, int longitud)
{
	int i;
	i=posicion_x;
	while (i<=posicion_x+longitud)
	{
		gotoxy(i, posicion_y);
		printf("%c",196);
		i++;
	}
}
//------------------------------------------------------------------
/*
Nombre subrutina: linea_vertical
Tipo: void
Objetivo: Dibujar una l�nea vertical en una posici�n espec�fica de la consola.
Par�metros:
    posicion_x: Entero que indica la posici�n horizontal (coordenada x) de la l�nea.
    posicion_y: Entero que indica la posici�n vertical (coordenada y) de inicio de la l�nea.
    longitud: Entero que indica la longitud de la l�nea vertical.
Retorno: Ninguno.
Ejemplo de uso:
    int x = 10;
    int y = 5;
    int longitud = 10;
    linea_vertical(x, y, longitud);
Notas: Esta funci�n utiliza la funci�n "gotoxy" para mover el cursor a la posici�n especificada y luego imprime el car�cter ASCII 179 repetidamente para dibujar la l�nea vertical. La l�nea se extender� desde la posici�n indicada hasta la posici�n indicada m�s la longitud especificada.
*/
void linea_vertical (int posicion_x, int posicion_y, int longitud)
{
	int i;
	i=posicion_y;
	while (i<=posicion_y+longitud)
	{
		gotoxy(posicion_x, i);
		printf("%c",179);
		i++;
	}
}
//------------------------------------------------------------------
/*
Nombre subrutina: cuadro
Tipo: void
Objetivo: Dibujar un cuadro en la consola delimitado por las coordenadas de inicio y fin.
Par�metros:
    x_inicial: Entero que indica la posici�n horizontal (coordenada x) de inicio del cuadro.
    y_inicial: Entero que indica la posici�n vertical (coordenada y) de inicio del cuadro.
    x_final: Entero que indica la posici�n horizontal (coordenada x) de fin del cuadro.
    y_final: Entero que indica la posici�n vertical (coordenada y) de fin del cuadro.
Retorno: Ninguno.
Ejemplo de uso:
    int xInicial = 5;
    int yInicial = 5;
    int xFinal = 15;
    int yFinal = 10;
    cuadro(xInicial, yInicial, xFinal, yFinal);
Notas: Esta funci�n utiliza las funciones "linea_horizontal", "linea_vertical", "esquina_1",
"esquina_2", "esquina_3" y "esquina_4" para dibujar un cuadro en la consola. Se dibujan las
l�neas horizontales y verticales en las posiciones correspondientes, y se dibujan las esquinas
utilizando los caracteres ASCII 218, 191, 192 y 217. Los par�metros x_inicial, y_inicial,
x_final e y_final definen las coordenadas de inicio y fin del cuadro.
*/
void cuadro (int x_inicial, int y_inicial, int x_final, int y_final)
{
		linea_horizontal (x_inicial+1, y_inicial, x_final-x_inicial-2);
		linea_horizontal (x_inicial+1, y_final, x_final-x_inicial-2);
		linea_vertical (x_inicial, y_inicial+1, y_final-y_inicial-2);
		linea_vertical (x_final, y_inicial+1, y_final-y_inicial-2);
		esquina_1 (x_inicial, y_inicial);
		esquina_2 (x_final, y_inicial);
		esquina_3 (x_inicial, y_final);
		esquina_4 (x_final, y_final);	
}
//------------------------------------------------------------------
/*
Nombre subrutina: estilo_recibos
Tipo: void
Objetivo: Dibujar un estilo de recibo en una posici�n espec�fica de la consola.
Par�metros:
    posicion_x: Entero que indica la posici�n horizontal (coordenada x) del recibo.
    posicion_y: Entero que indica la posici�n vertical (coordenada y) del recibo.
Retorno: Ninguno.
Ejemplo de uso:
    int x = 10;
    int y = 5;
    estilo_recibos(x, y);
Notas: Esta funci�n utiliza las funciones "cuadro", "linea_horizontal", "linea_vertical",
"esquina_1" y "esquina_3" para dibujar un estilo de recibo en la consola. Se dibuja un
cuadro en la posici�n indicada y se a�aden l�neas horizontales y verticales para dividir
el recibo en secciones. Se colocan etiquetas para indicar los campos correspondientes
dentro del recibo.
*/
void estilo_recibos (int posicion_x, int posicion_y)
{
	int i;
	cuadro (posicion_x, posicion_y, posicion_x+55, posicion_y+21);
	for (i=1; i<7; i++)
	{
		linea_horizontal (posicion_x+1, posicion_y+(3*i), 53);
	}
	linea_vertical (posicion_x+26, posicion_y+1, 1);
	esquina_1 (posicion_x+26, posicion_y);
	esquina_3 (posicion_x+26, posicion_y+3);
	linea_vertical (posicion_x+37, posicion_y+1, 4);
	esquina_1 (posicion_x+37, posicion_y);
	esquina_3 (posicion_x+37, posicion_y+6);
	
	gotoxy (posicion_x+1, posicion_y+1);
	printf ("Ciudad");
	gotoxy (posicion_x+27, posicion_y+1);
	printf ("DD-MM-AAAA");
	gotoxy (posicion_x+29, posicion_y+2);
	printf ("Fecha");
	gotoxy (posicion_x+38, posicion_y+1);
	printf ("No. XXXX");
	gotoxy (posicion_x+38, posicion_y+4);
	printf ("Valor $");
	gotoxy (posicion_x+1, posicion_y+4);
	printf ("Pagado a"); 
	gotoxy (posicion_x+1, posicion_y+7);
	printf ("Concepto");
	gotoxy (posicion_x+1, posicion_y+16);
	printf ("Valor (en letras)");
}
//------------------------------------------------------------------
/*
Nombre subrutina: ubicacion_datos
Tipo: void
Objetivo: Mostrar los datos de un recibo en una ubicaci�n espec�fica de la consola.
Par�metros:
    recibos: Arreglo de estructuras Recibo que contiene los datos de los recibos.
    posicion_x: Entero que indica la posici�n horizontal (coordenada x) de los datos del recibo.
    posicion_y: Entero que indica la posici�n vertical (coordenada y) de los datos del recibo.
    numero_estructura: Entero que indica el �ndice de la estructura de recibo a mostrar.
Retorno: Ninguno.
Ejemplo de uso:
    struct Recibo recibos[10]; // Suponiendo un arreglo de estructuras de recibo
    int x = 10;
    int y = 5;
    int numeroEstructura = 0;
    ubicacion_datos(recibos, x, y, numeroEstructura);
Notas: Esta funci�n utiliza la funci�n "gotoxy" para posicionar el cursor en las ubicaciones
espec�ficas de la consola y muestra los datos correspondientes de la estructura de recibo
indicada. Se muestra el n�mero, la fecha, el nombre, el valor, la ciudad, el concepto y el valor
en letras del recibo en las ubicaciones especificadas.
*/
void ubicacion_datos (struct Recibo recibos[], int posicion_x, int posicion_y, int numero_estructura)
{
	gotoxy (posicion_x+42, posicion_y+1);
	printf ("%s\n", recibos[numero_estructura].numero);
	gotoxy (posicion_x+27, posicion_y+1);
	printf ("%s\n", recibos[numero_estructura].fecha);
	gotoxy (posicion_x+10, posicion_y+4);
	printf ("%s\n", recibos[numero_estructura].nombre);
	gotoxy (posicion_x+45, posicion_y+4);
	printf ("%ld\n", recibos[numero_estructura].valor);
	gotoxy (posicion_x+8, posicion_y+1);
	printf ("%s\n", recibos[numero_estructura].ciudad);
	gotoxy (posicion_x+10, posicion_y+7);
	printf ("%s\n", recibos[numero_estructura].concepto);
	
	if (strlen (recibos[numero_estructura].numero_en_letras) <= 53)
	{
		gotoxy (posicion_x+1, posicion_y+17);
		printf ("%s", recibos[numero_estructura].numero_en_letras);
	}
	else if (strlen (recibos[numero_estructura].numero_en_letras) > 53)
	{
		int i, ubicacion_espacio;
		for (i=53; i>0; i--)
		{
			if (recibos[numero_estructura].numero_en_letras[i] == ' ')
			{
				ubicacion_espacio = i;
				break;
			}
		}
		for (i=0; i<ubicacion_espacio; i++)
		{
			gotoxy (posicion_x+1+i, posicion_y+17);
			printf ("%c", recibos[numero_estructura].numero_en_letras [i]);
		}
		for (i=ubicacion_espacio+1; i<strlen(recibos[numero_estructura].numero_en_letras); i++)
		{
			gotoxy (posicion_x+i-ubicacion_espacio, posicion_y+19);
			printf ("%c", recibos[numero_estructura].numero_en_letras [i]);
		}
	}
	printf ("\n\n\n\n\n\n");
}
//------------------------------------------------------------------
/*
Nombre subrutina: estilo_menu
Tipo: void
Objetivo: Dibujar un estilo de men� en la parte superior de la consola.
Par�metros: Ninguno.
Retorno: Ninguno.
Ejemplo de uso:
    estilo_menu();
Notas: Esta funci�n utiliza las funciones "cuadro" y "linea_horizontal" para dibujar un estilo
de men� en la parte superior de la consola. Se dibuja un cuadro con dimensiones predefinidas y
se a�ade una l�nea horizontal para separar el t�tulo del men� del resto de la consola.
*/
void estilo_menu ()
{
	cuadro (0, 0, 33, 9);
	linea_horizontal (1, 2, 31);
}
//------------------------------------------------------------------
/*
Nombre subrutina: estilo_lista
Tipo: void
Objetivo: Dibujar un estilo de lista en la consola.
Par�metros: Ninguno.
Retorno: Ninguno.
Ejemplo de uso:
    estilo_lista();
Notas: Esta funci�n utiliza las funciones "cuadro" y "linea_horizontal" para dibujar un estilo
de lista en la consola. Se dibuja un cuadro con dimensiones predefinidas y se a�ade una l�nea
horizontal para separar la lista del resto de la consola. El n�mero de filas en la lista se
determina por la variable "numero_recibos".
*/
void estilo_lista ()
{
	cuadro (0, 0, 103, numero_recibos+3);
	linea_horizontal (1, 2, 101);
}
//------------------------------------------------------------------
/*
Nombre subrutina: escribir_numero_en_letras
Tipo: void
Objetivo: Convertir un n�mero entero en su representaci�n en letras.
Par�metros:
    numero: N�mero entero a convertir.
    resultado: Puntero a un arreglo de caracteres donde se almacenar� el resultado.
    tamano: Entero que indica el tama�o m�ximo del arreglo "resultado".
Retorno: Ninguno.
Ejemplo de uso:
    long num = 12345;
    char resultado[100];
    escribir_numero_en_letras(num, resultado, sizeof(resultado));
Notas: Esta funci�n recibe un n�mero entero y lo convierte en su representaci�n en letras en
idioma espa�ol. El resultado se almacena en el arreglo de caracteres "resultado". El tama�o
m�ximo del arreglo se especifica en el par�metro "tamano". En caso de que el n�mero est� fuera
del rango v�lido (0 a 999,999,999), se almacenar� un mensaje indicando que el n�mero est� fuera
de rango en el arreglo "resultado".
*/
void escribir_numero_en_letras(long numero, char* resultado, int tamano) {
    const char* unidades[] = {"cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"};
    const char* especiales[] = {"diez", "once", "doce", "trece", "catorce", "quince", "diecis�is", "diecisiete", "dieciocho", "diecinueve"};
    const char* decenas[] = {"", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"};
    const char* centenas[] = {"", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"};
    const char* miles[] = {"", "mil", "millon", "millones"};

    if (numero < 0 || numero > 999999999) {
        strncpy(resultado, "Numero fuera de rango", tamano);
        return;
    }

    if (numero < 10) {
        strncpy(resultado, unidades[numero], tamano);
    } else if (numero < 20) {
        strncpy(resultado, especiales[numero - 10], tamano);
    } else if (numero < 100) {
        int decena = numero / 10;
        int unidad = numero % 10;
        if (unidad == 0) {
            strncpy(resultado, decenas[decena], tamano);
        } else {
            snprintf(resultado, tamano, "%s y %s", decenas[decena], unidades[unidad]);
        }
    } else if (numero < 1000) {
        int centena = numero / 100;
        int decena = (numero % 100) / 10;
        int unidad = numero % 10;
        if (decena == 0 && unidad == 0) {
            strncpy(resultado, centenas[centena], tamano);
        } else {
            char temp_resultado[100];
            escribir_numero_en_letras(numero % 100, temp_resultado, sizeof(temp_resultado));
            snprintf(resultado, tamano, "%s %s", centenas[centena], temp_resultado);
        }
    } else if (numero < 1000000) {
        int mil = numero / 1000;
        int centena = (numero % 1000) / 100;
        int decena = (numero % 100) / 10;
        int unidad = numero % 10;
        if (mil == 1 && centena == 0 && decena == 0 && unidad == 0) {
            strncpy(resultado, "mil", tamano);
        } else {
            char temp_resultado1[100];
            char temp_resultado2[100];
            escribir_numero_en_letras(mil, temp_resultado1, sizeof(temp_resultado1));
            if (numero % 1000 == 0) {
                snprintf(resultado, tamano, "%s mil", temp_resultado1);
            } else {
                escribir_numero_en_letras(numero % 1000, temp_resultado2, sizeof(temp_resultado2));
                snprintf(resultado, tamano, "%s mil %s", temp_resultado1, temp_resultado2);
            }
        }
    } else if (numero < 1000000000) {
        int millon = numero / 1000000;
        int mil = (numero % 1000000) / 1000;
        int centena = (numero % 1000) / 100;
        int decena = (numero % 100) / 10;
        int unidad = numero % 10;
        if (millon == 1 && mil == 0 && centena == 0 && decena == 0 && unidad == 0) {
            strncpy(resultado, "un millon", tamano);
        } else {
            char temp_resultado1[100];
            char temp_resultado2[100];
            escribir_numero_en_letras(millon, temp_resultado1, sizeof(temp_resultado1));
            if (numero % 1000000 == 0) {
                snprintf(resultado, tamano, "%s millones", temp_resultado1);
            } else {
                escribir_numero_en_letras(numero % 1000000, temp_resultado2, sizeof(temp_resultado2));
                snprintf(resultado, tamano, "%s millones %s", temp_resultado1, temp_resultado2);
            }
        }
    } else {
        strncpy(resultado, "Numero fuera de rango", tamano);
    }
}
//------------------------------------------------------------------
/*
Nombre subrutina: leer_archivo
Tipo: void
Objetivo: Leer un archivo de texto que contiene informaci�n de recibos y almacenar los datos en
una estructura.
Par�metros: Ninguno.
Retorno: Ninguno.
Ejemplo de uso: leer_archivo();
Notas: Esta funci�n lee el archivo de texto "Recibos.txt" y extrae la informaci�n de cada l�nea
para almacenarla en la estructura "recibos". El archivo debe tener un formato espec�fico, donde
cada l�nea representa un recibo y los datos est�n separados por el delimitador ";". Los datos se
asignan a los campos correspondientes en la estructura "recibos". Adem�s, se utiliza la funci�n
"escribir_numero_en_letras" para convertir el valor del recibo en letras y almacenarlo en el campo
"numero_en_letras" de la estructura. Si el archivo no se puede abrir, se muestra un mensaje de error.
*/
void leer_archivo ()
{
	FILE *archivo = fopen ("Recibos.txt", "r");
	if (archivo == NULL)
	{
		printf ("No se pudo abrir el archivo\n");
	}
	else
	{
			numero_recibos=0;
	while (fgets (linea, 100, archivo) != NULL)
	{
		char *delimitador;
		delimitador = strtok (linea, ";");
		strcpy (recibos[numero_recibos].numero, delimitador);
		delimitador=strtok(NULL, ";");
		strcpy (recibos[numero_recibos].fecha, delimitador);
		delimitador=strtok(NULL, ";");
		strcpy (recibos[numero_recibos].nombre, delimitador);
		delimitador=strtok(NULL, ";");
		recibos[numero_recibos].valor = atol(delimitador);
		delimitador=strtok(NULL, ";");
		strcpy (recibos[numero_recibos].ciudad, delimitador);
		delimitador=strtok(NULL, ";");
		strcpy (recibos[numero_recibos].concepto, delimitador);
		
		escribir_numero_en_letras (recibos[numero_recibos].valor, recibos[numero_recibos].numero_en_letras, sizeof(recibos[numero_recibos].numero_en_letras));
		
		numero_recibos++;
	}
	fclose (archivo);
	}
}
//-------------------------------------------------------------
/*
Nombre subrutina: fecha_valida
Tipo: bool
Objetivo: Verificar si una fecha es v�lida.
Par�metros:
  - fecha: cadena de caracteres que representa la fecha en formato "DD-MM-AAAA".
Retorno: Valor booleano que indica si la fecha es v�lida (true) o no (false).
Ejemplo de uso: bool es_valida = fecha_valida("25-06-2023");
Notas: Esta funci�n verifica si una fecha es v�lida comprobando que el d�a, mes y a�o se encuentren
dentro de los rangos permitidos. Adem�s, se tienen en cuenta las reglas de los meses con 30 o 31 d�as,
y la verificaci�n de los a�os bisiestos en el mes de febrero. Si la fecha es v�lida, la funci�n
devuelve true; de lo contrario, devuelve false.
*/
bool fecha_valida (const char fecha [])
{
	int dia = (fecha[0] - '0') * 10 + (fecha[1] - '0');
    int mes = (fecha[3] - '0') * 10 + (fecha[4] - '0');
    int year = (fecha[6] - '0') * 1000 + (fecha[7] - '0') * 100 + (fecha[8] - '0') * 10 + (fecha[9] - '0');

    if (dia < 1 || dia > 31 || mes < 1 || mes > 12 || year < 0 || year >2023) {
        return false;
    }

    if ((mes == 4 || mes == 6 || mes == 9 || mes == 11) && dia > 30) {
        return false;
    }

    if (mes == 2) {
        bool bisiesto = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
        if (bisiesto && dia > 29) {
            return false;
        } else if (!bisiesto && dia > 28) {
            return false;
        }
    }
    return true;
}
//-------------------------------------------------------------
/*
Nombre subrutina: comparar_numero
Tipo: int
Objetivo: Comparar un n�mero ingresado con los n�meros de los recibos existentes.
Par�metros:
  - recibos: arreglo de estructuras de tipo Recibo.
  - numero_ingresado: n�mero ingresado a comparar.
Retorno:
  - Entero que representa la posici�n del recibo en el arreglo recibos si se encuentra una coincidencia.
  - -1 si no se encuentra ninguna coincidencia.
Ejemplo de uso: int posicion = comparar_numero(recibos, numero_ingresado);
Notas: Esta funci�n recorre el arreglo de recibos y compara el n�mero ingresado con los n�meros de los
recibos existentes. Si encuentra una coincidencia, retorna la posici�n del recibo en el arreglo. En caso
contrario, retorna -1.
*/
int comparar_numero (struct Recibo recibos [], char numero_ingresado[5])
{
	int i;
	for (i=0; i<numero_recibos; i++)
	{
		if (strcmp (numero_ingresado, recibos[i].numero) == 0)
		{
			return i;
		}
	}
	return -1;
}
//--------------------------------------------------------------
/*
Nombre subrutina: asignar_datos
Tipo: void
Objetivo: Asignar datos a una estructura de tipo Recibo.
Par�metros:
  - recibos: arreglo de estructuras de tipo Recibo.
  - numero_a_asignar: entero que indica la posici�n en el arreglo donde se asignar�n los datos.
  - posicion_x: entero que indica la posici�n horizontal en la pantalla donde se mostrar�n los campos.
  - posicion_y: entero que indica la posici�n vertical en la pantalla donde se mostrar�n los campos.
Retorno: Ninguno.
Ejemplo de uso: asignar_datos(recibos, 0, 10, 20);
Notas: Esta funci�n permite ingresar datos para asignarlos a una estructura de tipo Recibo en la posici�n
especificada del arreglo. Los campos que se solicitan son: n�mero, fecha, nombre, valor, ciudad y concepto.
Adem�s, se verifica que la fecha ingresada sea v�lida utilizando la funci�n fecha_valida. La funci�n tambi�n
utiliza la funci�n escribir_numero_en_letras para convertir el valor num�rico a su representaci�n en letras.
*/
void asignar_datos (struct Recibo recibos [], int numero_a_asignar, int posicion_x, int posicion_y)
{
	if (numero_a_asignar == numero_recibos)
	{
		do
		{
			gotoxy (posicion_x+42, posicion_y+1);
			printf ("XXXX");
			gotoxy (posicion_x+42, posicion_y+1);
			printf ("");
			fflush (stdin);
			gets (recibos[numero_a_asignar].numero);
			if (strlen(recibos[numero_a_asignar].numero)>4)
			{
				recibos[numero_a_asignar].numero [4] = '\0';
			}
			gotoxy (posicion_x+1, posicion_y+22);
			printf ("El numero que ingreso ya se encuentra registrado");
		}while (comparar_numero(recibos, recibos[numero_a_asignar].numero) != -1);
		gotoxy (posicion_x+1, posicion_y+22);
		printf ("                                                 ");
	}
	else if (numero_a_asignar<numero_recibos)
	{
		char numero_actual [5];
		strcpy (numero_actual, recibos[numero_a_asignar].numero);
		do
		{			
			gotoxy (posicion_x+42, posicion_y+1);
			printf ("XXXX");
			gotoxy (posicion_x+42, posicion_y+1);
			printf ("");
			fflush (stdin);
			gets (recibos[numero_a_asignar].numero);
			if (strlen(recibos[numero_a_asignar].numero)>4)
			{
				recibos[numero_a_asignar].numero [4] = '\0';
			}
			if (strcmp (numero_actual, recibos[numero_a_asignar].numero) == 0)
			{
				break;
			}
			gotoxy (posicion_x+1, posicion_y+22);
			printf ("El numero que ingreso ya se encuentra registrado");
			}while (comparar_numero(recibos, recibos[numero_a_asignar].numero) != -1);
			gotoxy (posicion_x+1, posicion_y+22);
			printf ("                                                 ");	
	}
		
	do
	{
		gotoxy (posicion_x+27, posicion_y+1);
		printf ("DD-MM-AAAA");
		gotoxy (posicion_x+27, posicion_y+1);
		printf ("");
		fflush (stdin);
		gets (recibos[numero_a_asignar].fecha);
		if (strlen(recibos[numero_a_asignar].fecha)>10)
		{
			recibos[numero_a_asignar].fecha [10] = '\0';
		}
		if (!fecha_valida (recibos[numero_a_asignar].fecha))
		{
			gotoxy (posicion_x+1, posicion_y+22);
			printf ("La fecha que ingreso no es valida (DD-MM-AAAA)");
		}
	}while (!fecha_valida (recibos[numero_a_asignar].fecha));
	gotoxy (posicion_x+1, posicion_y+22);
	printf ("                                                      ");

	gotoxy (posicion_x+10, posicion_y+4);
	printf ("");
	fflush (stdin);
	gets (recibos[numero_a_asignar].nombre);
	if (strlen(recibos[numero_a_asignar].nombre)>28)
	{
		recibos[numero_a_asignar].nombre [28] = '\0';
	}
	
	gotoxy (posicion_x+45, posicion_y+4);
	printf ("");
	scanf ("%ld", &recibos[numero_a_asignar].valor);
	
	escribir_numero_en_letras (recibos[numero_a_asignar].valor, recibos[numero_a_asignar].numero_en_letras, sizeof(recibos[numero_a_asignar].numero_en_letras));
	if (strlen (recibos[numero_a_asignar].numero_en_letras) <= 53)
	{
		gotoxy (posicion_x+1, posicion_y+17);
		printf ("%s", recibos[numero_a_asignar].numero_en_letras);
	}
	else if (strlen (recibos[numero_a_asignar].numero_en_letras) > 53)
	{
		int i, ubicacion_espacio;
		for (i=53; i>0; i--)
		{
			if (recibos[numero_a_asignar].numero_en_letras[i] == ' ')
			{
				ubicacion_espacio = i;
				break;
			}
		}
		for (i=0; i<ubicacion_espacio; i++)
		{
			gotoxy (posicion_x+1+i, posicion_y+17);
			printf ("%c", recibos[numero_a_asignar].numero_en_letras [i]);
		}
		for (i=ubicacion_espacio+1; i<strlen(recibos[numero_a_asignar].numero_en_letras); i++)
		{
			gotoxy (posicion_x+i-ubicacion_espacio, posicion_y+19);
			printf ("%c", recibos[numero_a_asignar].numero_en_letras [i]);
		}
	}
	
	gotoxy (posicion_x+7, posicion_y+1);
	printf (" ");
	fflush (stdin);
	gets (recibos[numero_a_asignar].ciudad);
	if (strlen(recibos[numero_a_asignar].ciudad)>24)
	{
		recibos[numero_a_asignar].ciudad [24] = '\0';
	}
	
	gotoxy (posicion_x+10, posicion_y+7);
	printf ("");
	fflush (stdin);
	gets (recibos[numero_a_asignar].concepto);
	if (strlen(recibos[numero_a_asignar].concepto)>49)
	{
		recibos[numero_a_asignar].concepto [49] = '\0';
	}
	printf ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
}
//-------------------------------------------------------------
/*
Nombre subrutina: agregar_recibo
Tipo: void
Objetivo: Agregar un nuevo recibo al arreglo de recibos.
Par�metros:
  - recibos: arreglo de estructuras de tipo Recibo.
Retorno: Ninguno.
Ejemplo de uso: agregar_recibo(recibos);
Notas: Esta funci�n permite agregar un nuevo recibo al arreglo de recibos. Primero se limpia la pantalla,
luego se aplica el estilo de los recibos utilizando la funci�n estilo_recibos. A continuaci�n, se utiliza
la funci�n asignar_datos para ingresar los datos del nuevo recibo en la posici�n indicada por el
n�mero_recibos actual. Finalmente, se incrementa el n�mero_recibos en 1.
*/
void agregar_recibo (struct Recibo recibos [])
{
	system ("cls");
	estilo_recibos (2, 1);
	asignar_datos (recibos, numero_recibos, 2, 1);
	numero_recibos++;
}
//--------------------------------------------------------------
/*
Nombre subrutina: consultar_recibo
Tipo: void
Objetivo: Consultar un recibo a partir de un n�mero ingresado.
Par�metros:
  - recibos: arreglo de estructuras de tipo Recibo.
  - numero_ingresado: n�mero del recibo a consultar.
Retorno: Ninguno.
Ejemplo de uso: consultar_recibo(recibos, numero_ingresado);
Notas: Esta funci�n consulta un recibo a partir del n�mero ingresado. Primero verifica si el n�mero existe
en los recibos registrados utilizando la funci�n comparar_numero. Si el n�mero existe, muestra los datos del
recibo utilizando la funci�n ubicacion_datos. En caso contrario, muestra un mensaje indicando que el n�mero
no est� registrado.
*/
void consultar_recibo (struct Recibo recibos [], char numero_ingresado [5])
{
	system ("cls");
	int numero_estructura;
	numero_estructura = comparar_numero (recibos, numero_ingresado);
	if (numero_estructura == -1)
	{
		printf ("El numero que ingreso no esta registrado\n\n");
	}
	else
	{
		estilo_recibos (2, 1);
		ubicacion_datos (recibos, 2, 1, numero_estructura);
	}
}
//-------------------------------------------------------------
/*
Nombre subrutina: modificar_recibo
Tipo: void
Objetivo: Modificar los datos de un recibo a partir de un n�mero ingresado.
Par�metros:
  - recibos: arreglo de estructuras de tipo Recibo.
  - numero_ingresado: n�mero del recibo a modificar.
Retorno: Ninguno.
Ejemplo de uso: modificar_recibo(recibos, numero_ingresado);
Notas: Esta funci�n modifica los datos de un recibo a partir del n�mero ingresado. Primero verifica si el
n�mero existe en los recibos registrados utilizando la funci�n comparar_numero. Si el n�mero existe,
muestra los datos actuales del recibo y luego solicita los nuevos datos utilizando la funci�n asignar_datos.
Los nuevos datos se asignan a la misma posici�n en el arreglo de recibos.
*/
void modificar_recibo (struct Recibo recibos [], char numero_ingresado [5])
{
	system ("cls");
	int numero_estructura;
	numero_estructura = comparar_numero (recibos, numero_ingresado);
	if (numero_estructura == -1)
	{
		printf ("El numero que ingreso no esta registrado\n\n");
	}
	else
	{
		gotoxy (1, 0);
		printf ("Datos actuales del recibo:");
		estilo_recibos (1, 1);
		ubicacion_datos (recibos, 1, 1, numero_estructura);
		gotoxy (63, 0);
		printf ("Datos nuevos del recibo:");
		estilo_recibos (63, 1);
		asignar_datos (recibos, numero_estructura, 63, 1);
	}
}
//-------------------------------------------------------------
/*
Nombre subrutina: total_valores
Tipo: long
Objetivo: Calcular el total de los valores de los recibos registrados.
Par�metros:
  - recibos: arreglo de estructuras de tipo Recibo.
Retorno: El total de los valores de los recibos registrados.
Ejemplo de uso: long total = total_valores(recibos);
Notas: Esta funci�n calcula el total de los valores de los recibos registrados. Itera sobre el arreglo de
recibos y suma los valores de cada recibo. Retorna el resultado total.
*/
long total_valores (struct Recibo recibos [])
{
	long total;
	int i;
	for (i=0; i<numero_recibos; i++)
	{
		total = total + recibos[i].valor;
	}
	return total;
}
//-------------------------------------------------------------
/*
Nombre subrutina: valor_maximo
Tipo: int
Objetivo: Obtener la ubicaci�n del recibo con el valor m�ximo.
Par�metros:
  - recibos: arreglo de estructuras de tipo Recibo.
Retorno: La ubicaci�n del recibo con el valor m�ximo en el arreglo.
Ejemplo de uso: int ubicacion = valor_maximo(recibos);
Notas: Esta funci�n recorre el arreglo de recibos y busca el recibo con el valor m�ximo. Retorna la
ubicaci�n (�ndice) de ese recibo en el arreglo. En caso de empate, retorna la primera ubicaci�n encontrada.
*/
int valor_maximo (struct Recibo recibos [])
{
	int i=1, ubicacion_parcial=0;
	long maximo_parcial = recibos[0].valor;
	while (i<numero_recibos)
	{
		if (recibos[i].valor > maximo_parcial)
		{
			maximo_parcial = recibos[i].valor;
			ubicacion_parcial = i;
		}
		i++;
	}
	return ubicacion_parcial;
}
//-------------------------------------------------------------
/*
Nombre subrutina: valor_minimo
Tipo: int
Objetivo: Obtener la ubicaci�n del recibo con el valor m�nimo.
Par�metros:
  - recibos: arreglo de estructuras de tipo Recibo.
Retorno: La ubicaci�n del recibo con el valor m�nimo en el arreglo.
Ejemplo de uso: int ubicacion = valor_minimo(recibos);
Notas: Esta funci�n recorre el arreglo de recibos y busca el recibo con el valor m�nimo. Retorna la
ubicaci�n (�ndice) de ese recibo en el arreglo. En caso de empate, retorna la primera ubicaci�n encontrada.
*/
int valor_minimo (struct Recibo recibos [])
{
	int i=1, ubicacion_parcial=0;
	long minimo_parcial = recibos[0].valor;
	while (i<numero_recibos)
	{
		if (recibos[i].valor < minimo_parcial)
		{
			minimo_parcial = recibos[i].valor;
			ubicacion_parcial = i;
		}
		i++;
	}
	return ubicacion_parcial;
}
//-------------------------------------------------------------
/*
Nombre subrutina: mostrar_lista_recibos
Tipo: void
Objetivo: Mostrar en pantalla la lista de recibos registrados.
Par�metros: Ninguno.
Retorno: Ninguno.
Ejemplo de uso: mostrar_lista_recibos();
Notas: Esta funci�n muestra en pantalla la lista de recibos registrados. Imprime cada uno de los campos
de los recibos, incluyendo el n�mero, la fecha, el beneficiario, el valor y la ciudad. Adem�s, calcula y
muestra el total de los valores de los recibos, el recibo con el valor m�ximo y el recibo con el valor m�nimo.
*/
void mostrar_lista_recibos ()
{
	system ("cls");
	estilo_lista ();
	gotoxy (1, 1);
	printf ("# RC");
	gotoxy (14, 1);
	printf ("Fecha");
	gotoxy (33, 1);
	printf ("Pagado a");
	gotoxy (65, 1);
	printf ("Valor");
	gotoxy (83, 1);
	printf ("Ciudad");
	
	int i;
	for (i=0; i<numero_recibos; i++)
	{
		gotoxy (1, 3+i);
		printf ("%s", recibos[i].numero);
		gotoxy (14, 3+i);
		printf ("%s", recibos[i].fecha);
		gotoxy (33, 3+i);
		printf ("%s", recibos[i].nombre);
		gotoxy (65, 3+i);
		printf ("$%ld", recibos[i].valor);
		gotoxy (83, 3+i);
		printf ("%s", recibos[i].ciudad);
	}
	long total;
	total = total_valores (recibos);
	gotoxy (1, numero_recibos+4);
	printf ("Total: $%ld", total);
	
	int ubicacion_maximo;
	ubicacion_maximo = valor_maximo (recibos);
	gotoxy (1, numero_recibos+5);
	printf ("Valor m%cximo: No. %s   Valor $%ld", 160, recibos[ubicacion_maximo].numero, recibos[ubicacion_maximo].valor);
	
	int ubicacion_minimo;
	ubicacion_minimo = valor_minimo (recibos);
	gotoxy (1, numero_recibos+6);
	printf ("Valor m%cnimo: No. %s   Valor $%ld", 161, recibos[ubicacion_minimo].numero, recibos[ubicacion_minimo].valor);
	
	gotoxy (1, numero_recibos+8);
	system ("pause");
}
//------------------------------------------------------------
/*
Nombre subrutina: guardar_datos
Tipo: void
Objetivo: Guardar los datos de los recibos en un archivo de texto.
Par�metros:
  - recibos: arreglo de estructuras de tipo Recibo.
Retorno: Ninguno.
Ejemplo de uso: guardar_datos(recibos);
Notas: Esta funci�n guarda los datos de los recibos en un archivo de texto llamado "Recibos.txt". Abre el archivo
en modo escritura y, si la apertura es exitosa, itera sobre el arreglo de recibos y escribe cada campo de los recibos
en el archivo, separados por punto y coma. Cada recibo se escribe en una nueva l�nea. Finalmente, cierra el archivo.
*/
void guardar_datos (struct Recibo recibos [])
{
	FILE *archivo = fopen ("Recibos.txt", "w");
	if (archivo == NULL)
	{
		printf ("No se pudo abrir el archivo\n");
	}
	else 
	{
		int i;
		for (i=0; i<numero_recibos; i++)
		{
			fputs (recibos[i].numero, archivo);
			fputc (';', archivo);
			fputs (recibos[i].fecha, archivo);
			fputc (';', archivo);
			fputs (recibos[i].nombre, archivo);
			fputc (';', archivo);
			fprintf (archivo, "%ld", recibos[i].valor);
			fputc (';', archivo);
			fputs (recibos[i].ciudad, archivo);
			fputc (';', archivo);
			fputs (recibos[i].concepto, archivo);
			fputc (';', archivo);
			fputc ('\n', archivo);
		}
		fclose (archivo);
	}
}
//------------------------------------------------------------
/*
Nombre subrutina: menu
Tipo: void
Objetivo: Mostrar el men� principal y gestionar las opciones seleccionadas por el usuario.
Par�metros: Ninguno.
Retorno: Ninguno.
Ejemplo de uso: menu();
Notas: Esta funci�n muestra un men� principal con diferentes opciones y solicita al usuario que ingrese una opci�n.
Luego, seg�n la opci�n seleccionada, ejecuta la funci�n correspondiente o muestra un mensaje de error en caso de opci�n
inv�lida. Las opciones disponibles son:
  1. Capturar Documento: Permite agregar un nuevo recibo llamando a la funci�n agregar_recibo.
  2. Consultar Documento: Solicita al usuario el n�mero de recibo a consultar y llama a la funci�n consultar_recibo.
  3. Listar Documentos: Muestra la lista de todos los recibos registrados llamando a la funci�n mostrar_lista_recibos.
  4. Modificar Documento: Solicita al usuario el n�mero de recibo a modificar y llama a la funci�n modificar_recibo.
  5. Salir: Guarda los datos de los recibos en un archivo de texto llamando a la funci�n guardar_datos y finaliza la
  	ejecuci�n del programa.
Si se ingresa una opci�n inv�lida, se muestra un mensaje de error y se vuelve a mostrar el men� principal.
*/
void menu ()
{
	int opcion;
	system ("cls");
	estilo_menu ();
	gotoxy (1, 1);
	printf ("Men%c principal\n", 163);
	gotoxy (1, 3);
	printf ("1. Capturar Documento\n");
	gotoxy (1, 4);
	printf ("2. Consultar Documento\n");
	gotoxy (1, 5);
	printf ("3. Listar Documentos\n");
	gotoxy (1, 6);
	printf ("4. Modificar Documento\n");
	gotoxy (1, 7);
	printf ("5. Salir\n");
	gotoxy (1, 8);
	fflush(stdin);
	printf ("Ingrese la opci%cn que desea: ", 162);
	scanf ("%d", &opcion);
 	
 	if (opcion>5 || opcion<1)
 	{
 		printf ("\nLa opci%cn que ingres%c no es v%clida\n\n", 162, 162, 160);
 		system ("pause");
 		menu ();
	}
	if (opcion == 1)
	{
		agregar_recibo (recibos);
		system ("pause");
		menu ();
	}
	if (opcion == 2)
	{
		system ("cls");
		char buscar_numero [5];
		printf ("Ingrese el n%cmero del recibo que desea consultar (XXXX): ", 163);
		fflush (stdin);
		gets (buscar_numero);
		consultar_recibo (recibos, buscar_numero);
		system ("pause");
		menu ();
	}
	if (opcion == 3)
	{
		mostrar_lista_recibos ();
		menu ();
	}
	if (opcion == 4)
	{
		system ("cls");
		char buscar_numero [5];
		printf ("Ingrese el n%cmero del recibo que desea modificar (XXXX): ", 163);
		fflush (stdin);
		gets (buscar_numero);
		modificar_recibo (recibos, buscar_numero);
		system ("pause");
		menu ();
	}
	if (opcion == 5)
	{
		guardar_datos (recibos);
	}
}
//------------------------------------------------------------
/*
Nombre funci�n: main
Tipo: int
Objetivo: Punto de entrada del programa.
Retorno: Valor entero que indica el estado de finalizaci�n del programa.
Notas: Esta funci�n es el punto de entrada del programa. Llama a la funci�n leer_archivo() para cargar los datos
existentes desde un archivo. Luego, muestra el men� principal llamando a la funci�n menu() para que el usuario
pueda interactuar con las opciones. Finalmente, retorna 0 para indicar que el programa finaliz� sin errores.
*/
int main ()
{
	leer_archivo ();
	menu ();
	return 0;
}
