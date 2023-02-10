// skończone
#include <stdio.h>
#include <stdlib.h>

double* add(double *tab, int n, double new_elem) {
    double *new_tab = malloc(n * sizeof(*tab) + sizeof(*tab));
    
    if (new_tab == NULL) {
        return NULL;
    }
    
    for (int i = 0; i < n; ++i) {
        new_tab[i] = tab[i];
    }
    new_tab[n] = new_elem;
    
    free(tab);
    
    return new_tab;
}

int main() {
    double *tab = NULL;
    
    for (int i = 0; i < 10; ++i) {
        tab = add(tab, i, i + 1);
        if (tab == NULL) {
            return -1;
        }
    }
    
    for (int i = 0; i < 10; ++i) {
        printf("%.2lf\n", tab[i]);
    }
    
    free(tab);
    
    return 0;
}