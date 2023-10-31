#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct nodeTree {
    int key;
    struct nodeTree *p, *left, *right;
};

void inOrderTreeWalk (struct nodeTree *x) {
    if (x != NULL) {
        inOrderTreeWalk (x->left);
        printf ("%d ", x->key);
        inOrderTreeWalk (x->right);
    }
}

struct nodeTree *treeSearch (struct nodeTree *x, int k) {
    while ((x != NULL) && (k != x->key)) {
        if (k < x->key)
            x = x->left;
        else
            x = x->right;
    }
    return x;
}

struct nodeTree *treeMinimum (struct nodeTree *x) {
    while (x->left != NULL)
        x = x->left;
    return x;
}

struct nodeTree *treeMaximum (struct nodeTree *x) {
    while (x->right != NULL)
        x = x->right;
    return x;
}

struct nodeTree *treeSucessor (struct nodeTree *x) {
    struct nodeTree *y;
    if (x->right != NULL)
        return treeMinimum (x->right);
    y = x->p;
    while ((y != NULL) && (y == x->right)) {
        x = y;
        y = y->p;
    }
    
    return y;
}

struct nodeTree *treePredecessor (struct nodeTree *x) {
    struct nodeTree *y;
    if (x->left != NULL)
        return treeMaximum (x->left);
    y = x->p;
    while ((y != NULL) && (y == x->left)) {
        x = y;
        y = y->p;
    }
    
    return y;
}

struct nodeTree *treeInsert (struct nodeTree *T, int k) {
    struct nodeTree *z, *x, *y;
    z = (struct nodeTree *)malloc(sizeof (struct nodeTree));
    z->key = k;
    z->left = NULL;
    z->right = NULL;
    y = NULL;
    x = T;
    
    while (x != NULL) {
        y = x;
        if (z->key < x->key)
            x = x->left;
        else
            x = x->right;
    }
    z->p = y;
    
    if (y == NULL)
        T = z; //The tree is empty.
    else if (z->key < y->key)
        y->left = z;
    else
        y->right = z;
        
    return T;
}

struct nodeTree *treeDelete(struct nodeTree *T, struct nodeTree *z)
{
	struct nodeTree *x, *y;
	if((z -> left == NULL) || (z -> right == NULL))
        y = z;
    else
        y = treeSucessor(z);
    
    if (y->left != NULL)
        x = y->left;
    else
        x = y->right;
    
    if (x != NULL)
        x->p = y->p;
    
    if (y->p == NULL)
        T = x;
    else if (y == y->p->left)
        y->p->left = x;
 	else
        y->p->right = x;
	
	if (y != z)
	{
		z->key = y->key;
		/* Copy all information fields from y to z. */
	}
	free (y);
	
	return T;
}

int main () {
    int n, element, idElement, result, value;
    struct nodeTree *T, *z;
    
    while (scanf ("%d", &n) && (n != 0)) {
        
        result = 0;
        for (idElement = 1; idElement <= n; idElement++) {
            scanf ("%d", &element);
            T = treeInsert (T, element);
        }
        
        for (idElement = 1; idElement < n; idElement++) {
            z = treeMinimum (T);
            value = z->key;
            T = treeDelete (T, z);
            
            z = treeMinimum (T);
            value += z->key;
            T = treeDelete (T, z);
            
            result += value;
            T = treeInsert (T, value);
        }
        
        printf ("%d\n", result);
        T = treeDelete (T, T);
    }
    
    return 0;
}
