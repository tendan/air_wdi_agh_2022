# ocenione na 100%, bez komentarzy
def main():
    n = 1
    while n != 0 and n != 10:
        n = int(input("Wprowadź n (n >= 0): "))

        if n < 0:
            print("Ujemna wartość n, odrzucam")
            return

        wynik = 1

        for i in range(1, n + 1):
            wynik *= i

        print("Wynik %d!: %d" % (n, wynik))

    print("Koniec")


if __name__ == "__main__":
    main()
