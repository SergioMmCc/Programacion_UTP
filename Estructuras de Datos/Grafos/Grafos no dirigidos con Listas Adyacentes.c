#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAXV 1005

struct edge
{
    int vertex;
	// int weight;
    struct edge *next;
};

struct graph
{
    int n_vertex;
    int m_edges;
    struct edge *Adj[MAXV];
};

struct graph *readGraph (int vertices, int edges) {
    int idVertex, idEdge, u, v;
    struct graph *G;
    struct edge *tempEdge;

    G = (struct graph *) malloc(sizeof(struct graph));
    G->n_vertex = vertices;
    G->m_edges = edges;

    for(idVertex = 1; idVertex <= G->n_vertex; idVertex++)
        G->Adj[idVertex] = NULL;

    for(idEdge = 1; idEdge <= G->m_edges; idEdge++) {
        scanf("%d %d", &u, &v);
        tempEdge = (struct edge *) malloc(sizeof(struct edge));
        tempEdge->vertex = v;
        tempEdge->next = G->Adj[u];
        G->Adj[u] = tempEdge;

        if(u != v)
        {
            tempEdge = (struct edge *) malloc(sizeof(struct edge));
            tempEdge->vertex = u;
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
                printf(" -> %d", tempEdge->vertex);
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

int main () {
    int vertices, edges;
    struct graph *G;

    while (scanf ("%d %d", &vertices, &edges) != EOF) {
        G = readGraph (vertices, edges);
        printGraph (G);
        G = deleteGraph (G);
        printGraph (G);
    }
    return 0;
}
