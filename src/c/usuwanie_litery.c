// skończone
#include <stdio.h>

void usun_znak(char napis[], char znak) {
    int i = 0;
    while (napis[i]) {
        while (napis[i] == znak) {
            int j = 0;
            while (napis[i+j]) {
                napis[i+j] = napis[i + j + 1];
                ++j;
            }
        }
        ++i;
    }
}

int main() {
    char tekst[] = "Zaawansowane techniki programowania";
    puts(tekst);
    usun_znak(tekst, 'a');
    puts(tekst);
    return 0;
}