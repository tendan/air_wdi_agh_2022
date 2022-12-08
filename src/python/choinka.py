# ocenione na 100%, bez komentarzy
def main():
    # wprowadzamy wartość dla n poprzez inputa (input()), potem konwertujemy na liczbę całkowitą (int())
    # n to jest ilość rzędów choinki
    n = int(input("Wprowadź n: "))
    for i in range(1, n + 1):
        # wygeneruj ilość spacji zależącą od rzędu, który jest generowany (o jeden mniejsza od indeksu rzędu)
        # kończ pustym znakiem, żeby nie zaczynać od nowej linii
        for _ in range(n - i):
            print(" ", end="")
        # wygeneruj ilość gwiazdek zależną od indeksu rzędu (ilość dwukrotnie większa od indeksu rzędu + 1)
        # kończ pustym znakiem, żeby nie zaczynać od nowej linii
        for _ in range(i + (i - 1)):
            print("*", end="")
        # wygeneruj znak nowej linii poprzez wywołanie bezargumentowego printa (print())
        print()


if __name__ == "__main__":
    main()
