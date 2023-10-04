/* Programa: LEELIN2. CDesc.: lee linea (version con apuntadores)" */
#include<stdio.h>
#include <stdlib.h>

int lee_linea (char *s, int lim)
{
	int lon,
	c; lon = 0;
	c = getchar();
	while (lon < lim && c != EOF && c != '\n')
	{
		*s=c;
		lon++;
		s++;
		c = getchar();
	}
	*s = '\0';
	return lon;
}


int main(void)
{
	char s[20];
	int n;
	printf("\nString: ");
	n = lee_linea (s, 30);
	printf("\n%s longitud = %d\n", s, n);
	system ("pause");
	return 0;
}
