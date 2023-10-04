#include <stdio.h>

int suma(int n1, int n2);
int resta(int n1, int n2);
int multiplicacion(int n1, int n2);
float division(float n1, float n2);

// --------------------------------------

void menu()
{
	int x, a,b, op;
	float y;
		printf("Ingrese a: ");
		scanf("%d", &a);
		printf("Ingrese b: ");
		scanf("%d", &b);
		
		printf("1 para sumar \n");
    	printf("2 para restar\n");
    	printf("3 para multiplicar \n");
   		printf("4 para dividir \n");
    	printf("5 para salir \n");
    	printf("Ingrese la opcion que desee (1-5): ");
    	scanf("%d", &op);
    	
    	if (op==1)
    	{
    		x=suma(a,b);
    		printf("%d + %d = %d\n",a,b,x);
    		menu();
		}
		if (op==2)
    	{
    		x=resta(a,b);
    		printf("%d - %d = %d\n",a,b,x);
    		menu();
		}
		if (op==3)
		{
    		x=multiplicacion(a,b);
    		printf("%d * %d = %d\n",a,b,x);
    		menu();
		}
		if (op==4)
		{
			if (b==0)
			{
				printf("No se puede dividir por 0\n");
				menu();
			}
			else
			{
				y=division(a,b);
				printf("%d / %d = %f\n",a,b,y);
				menu();
			}
		}
}

//---------------------------------------------------

main()
{
	menu();
}

// -------------------------------------

int suma(int n1, int n2)
{
	int s;
	s=n1+n2;
	return s;
}
//-----------------------------
int resta(int n1, int n2)
{
	int r;
	r=n1-n2;
	return r;
}
//----------------------------------
int multiplicacion(int n1, int n2)
{
	int m;
	m=n1*n2;
	return m;
}
//-----------------------------------
float division(float n1, float n2)
{
	float d;
	d=n1/n2;
	return d;
}
