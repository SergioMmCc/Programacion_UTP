#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#define MAXT 100000
#define myPositiveInfinite 9223372036854771616
#define myNegativeInfinite -9223372036854771616

int main () {
	long long int T, X[MAXT+1], Y[MAXT+1], P, A, B, i, j, total, tokens [MAXT], k;
	scanf ("%lld", &T);
	
	for (i=1; i<=T; i++)
		scanf ("%lld %lld", &X[i], &Y[i]);
	
	scanf ("%lld", &P);
	
	for (i=1; i<=P; i++) {
		scanf ("%lld %lld", &A, &B);
		
		total = 0;
		k=1;
		
		for (j=1; j<=T; j++) {
			if (Y[j] < (A * X[j] + B)) {
				total ++;
				tokens [k] = j;
				k++;
				Y[j] = myPositiveInfinite;
				X[j] = myNegativeInfinite;
			}
		}
		
		printf ("%lld", total);
		
		k=1;
		
		while (total > 0) {
			printf (" %lld", tokens [k]);
			k++;
			total--;
		}
		printf ("\n");
	}
	
	return 0;
}
