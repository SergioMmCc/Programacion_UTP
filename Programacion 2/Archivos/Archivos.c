#include <stdio.h>

int main() {
    FILE *archivo;
    char contenido[] = "Hola, mundo!\nEste es un archivo de texto creado en C.";

    // Abre el archivo en modo escritura
    archivo = fopen("ruta_del_archivo.txt", "w");

    // Verifica si el archivo se creó correctamente
    if (archivo == NULL) {
        printf("No se pudo crear el archivo.\n");
        return 1;
    }

    // Escribe el contenido en el archivo
    fprintf(archivo, "%s", contenido);

    // Cierra el archivo
    fclose(archivo);

    printf("El archivo se creo correctamente.\n");

    return 0;
}
