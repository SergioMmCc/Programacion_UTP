#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#define TRUE 1
#define FALSE 0

struct node
{
    int key, max, min;
    struct node *next;
};

struct node *push (struct node *top, int element) {
    struct node *newNode;
    newNode = (struct node *)malloc(sizeof (struct node));
    newNode->key = element;
    
    if (top == NULL) {
        newNode->min = element;
        newNode->max = element;
    }
    else {
        if (element > top->max) 
            newNode->max = element;
        else
            newNode->max = top->max;
        if (element < top->min)
            newNode->min = element;
        else
            newNode->min = top->min;
    }
    
    newNode->next = top;
    top = newNode;
    return top;
}

int pop (struct node **top) {
    struct node *actualNode;
    int element;
    actualNode = *top;
    element = actualNode->key;
    *top = actualNode->next;
    free (actualNode);
    return element;
}

int stackEmpty (struct node *top) {
    if (top == NULL)
        return TRUE;
    else
        return FALSE;
}

struct node *FreeNodesStack (struct node *top) {
    struct node *actualNode;
    actualNode = top;
    
    while (actualNode != NULL) {
        top = actualNode->next;
        free (actualNode);
        actualNode = top;
    }
    return top;
}

int main () {
    int totalCases, totalQueries, operation, idCase, idQuery, element;
    struct node *top;
    top = NULL;
    
    scanf ("%d", &totalCases);
    
    for (idCase = 1; idCase <= totalCases; idCase++) {
        scanf ("%d", &totalQueries);
        
        for (idQuery = 1; idQuery <= totalQueries; idQuery++) {
            scanf ("%d", &operation);
            
            if (operation == 1) {
                scanf ("%d", &element);
                top = push (top, element);
            }
            
            else if (operation == 2) {
                if (stackEmpty (top) != TRUE) 
                    element = pop (&top);
            }
            
            else if (operation == 3) {
                if (stackEmpty (top) == TRUE)
                    printf ("Empty!\n");
                else 
                    printf ("%d\n", top->max - top->min);
                    
            }
        }
        top = FreeNodesStack (top);
    }
    return 0;
}
