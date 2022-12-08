# ocenione na 100%, bez komentarzy
def main():
    # pierwsza liczba wprowadzana poza pętlę, żeby przypisać najmniejszą wartość
    # żeby móc to porównywać z innymi wprowadzonymi liczbami
    najmniejsza = int(input("Wprowadź liczbę: "))

    # zaczynamy pętlę powtarzającą się 9 razy
    for i in range(9):
        liczba = int(input("Wprowadź liczbę: "))
        # gdy wczytana liczba jest mniejsza od ostatniej najmniejszej liczby,
        # zmień jej wartość
        if liczba < najmniejsza:
            najmniejsza = liczba

    print(najmniejsza)


if __name__ == "__main__":
    main()
