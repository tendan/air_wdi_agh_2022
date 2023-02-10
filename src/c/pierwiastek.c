// skończone
#include <stdio.h>
#include <math.h>

int main()
{
    float a = 2;
    do {
        scanf("%f", &a);
        printf("%lf\n", sqrt(a));
    } while (a != 0 && a != 1);
    
    printf("Koniec");
    
    return 0;
}