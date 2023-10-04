#include <windows.h>
#include <stdio.h>
//------------------------------------------------------------------
void gotoxy(int x, int y){
	COORD coord;
	coord.X = x;
	coord.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}
//------------------------------------------------------------------
void color (int C)
{
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
		SetConsoleTextAttribute(hConsole, C);
}
//------------------------------------------------------------------
void ListaColores()
{
	int i=1;
	while (i<64)
	{
		gotoxy(1,i+1);
		color(i);
		printf("Color %d", i);
		gotoxy(25,i+1);
		color(i+64);
		printf("Color %d", i+64);
		gotoxy(50,i+1);
		color(i+128);
		printf("Color %d", i+128);
		gotoxy(75,i+1);
		color(i+192);
		printf("Color %d", i+192);
		i++;
	}
}
//-------------------------------------------------------------------
void Listaascii()
{
	int i=0;
	while (i<64)
	{
		gotoxy(1,i+1);
		printf("%d : %c \n", i, i);
		gotoxy(25,i+1);
		printf("%d : %c \n", i+64, i+64);
		gotoxy(50,i+1);
		printf("%d : %c \n", i+128, i+128);
		gotoxy(75,i+1);
		printf("%d : %c \n", i+192, i+192);
		i++;
	}
}
//-------------------------------------------------------------------
void lineaH (int x, int y, int tam)
{
	int i;
	i=x;
	while (i<=x+tam)
	{
		gotoxy(i,y);
		printf("%c",196);
		i++;
	}
}
void lineaH2 (int x, int y, int tam)
{
	int i;
	i=x;
	while (i<=x+tam)
	{
		gotoxy(i,y);
		printf("%c",205);
		i++;
	}
}
//---------------------------------------
void lineaV (int x, int y, int tam)
{
	int i;
	i=y;
	while (i<=y+tam)
	{
		gotoxy(x,i);
		printf("%c",179);
		i++;
	}
}
void lineaV2 (int x, int y, int tam)
{
	int i;
	i=y;
	while (i<=y+tam)
	{
		gotoxy(x,i);
		printf("%c",186);
		i++;
	}
}
//------------------------------------------
void esquina1 (int x, int y)
{
	gotoxy (x, y);
	printf ("%c", 218);
}
void esquina2 (int x, int y)
{
	gotoxy (x, y);
	printf ("%c", 191);
}
void esquina3 (int x, int y)
{
	gotoxy (x, y);
	printf ("%c", 192);
}
void esquina4 (int x, int y)
{
	gotoxy (x, y);
	printf ("%c", 217);
}
void esquina5 (int x, int y)
{
	gotoxy (x, y);
	printf ("%c", 201);
}
void esquina6 (int x, int y)
{
	gotoxy (x, y);
	printf ("%c", 187);
}
void esquina7 (int x, int y)
{
	gotoxy (x, y);
	printf ("%c", 200);
}
void esquina8 (int x, int y)
{
	gotoxy (x, y);
	printf ("%c", 188);
}
//-----------------------------------------
void cuadro (int x1, int y1, int x2, int y2, int borde)
{
	if (borde==1)
	{
		lineaH (x1+1, y1, x2-x1-2);
		lineaH (x1+1, y2, x2-x1-2);
		lineaV (x1, y1+1, y2-y1-2);
		lineaV (x2, y1+1, y2-y1-2);
		esquina1 (x1, y1);
		esquina2 (x2, y1);
		esquina3 (x1, y2);
		esquina4 (x2, y2);	
	}
	if (borde==2)
	{
		lineaH2 (x1+1, y1, x2-x1-2);
		lineaH2 (x1+1, y2, x2-x1-2);
		lineaV2 (x1, y1+1, y2-y1-2);
		lineaV2 (x2, y1+1, y2-y1-2);
		esquina5 (x1, y1);
		esquina6 (x2, y1);
		esquina7 (x1, y2);
		esquina8 (x2, y2);
	}
}
//---------------------------------------------
void cuadroR (int x1, int y1, int x2, int y2, int colorRelleno)
{
	int i, i2;
	i2=y1;
	while (i2<=y2)
	{
		i=x1;
		while (i<=x2)
		{
			color (colorRelleno);
			gotoxy (i, i2);
			printf ("%c", 219);
			i++;
		}
		i2++;
	}
}
//---------------------------------------------
void sombraH (int x, int y, int tam, int col)
{
	int i;
	i=y;
	while (i<=tam)
	{
		gotoxy (x+1, i+1);
		color (col);
		printf ("%c", 178);
		i++;
	}
}
void sombraV (int x, int y, int tam, int col)
{
	int i;
	i=x;
	while (i<=tam)
	{
		gotoxy (i+2, y+1);
		color (col);
		printf ("%c", 178);
		i++;
	}
}
//---------------------------------------------
void ventana1 (int x1, int y1, int x2, int y2, int colorfondo, int colorSombra)
{
	int i, i2;
	i=y1;
	i2=x1;
	cuadroR (x1, y1, x2, y2, colorfondo);
	sombraH (x2, y1, y2, colorSombra);
	sombraH (x2+1, y1, y2, colorSombra);
	sombraV (x1, y2, x2, colorSombra);
}
//---------------------------------------------
void renglon (int x, int y, int tam, int col)
{
	int i;
	i=x;
	while (i<=tam)
	{
		gotoxy (i, y);
		color (col);
		printf ("%c", 219);
		i++;
	}
}
//---------------------------------------------
void ventana2 (int x1, int y1, int x2, int y2, int colortitulo, int colorfondo, int colorSombra)
{
	int i;
	i=x1;
	ventana1 (x1, y1, x2, y2, colorfondo, colorSombra);
	renglon (x1, y1, x2, colortitulo);
	renglon (x1, y1+1, x2, colortitulo);
}
//----------------------------------------------
void tabla (int x1, int y1, int filas, int columnas, int borde)
{
	int i, i2, i3;
	i=0;
	i2=0;
	i3=1;
	while (i<=filas)
	{
		if (borde==1)
		{
			lineaH (x1+1, y1+i, (10*columnas)-2);
		}
		if (borde==2)
		{
			lineaH2 (x1+1, y1+i, (10*columnas)-2);
		}
		i++;
	}
	while (i2<=columnas)
	{
		if (borde==1)
		{
			lineaV (x1+(i2*10), y1+1, filas-2);
		}
		if (borde==2)
		{
			lineaV2 (x1+(i2*10), y1+1, filas-2);
		}
		i2++;
	}
	if (borde==1)
	{
		esquina1 (x1, y1);
		esquina2 (x1+(columnas*10), y1);
		esquina3 (x1, y1+filas);
		esquina4 (x1+(columnas*10), y1+filas);
		while (i3<columnas)
		{
			esquina1 (x1+(i3*10), y1);
			esquina3 (x1+(i3*10), y1+filas);
			i3++;
		}
	}
	if (borde==2)
	{
		esquina5 (x1, y1);
		esquina6 (x1+(columnas*10), y1);
		esquina7 (x1, y1+filas);
		esquina8 (x1+(columnas*10), y1+filas);
		while (i3<columnas)
		{
			esquina5 (x1+(i3*10), y1);
			esquina7 (x1+(i3*10), y1+filas);
			i3++;
		}
	}
}
//----------------------------------------------
void listaAscii ()
{
	int i;
	i=1;
	tabla (1, 1, 85, 3, 1);
	while (i<=85)
	{
		gotoxy (2, i*2);
		printf ("%d: %c \n\n", i, i);
		gotoxy (2+10, i*2);
		printf ("%d: %c \n\n", i+85, i+85);
		gotoxy (2+20, i*2);
		printf ("%d: %c \n\n", i+170, i+170);
		i++;
	}
}
//-----------------------------------------------
void listacolores ()
{
	int i;
	i=0;
	// tabla (1, 1, 64, 4, 1);
	while (i<64)
	{
		gotoxy (2, (i*2)+2);
		color (i);
		printf ("Color %d", i);
		gotoxy (2+10, (i*2)+2);
		color (i+64);
		printf ("Color %d", i+64);
		gotoxy (2+20, (i*2)+2);
		color (i+128);
		printf ("Color %d", i+128);
		gotoxy (2+30, (i*2)+2);
		color (i+192);
		printf ("Color %d", i+192);
		i++;
	}
}
