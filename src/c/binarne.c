// skończone
#include <stdio.h>
#include <string.h>

#define BUFFER 1000

int main() {
    
    FILE *input = fopen("input.txt", "rb");
    FILE *output = fopen("output.txt", "w+b");
    
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
    
    fseek(input, 0L, SEEK_SET);
    long poczatek = ftell(input);
    fseek(input, 0L, SEEK_END);
    long koniec = ftell(input);
    long dlugosc_pliku = koniec - poczatek;
    
    rewind(input);
    
    char buffer[dlugosc_pliku];
    
    fread(buffer, sizeof(*buffer), dlugosc_pliku, input);
    
    for (int i = 0; i < 3; ++i)
        fwrite(buffer, sizeof(*buffer), dlugosc_pliku, output);
        
    rewind(output);
    
    fseek(output, dlugosc_pliku, SEEK_SET);
    
    memset(buffer, 'A', sizeof(*buffer) * dlugosc_pliku);
    
    fwrite(buffer, sizeof(*buffer), dlugosc_pliku, output);
    
    fclose(input);
    fclose(output);
    
    return 0;
}