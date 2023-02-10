// skończone
#include <stdio.h>

#define SIZE 100

char *znajdz_znak(char *napis, char szuk_znak) {
    while (*napis) {
        if (szuk_znak == *napis) {
            return napis;
        }
        ++napis;
    }
    return NULL;
}

int main() {
    char napis[SIZE];
    fgets(napis, SIZE, stdin);
    char *znaleziony = znajdz_znak(napis, 'p');
    
    if (znaleziony == NULL) {
        printf("Nie znaleziono takiej litery");
    } else {
        printf("Zawartość adresu: %c", *znaleziony);
    }
    
    return 0;
}