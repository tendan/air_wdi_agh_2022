// skończone
#include <stdio.h>
#include <math.h>

int pierwiastki(double a, double b, double c, double *x1, double *x2) {
    double delta = b * b - 4 * a * c;
    
    if (delta < 0) {
        return 0;
    }
    
    if (delta == 0) {
        *x1 = (-b) / (2 * a);
        return 1;
    }
    
    if (delta > 0) {
        *x1 = (-b - sqrt(delta)) / (2 * a);
        *x2 = (-b + sqrt(delta)) / (2 * a);
        return 2;
    }
}

int main() {
    double a, b, c;
    double x1, x2;
    scanf("%lf %lf %lf", &a, &b, &c);
    
    int ilosc_rozwiazan = pierwiastki(a, b, c, &x1, &x2);
    
    // można było użyć switcha
    if (ilosc_rozwiazan == 0) {
        printf("nie ma miejsc zerowych");
    } else if (ilosc_rozwiazan == 1) {
        printf("jedno miejsce zerowe x0 = %lf", x1);
    } else if (ilosc_rozwiazan == 2) {
        printf("dwa miejsca zerowe x1 = %lf, x2 = %lf", x1, x2);
    }
    
    return 0;
}