// skończone
#include <stdio.h>

#define ROW1 4
#define COL1 3
#define ROW2 3
#define COL2 2

void print_macierz(double macierz[ROW1][COL2])
{
    for (int i = 0; i < ROW1; ++i)
    {
        for (int j = 0; j < COL2; ++j)
        {
            printf("%8.2lf", macierz[i][j]);
        }
        printf("\n");
    }
}

int main() {
    double macierz1[ROW1][COL1] = {{4, 2, 0}, {1, -3, 4}, {8, 10, 3}, {5, 12, 4}};
    double macierz2[ROW2][COL2] = {{7, -5}, {-6, 2}, {3, -9}};
    
    double macierz3[ROW1][COL2] = {{0, 0}, {0, 0}, {0, 0}, {0, 0}};
    
    for (int i = 0; i < ROW1; ++i) {
        for (int k = 0; k < COL2; ++k) {
            for (int j = 0; j < COL1; ++j) {
                macierz3[i][k] += macierz1[i][j] * macierz2[j][k];
            }
        }
    }
    
    print_macierz(macierz3);
    
    return 0;
}