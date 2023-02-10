// skończone
#include <stdio.h>

#define ROW 4
#define COL 3

int main() {
    int macierz1[ROW][COL] = {{5, 2, 3}, {3, 4, 7}, {8, 3, 5}, {2, 6, 4}};
    int macierz2[ROW][COL] = {{12, 4, 6}, {4, 8, -2}, {4, 3, -6}, {-3, 5, 4}};
    
    int macierz3[ROW][COL];
    
    for (int i = 0; i < ROW; ++i)
    {
        for (int j = 0; j < COL; ++j)
        {
            macierz3[i][j] = macierz1[i][j] + macierz2[i][j];
        }
    }
    
    printf("macierz1:\n");
    for (int i = 0; i < ROW; ++i)
    {
        for (int j = 0; j < COL; ++j)
        {
            printf("%4d", macierz1[i][j]);
        }
        printf("\n");
    }
    printf("macierz2:\n");
    for (int i = 0; i < ROW; ++i)
    {
        for (int j = 0; j < COL; ++j)
        {
            printf("%4d", macierz2[i][j]);
        }
        printf("\n");
    }
    printf("macierz3:\n");
    for (int i = 0; i < ROW; ++i)
    {
        for (int j = 0; j < COL; ++j)
        {
            printf("%4d", macierz3[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}