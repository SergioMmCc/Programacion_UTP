#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXH 105
#define MAXW 105
#define WHITE 2
#define GRAY 1
#define BLACK 0
#define myInfinite 2147483647
#define NIL -1

struct cell 
{
    int coord_x;
    int coord_y;
};

struct cell readMaze (char maze[][MAXW], int W, int H) {
    char line [MAXW];
    int idRow, idColumn;
    struct cell source;
    
    for (idRow = 1; idRow <= H; idRow++) {
        scanf ("%s", line);
        
        for (idColumn = 1; idColumn <= W; idColumn++) {
            maze[idRow][idColumn] = line[idColumn - 1];
            
            if (line[idColumn - 1] == '@') {
                source.coord_x = idColumn;
                source.coord_y = idRow;
                maze[idRow][idColumn] = '.';
            }
        }
    }
    
    return source;
}

void printMaze (char maze[][MAXW], int W, int H) {
    int idRow, idColumn;
    printf ("\nThe original maze without source position:\n\n");
    
    for (idRow = 1; idRow <= H; idRow++) {
        for (idColumn = 1; idColumn <= W; idColumn++)
            printf ("%c", maze[idRow][idColumn]);
        printf ("\n");
    }
    printf ("\n");
}

void initializerMovements (struct cell movements[]) {
    movements[0].coord_x = 0;
    movements[0].coord_y = 0;
    movements[1].coord_x = 0;
    movements[1].coord_y = -1;
    movements[2].coord_x = 0;
    movements[2].coord_y = 1;
    movements[3].coord_x = 1;
    movements[3].coord_y = 0;
    movements[4].coord_x = -1;
    movements[4].coord_y = 0;
}

void BFS_Maze (char maze[][MAXW], int W, int H, struct cell source, 
                int color[][MAXW], int d[][MAXW], struct cell pi[][MAXW])
{
    int idRow, idColumn, head = 1, tail = 1, idMovement;
    struct cell NILFather, Q[MAXH * MAXW], u, v, movements[5];
    
    initializerMovements (movements);
    NILFather.coord_x = NIL;
    NILFather.coord_y = NIL;
    
    for (idRow = 1; idRow <= H; idRow++) {
        for (idColumn = 1; idColumn <= W; idColumn++) {
            color[idRow][idColumn] = WHITE;
            d[idRow][idColumn] = myInfinite;
            pi[idRow][idColumn] = NILFather;
        }
    }
    
    color[source.coord_y][source.coord_x] = GRAY;
    d[source.coord_y][source.coord_x] = 0;
    pi[source.coord_y][source.coord_x] = NILFather;
    
    Q[tail] = source;
    tail++;
    
    while (head < tail) {
        u = Q[head];
        head++;
        for (idMovement = 1; idMovement <= 4; idMovement++) {
            v.coord_x = u.coord_x + movements[idMovement].coord_x;
            v.coord_y = u.coord_y + movements[idMovement].coord_y;
            if ((v.coord_x >= 1 && v.coord_x <= W) && 
                (v.coord_y >= 1 && v.coord_y <= H) && 
                (maze[v.coord_y][v.coord_x] == '.') &&
                (color[v.coord_y][v.coord_x] == WHITE))
            {
                color[v.coord_y][v.coord_x] = GRAY;
                d[v.coord_y][v.coord_x] = d[u.coord_y][u.coord_x] + 1;
                pi[v.coord_y][v.coord_x] = u;
                Q[tail] = v;
                tail++;
            }
        }
        
        color[u.coord_y][u.coord_x] = BLACK;
    }
}

void solver (char maze[][MAXW], int W, int H, struct cell source) {
    int color[MAXH][MAXW], d[MAXH][MAXW], idRow, idColumn;
    struct cell pi[MAXH][MAXW];
    
    BFS_Maze (maze, W, H, source, color, d, pi);
    
    printf ("Colors:\n");
    for (idRow = 1; idRow <= W; idRow++) {
        for (idColumn = 1; idColumn <= W; idColumn++) {
            if (color[idRow][idColumn] == WHITE)
                printf ("W");
            if (color[idRow][idColumn] == GRAY)
                printf ("G");
            if (color[idRow][idColumn] == BLACK)
                printf ("B");
        }
        printf ("\n");
    }
    printf ("\n");
    
    printf ("Distances:\n");
    for (idRow = 1; idRow <= W; idRow++) {
        for (idColumn = 1; idColumn <= W; idColumn++) 
            printf ("%d ", d[idRow][idColumn]);
            
        printf ("\n");
    }
    printf ("\n");
    
    printf ("Fathers:\n");
    for (idRow = 1; idRow <= W; idRow++) {
        for (idColumn = 1; idColumn <= W; idColumn++) 
            printf ("[%d, %d] ", 
                    pi[idRow][idColumn].coord_y, 
                    pi[idRow][idColumn].coord_x);
            
        printf ("\n");
    }
    printf ("\n");
}

int main () {
    char maze[MAXH][MAXW];
    int T, W, H, idCase;
    struct cell source;
    
    scanf ("%d", &T);
    for (idCase = 1; idCase <= T; idCase++) {
        scanf ("%d %d", &W, &H);
        source = readMaze (maze, W, H);
        printMaze (maze, W, H);
        solver (maze, W, H, source);
    }

    return 0;
}
