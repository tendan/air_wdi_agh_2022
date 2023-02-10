// skończone
#include <stdio.h>
#include <stdlib.h>

int* compress(double **a_table, int *a_size) {
    double *new_table = NULL;
    int *indexes = NULL;
    
    int new_size = 0;
    
    for (
        double *cur_element = *a_table; 
        cur_element < &(*a_table)[*a_size]; 
        ++cur_element  //*a_table+*a_size
        ) {
        if (*cur_element != 0)
            ++new_size;
    }
    
    new_table = calloc(new_size, sizeof(double));
    indexes = calloc(new_size,  sizeof(int));
    
    if (new_table == NULL || indexes == NULL) {
        free(new_table);
        free(indexes);
        return NULL;
    }
    
    for (int i = 0, j = 0; i < *a_size; ++i) {
        if ((*a_table)[i] != 0) {
            new_table[j] = (*a_table)[i];
            indexes[j] = i;
            ++j;
        }
    }
    free(*a_table);
    *a_table = new_table;
    *a_size = new_size;
    
    return indexes;
}

void print_tabd(double *tab, int size) {
    for (int i = 0; i < size; ++i) {
        printf("%lf ", tab[i]);
    }
    printf("\n");
}

void print_tabi(int *tab, int size) {
    for (int i = 0; i < size; ++i) {
        printf("%d ", tab[i]);
    }
    printf("\n");
}

int main() {
    int size = 10;
    double *rzadka1 = calloc(size, sizeof(double));
    if (rzadka1 == NULL) {
        return -1;
    }
    rzadka1[2] = 3.0;
    rzadka1[5] = 1.0;
    rzadka1[8] = 7.0;
    
    print_tabd(rzadka1, size);
    
    int *indexes = compress(&rzadka1, &size);
    
    if (indexes == NULL) {
        free(rzadka1);
        return -1;
    }
    
    printf("Nowy rozmiar: %d\n", size);
    
    printf("Nowa tablica rzadka: \n");
    print_tabd(rzadka1, size);
    printf("Tablica indeksów: \n");
    print_tabi(indexes, size);
    
    free(indexes);
    free(rzadka1);
    
    return 0;
}