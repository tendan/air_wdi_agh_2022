# ocenione na 100%, bez komentarzy
def main():
    najmniejsza = int(input("Wprowadź liczbę: "))
    for i in range(9):
        liczba = int(input("Wprowadź liczbę: "))
        if liczba < najmniejsza:
            najmniejsza = liczba

    print(najmniejsza)


if __name__ == "__main__":
    main()
