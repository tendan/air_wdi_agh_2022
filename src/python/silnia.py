# ocenione na 100%, bez komentarzy
def main():
    n = 1
    while n != 0 and n != 10:
        n = int(input("Wprowadź n (n >= 0): "))

        # nie spełnia założeń silni, odrzuć wartość i zakończ program
        # return wewnątrz funkcji kończy jej działanie (w tym przypadku)
        if n < 0:
            print("Ujemna wartość n, odrzucam")
            return

        # utwórz zmienną wynik, żeby móc modyfikować jej wartość
        wynik = 1

        # mnóż wynik przez rosnącą o 1 wartość i dopóki jest ono mniejsze od n + 1, aby wyszedł wynik silni
        for i in range(1, n + 1):
            wynik *= i

        # string formatting
        # można zastąpić:
        # print("Wynik", n, "! :", wynik)
        print("Wynik %d!: %d" % (n, wynik))

    print("Koniec")


if __name__ == "__main__":
    main()
