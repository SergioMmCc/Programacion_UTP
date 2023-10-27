#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define TRUE 1
#define FALSE 0
#define myPositiveInfinite 2147483647
#define myNegativeInfinite -2147483647
#define MAXT 1000

struct node
{
    int key;
    struct node *next;
};

int Parent (int i) {
    return i / 2;
}

int Left (int i) {
    return 2 * i;
}

int Right (int i) {
    return 2 * i + 1;
}

void MaxHeapify (int Q[], int i, int heapSize) {
    int l, r, least;
    int temp;
    l = Left(i);
    r = Right(i);
    if((l <= heapSize) && (Q[l] > Q[i]))
        least = l;
    else
        least = i;
    if((r <= heapSize) && (Q[r] > Q[least]))
        least = r;
    if(least != i) {
        temp = Q[i];
        Q[i] = Q[least];
        Q[least] = temp;
        MaxHeapify(Q, least, heapSize);

    }
}

int MaxPQ_Minimum (int Q[]) {
    return Q[1];
}

int MaxPQ_Extract (int Q[], int *heapSize) {
    int max;
    max = myPositiveInfinite;
    if (*heapSize < 1)
        printf("Heap underflow.\n");
    else {
        max = Q[1];
        Q[1] = Q[*heapSize];
        *heapSize = *heapSize - 1;
        MaxHeapify(Q, 1, *heapSize);
    }
    return max;
}

void MaxPQ_IncreaseKey (int Q[], int i, int key) {
    int temp;
    if (key < Q[i])
        printf("New key is lower than current key.\n");
    else {
        Q[i] = key;
        while ((i > 1) && (Q[Parent(i)] < Q[i])) {
            temp = Q[i];
            Q[i] = Q[Parent(i)];
            Q[Parent(i)] = temp;
            i = Parent(i);
        }
    }
}

void MaxPQ_Insert (int Q[], int key, int *heapSize) {
    *heapSize = *heapSize + 1;
    Q[*heapSize] = myNegativeInfinite;
    MaxPQ_IncreaseKey(Q, *heapSize, key);
}

//Funcion para agregar un nodo a una cola
struct node *enqueue (struct node *tail, int element) {
    struct node *newNode;
    newNode = (struct node *)malloc(sizeof (struct node));
    newNode->key = element;
    if (tail == NULL) {
        newNode->next = newNode;
        tail = newNode;
    }
    else {
        newNode->next = tail->next;
        tail->next = newNode;
        tail = newNode;
    }
    return tail;
}

//Funcion para extraer un elemento de la cola
int dequeue (struct node **tail) {
    struct node *firstNode;
    int element;
    if (*tail == (*tail)->next) {
        element = (*tail)->key;
        free (*tail);
        *tail = NULL;
    }
    else {
        firstNode = (*tail)->next;
        element = firstNode->key;
        (*tail)->next = firstNode->next;
        free (firstNode);
    }
    return element;
}

//Funcion para averiguar si una cola esta vacia
int queueEmpty (struct node *tail) {
    if (tail == NULL)
        return TRUE;
    else 
        return FALSE;
}

//Funcion para agregar un elemento a la pila
struct node *push (struct node *top, int element) {
    struct node *newNode;
    newNode = (struct node *)malloc(sizeof (struct node));
    newNode->key = element;
    newNode->next = top;
    top = newNode;
    return top;
}

//Funcion para eliminar un elemento de la pila
int pop (struct node **top) {
    struct node *actualNode;
    int element;
    actualNode = *top;
    element = actualNode->key;
    *top = actualNode->next;
    free (actualNode);
    return element;
}

//Funcion para averiguar si la pila esta vacia
int stackEmpty (struct node *top) {
    if (top == NULL)
        return TRUE;
    else
        return FALSE;
}

int main () {
	int n, result, element, Q [MAXT + 1], heapSize, operation, compare;
	struct node *tail = NULL, *top = NULL;
	
	while (scanf ("%d", &n) != EOF) {
		heapSize = 0;
		result = 7;
		
		while (n--) {
			scanf ("%d %d", &operation, &element);
			
			if (operation == 1) {
				MaxPQ_Insert (Q, element, &heapSize);
				tail = enqueue (tail, element);
				top = push (top, element);
			}
			else {
				if ((result == 7) || (result == 5) || (result == 3) || (result == 1)) {
					compare = MaxPQ_Extract (Q, &heapSize);
					if (compare != element)
						result--;
				}
				if ((result == 7) || (result == 6) || (result == 3) || (result == 2)) {
					compare = dequeue (&tail);
					if (compare != element)
						result = result - 2;
				}
				if ((result == 7) || (result == 6) || (result == 5) || (result == 4)) {
					compare = pop (&top);
					if (compare != element)
						result = result - 4;
				}
			}
		}
		if (result == 0)
			printf ("impossible\n");
		else if (result == 1)
			printf ("priority queue\n");
		else if (result == 2)
			printf ("queue\n");
		else if (result == 4)
			printf ("stack\n");
		else
			printf ("not sure\n");
				
		while (tail != NULL)
			element = dequeue (&tail);	
		while (top != NULL)
			element = pop (&top);
		
	}
	return 0;
}
