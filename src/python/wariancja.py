# ocenione na 100%, bez komentarzy
def srednia_wariancja(lista):
    n = len(lista)
    suma = 0

    for element in lista:
        suma += element

    srednia = suma / n

    suma_2 = 0

    for element in lista:
        suma_2 += (element - srednia) ** 2

    wariancja = suma_2 / (n - 1)

    return srednia, wariancja


def main():
    srednia, wariancja = srednia_wariancja([3, 3, 3, 3])
    print("Średnia wynosi: ", srednia)
    print("Wariancja wynosi: ", wariancja)

    srednia, wariancja = srednia_wariancja([5, 6, 7, 8, 9])
    print("Średnia wynosi: ", srednia)
    print("Wariancja wynosi: ", wariancja)


if __name__ == "__main__":
    main()
