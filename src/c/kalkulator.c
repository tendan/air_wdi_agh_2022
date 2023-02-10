// skończone
#include <stdio.h>

int main()
{
    char znak = '\0';
    float x = 0, y = 0;
    scanf("%c %f %f", &znak, &x, &y);
    
    switch (znak) {
        case '+':
            printf("%f\n", x + y);
        break;
        case '-':
            printf("%f\n", x - y);
        break;
        case '*':
            printf("%f\n", x * y);
        break;
        case '/':
            if (y == 0) {
                printf("Nie można dzielić przez zero\n");
                return 1;
            }
            printf("%f", x / y);
        break;
        default:
            printf("Nieznany operator\n");
            return 1;
    }
    return 0;
}