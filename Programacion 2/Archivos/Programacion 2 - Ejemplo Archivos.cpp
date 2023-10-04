/* Nota: para este ejemplo cree un archivo con el nombre de "notas.txt" y con los siguientes datos:

    01 pedro 2 1 1
   02 paco 5 3 4.5
   03 luis 5 5 5   */

#include <iostream>
#include <fstream>
#include <string.h>
#include <stdlib.h>
using namespace std;
struct estudiante
{
	char codigo[5];
	char nombre [20];
	float n1, n2, n3;
};


int i;
char cadena[20];
estudiante e[5];
char codigo[5];
float prome;

//-------------------------------------
void leerarchivo()
{
	//ifstream permite trabajar el archivo en modo de lectura
	ifstream leer;
	//open permite abrir el archivo
	leer.open ("notas.txt");
	//good indica si la operacion de abrir el archivo fue exitosa
	//bad indica produjo una operacion invalida
	//fail indica si se produjo un error
	if (leer.good())
	{
		cout<<"El archivo fue abierto correctamente..."<<endl;
	}
	else
	{
		cout<<"El archivo no se pudo abrir..."<<endl;
		
	}
	//eof () Produce un 1 si se encuentra en el final del archivo
	// !leer.eof() indica que no esta en el final del archivo
	i=0;
	while(!leer.eof())
	{
	  leer>>cadena;
	  strcpy(e[i].codigo,cadena);
      leer>>cadena;
	  strcpy(e[i].nombre,cadena);	  
      leer>>cadena;
	  e[i].n1=atof(cadena);
	  leer>>cadena;
	  e[i].n2=atof(cadena);
	  leer>>cadena;
	  e[i].n3=atof(cadena);
	  i++;
    }
    //close permite cerrar el archivo
	leer.close();
}

//------------------------------------------
void consultar()
{
	cout<<"Escriba el codigo del Estudiante --> ";
	cin>>codigo;
	int pos;
	for(int i=0;i<3;i++)
	{
		if (strcmp(codigo,e[i].codigo)==0)
		{
			pos=i;
			   	cout<<"datos del estudiante "<<i+1<<endl;
   	            cout<<"Codigo --> "<<e[i].codigo<<endl;
   				cout<<"Nombre --> "<<e[i].nombre<<endl;
   				cout<<"Nota 1 --> "<<e[i].n1<<endl;
   				cout<<"Nota 2 --> "<<e[i].n2<<endl;
   				cout<<"Nota 3 --> "<<e[i].n3<<endl;
   				prome =(e[i].n1+e[i].n2+e[i].n3)/3;
   				cout<<"Su promedio es  --> "<<prome<<endl<<endl;
			
		}
	}
}
//------------------------------------------
void modificar()
{
	cout<<"Escriba el codigo del Estudiante --> ";
	cin>>codigo;
	int pos;
	for(int i=0;i<5;i++)
	{
		if (strcmp(codigo,e[i].codigo)==0)
		{
			pos=i;
			   	cout<<"datos del estudiante "<<i+1<<endl;
   	            cout<<"Codigo --> "<<e[i].codigo<<endl;
   				cout<<"Nombre --> "<<e[i].nombre<<" --> ";
   				cin>>e[i].nombre;			
   				cout<<"Nota 1 --> "<<e[i].n1<<" --> ";
   				cin>>e[i].n1;
   				cout<<"Nota 2 --> "<<e[i].n2<<" --> ";
   				cin>>e[i].n2;
   				cout<<"Nota 3 --> "<<e[i].n3<<" --> ";
   				cin>>e[i].n3;
   				prome =(e[i].n1+e[i].n2+e[i].n3)/3;
   				cout<<"Su promedio es  --> "<<prome<<endl<<endl;
			
		}
	}
}
//------------------------------------------
void listar()
{
	float pg=0;
	for (int i=0;i<3;i++)
	{
	   	cout<<"datos del estudiante "<<i+1<<endl;
        cout<<"Codigo --> "<<e[i].codigo<<endl;
		cout<<"Nombre --> "<<e[i].nombre<<endl;
   	    cout<<"Nota 1 --> "<<e[i].n1<<endl;
   		cout<<"Nota 2 --> "<<e[i].n2<<endl;
   		cout<<"Nota 3 --> "<<e[i].n3<<endl;
   		prome =(e[i].n1+e[i].n2+e[i].n3)/3;
   		cout<<"Su promedio es  --> "<<prome<<endl;
   		pg=pg+prome;
	}
		pg=pg/3;
		cout<<"El promedio del grupo  es  --> "<<pg<<endl<<endl;
}
//------------------------------------------
void escribirarchivo()
{
	ofstream escribir;
	escribir.open ("notas.txt");
    if(escribir.good())
    {
    	cout<<"El archivo fue abierto correctamente..."<<endl;
    }
    else
    {
    	cout<<"El archivo no se pudo abrir..."<<endl;
    }
     
//    cin>>cadena;
//    escribir<<cadena;
	for (int i=0;i<3;i++)
	{
        //32 Espacio en blanco
        //10 Salto de Linea
        //9 Tabulador Horizontal
		escribir<<e[i].codigo;
        escribir<<(char)9; //Espacio en Blanco
		escribir<<e[i].nombre;
        escribir<<(char)9; //Espacio en Blanco
   	    escribir<<e[i].n1;
        escribir<<(char)9; //Espacio en Blanco
   		escribir<<e[i].n2;
        escribir<<(char)9; //Espacio en Blanco
   		escribir<<e[i].n3;
        escribir<<(char)9; //Espacio en Blanco
        escribir<<(char)10; //Salto de Linea
    }
	escribir.close();
}
//-------------------------------------------
void menu()
{   
    int op;
    op=0;
    while (op!=5)
	{
		cout<<"menu Principal"<<endl;
		cout<<"1. consultar promedio estudiante"<<endl;
		cout<<"2. modificar datos de estudiante"<<endl;
		cout<<"3. listar estudiantes"<<endl;
		cout<<"4. Guardar en el Archivo"<<endl;
		cout<<"5. salir"<<endl;	
		cout<<"Seleccione la Opcion (1-5)"<<endl;
		cin>>op;
		switch (op)
		{
			case 1:
				consultar();
				break;
			case 2:
				modificar();
				break;
			case 3:	
				listar();
				break;
			case 4:	
				escribirarchivo();
				break;

		}
	}
}
//-------------------------------------------
int main()
{
	leerarchivo();
    menu();
}
