#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#define NIL -1
#define myPositiveInfinite 2147483647
#define MAXV 1000
#define TRUE 1
#define FALSE 0

struct edge
{
    int vertex;
	int weight;
    struct edge *next;
};

struct graph
{
    int n_vertex;
    int m_edges;
    struct edge *Adj[MAXV + 1];
};

struct graph *readGraph (int vertices, int edges) {
    int idVertex, idEdge, u, v, w;
    struct graph *G;
    struct edge *tempEdge;

    G = (struct graph *) malloc(sizeof(struct graph));
    G->n_vertex = vertices;
    G->m_edges = edges;

    for(idVertex = 1; idVertex <= G->n_vertex; idVertex++)
        G->Adj[idVertex] = NULL;

    for(idEdge = 1; idEdge <= G->m_edges; idEdge++) {
        scanf("%d %d %d", &u, &v, &w);

        u++;
        v++;
        tempEdge = (struct edge *) malloc(sizeof(struct edge));
        tempEdge->vertex = v;
        tempEdge->weight = w;
        tempEdge->next = G->Adj[u];
        G->Adj[u] = tempEdge;

        if(u != v)
        {
            tempEdge = (struct edge *) malloc(sizeof(struct edge));
            tempEdge->vertex = u;
            tempEdge->weight = w;
            tempEdge->next = G->Adj[v];
            G->Adj[v] = tempEdge;
        }
    }
    return G;
}

void printGraph (struct graph *G) {
    int idVertex;
    struct edge *tempEdge;

    if (G != NULL)
    {
        printf("Representation for graph's adjacent lists: \n");
        for(idVertex = 1; idVertex <= G->n_vertex; idVertex++)
        {
            printf("[%d]: ", idVertex);
            tempEdge = G->Adj[idVertex];
            while(tempEdge != NULL)
            {
                printf(" -> (%d, %d)", tempEdge->vertex, tempEdge->weight);
                tempEdge = tempEdge->next;
            }
            printf(" -> NULL\n");
        }
    }
    else
        printf("Empty Graph.\n");
}

struct graph *deleteGraph (struct graph *G) {
    int idVertex;
    struct edge *actualEdge, *nextEdge;

    for (idVertex = 1; idVertex <= G->n_vertex; idVertex++) {
        actualEdge = G->Adj[idVertex];
        while(actualEdge != NULL)
        {
            nextEdge = actualEdge->next;
            free (actualEdge);
            actualEdge = nextEdge;
        }
    }
    free (G);
    G = NULL;
    return G;
}

int extractMin (int d[], int inQueue[], int n) {
    int idVertex, minimum = myPositiveInfinite, idMinimum = myPositiveInfinite;
    
    for (idVertex = 1; idVertex <= n; idVertex++) {
        if (inQueue[idVertex] == TRUE && d[idVertex] < minimum) {
            minimum = d[idVertex];
            idMinimum = idVertex;
        }
    }
    if (idMinimum != myPositiveInfinite)
        inQueue[idMinimum] = FALSE;
        
    return idMinimum;
}

void prim (struct graph *G, int d[], int pi[], int s) {
    int idVertex, u, v, w, inQueue[MAXV + 1];
    int totalElementsInQueue = G->n_vertex;
    struct edge *tempEdge;
    
    for (idVertex = 1; idVertex <= G->n_vertex; idVertex++) {
        d[idVertex] = myPositiveInfinite;
        pi[idVertex] = NIL;
        inQueue[idVertex] = TRUE;
    }
    d[s] = 0;
    
    while (totalElementsInQueue > 0) {
        u = extractMin (d, inQueue, G->n_vertex);
        
        if (u == myPositiveInfinite) 
            break;
        
        totalElementsInQueue--;
        tempEdge = G->Adj[u];
        
        while (tempEdge != NULL) {
            v = tempEdge->vertex;
            w = tempEdge->weight;
            
            if (inQueue[v] == TRUE && d[v] > w) {
                d[v] = w;
                pi[v] = u;
            }
            tempEdge = tempEdge->next;
        }
    }
}

void solver (struct graph *G, int s) {
    int d[MAXV + 1], pi[MAXV + 1], idVertex, max, actualVertex;
    prim (G, d, pi, s);
    
    for (idVertex = 1; idVertex <= G->n_vertex; idVertex++) {
        if (d[idVertex] == myPositiveInfinite)
            printf ("Impossible\n");
        else {
            max = 0;
            actualVertex = idVertex;
            while (actualVertex != -1) {
                if (d[actualVertex] > max)
                    max = d[actualVertex];
                actualVertex = pi[actualVertex];
            }
            printf ("%d\n", max);
        }
    }
}

int main () {
    int vertices, edges, s, totalCases, idCase;
    struct graph *G;
    
    scanf ("%d", &totalCases);
    for (idCase = 1; idCase <= totalCases; idCase++) {
        scanf ("%d %d", &vertices, &edges);
        G = readGraph (vertices, edges);
        scanf ("%d", &s);
        printf ("Case %d:\n", idCase);
        solver (G, s + 1);
        G = deleteGraph (G);
    }
    
    return 0;
}