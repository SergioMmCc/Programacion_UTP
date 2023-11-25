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


int main () {
    char maze[MAXH][MAXW];
    int T, W, H, idCase;
    struct cell source;
    
    scanf ("%d", &T);
    for (idCase = 1; idCase <= T; idCase++) {
        scanf ("%d %d", &W, &H);
        source = readMaze (maze, W, H);
        printMaze (maze, W, H);
        printf ("The source position is, column: %d, row: %d\n",
                source.coord_x, source.coord_y);
    }

    return 0;
}
