// skończone
#include <stdio.h>

double iloczyn_skalarny(
    double* tablica1,
    double* tablica2,
    int rozmiar
) {
    double suma = 0;
    
    for (int i = 0; i < rozmiar; ++i)
    {
        suma += tablica1[i] * tablica2[i];
    }
    
    return suma;
}

int main() {
    
    double tab1[] = {1.0,2.0,3.0,4.0,5.0};
    double tab2[] = {6.0,7.0,8.0,9.0,10.0};
    
    printf("%lf\n", iloczyn_skalarny(tab1, tab2, sizeof(tab1) / sizeof(*tab1)));
    
    double tab3[] = {0.0,2.0,3.0};
    double tab4[] = {0.0,7.0,0.0};
    
    printf("%lf\n", iloczyn_skalarny(tab3, tab4, sizeof(tab3) / sizeof(*tab3)));
    
    return 0;
}