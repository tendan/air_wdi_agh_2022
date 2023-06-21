// skończone
#include <stdio.h>
#include <stdlib.h>

int* generuj(int n) {
    int *tablica = malloc(n * sizeof(*tablica));
    
    if (tablica == NULL) {
        return NULL;
    }
    
    for (int i = 0; i < n; ++i) {
        tablica[i] = 2 * i + 1;
    }
    
    return tablica;
}

int main() {
    int n = 5;
    int *moja_tab = generuj(n);
    
    if (moja_tab == NULL) {
        return -1;
    }
    
    for (int i = 0; i < n; ++i) {
        printf("%d\n", moja_tab[i]);
    }
    
    free(moja_tab);
    
    return 0;
}