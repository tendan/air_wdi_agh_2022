// skończone
#include <stdio.h>

#define SIZE 200

int main() {
    FILE *input = fopen("input.txt", "r");
    FILE *output = fopen("output.txt", "w");
    
    if (input == NULL) {
        if (output != NULL) {
            fclose(output);
        }
        return -1;
    }
    
    if (output == NULL) {
        fclose(input);
        return -1;
    }
    
    char c;
    while ((c = fgetc(input)) != EOF) {
        fputc(c, output);
    }
    
    rewind(input);
    
    char s[SIZE];
    while ((fgets(s, SIZE, input)) != NULL) {
        fputs(s, output);
    }
    
    fclose(input);
    fclose(output);
    
    return 0;
}