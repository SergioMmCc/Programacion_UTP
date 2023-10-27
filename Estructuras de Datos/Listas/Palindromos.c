#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

#define TRUE 1
#define FALSE 0

struct node {
    int key;
    struct node *next;
};

struct node *push(struct node *top, int element) {
    struct node *newNode;
    newNode = (struct node *)malloc(sizeof(struct node));
    newNode->key = element;
    newNode->next = top;
    top = newNode;
    return top;
}

int pop(struct node **top) {
    struct node *actualNode;
    int element;
    actualNode = *top;
    element = actualNode->key;
    *top = actualNode->next;
    free(actualNode);
    return element;
}

int stackEmpty(struct node *top) {
    if (top == NULL)
        return TRUE;
    else
        return FALSE;
}

struct node *enqueue(struct node *tail, int element) {
    struct node *newNode;
    newNode = (struct node *)malloc(sizeof(struct node));
    newNode->key = element;
    if (tail == NULL) {
        newNode->next = newNode;
        tail = newNode;
    } else {
        newNode->next = tail->next;
        tail->next = newNode;
        tail = newNode;
    }
    return tail;
}

int dequeue(struct node **tail) {
    struct node *firstNode;
    int element;
    if (*tail == (*tail)->next) {
        element = (*tail)->key;
        free(*tail);
        *tail = NULL;
    } else {
        firstNode = (*tail)->next;
        element = firstNode->key;
        (*tail)->next = firstNode->next;
        free(firstNode);
    }
    return element;
}

int queueEmpty(struct node *tail) {
    if (tail == NULL)
        return TRUE;
    else
        return FALSE;
}

int main() {
    struct node *top, *tail;
    int n, element, idElement, flag;
    top = NULL;
    tail = NULL;
    while (scanf("%d", &n) != EOF) {
        flag = TRUE;
        for (idElement = 1; idElement <= n; idElement++) {
            scanf("%d", &element);
            top = push(top, element);
            tail = enqueue(tail, element);
        }
        while (stackEmpty(top) != TRUE) {
            if (pop(&top) != dequeue(&tail))
                flag = FALSE;
        }
        if (flag == TRUE)
            printf("The %d element(s) are palindrome.\n", n);
        else
            printf("The %d element(s) are not palindrome.\n", n);
    }
    return 0;
}
