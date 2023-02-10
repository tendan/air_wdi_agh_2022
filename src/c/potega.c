// skończone
#include <stdio.h>

double potega_rek(double, int);
double potega(double, int);

int main() 
{
    printf("%lf \n%lf \n%lf \n", potega(3, -2), potega(2, 4), potega(4, 0));
    printf("%lf \n%lf \n%lf \n", potega_rek(3, -2), potega_rek(2, 4), potega_rek(4, 0));
    return 0;
}

double potega_rek(double x, int n)
{
    if (n == 0)
    {
        return 1;
    }
    if (n > 0) 
    {
        return x * potega_rek(x, n - 1);
    }
    if (n < 0)
    {
        return (1 / x) * potega_rek(x, n + 1);
    }
}

double potega(double x, int n)
{
    double wynik = 1;
    if (n == 0)
    {
        return wynik;
    }
    if (n > 0)
    {
        int i = 0;
        while (i < n)
        {
            wynik *= x;
            ++i;
        }
        return wynik;
    }
    if (n < 0)
    {
        n = -n;
        for (int i = 0; i < n; ++i)
        {
            wynik *= x;
        }
        return 1.0 / wynik;
    }
}