# ocenione na 100%, bez komentarzy
def srednia_wariancja(lista):
    # liczymy długość listy za pomocą metody len
    n = len(lista)
    suma = 0

    # zsumuj wszystkie elementy zawarte w liście
    for element in lista:
        suma += element

    # policz średnią
    srednia = suma / n

    # suma pomocnicza dla wariancji
    suma_2 = 0

    # znowu przechodzimy po elementach listy
    for element in lista:
        # tym razem dodajemy do suma_2 kwadraty różnic elementów i średniej
        suma_2 += (element - srednia) ** 2

    # wyliczamy wariancję
    wariancja = suma_2 / (n - 1)

    # zwracamy jako krotkę średnią i wariancję
    return srednia, wariancja


def main():
    # gdy funkcja zwraca krotkę, można przechwycić jej elementy np. do dwóch różnych zmiennych podanych po przecinku
    srednia, wariancja = srednia_wariancja([3, 3, 3, 3])
    print("Średnia wynosi: ", srednia)
    print("Wariancja wynosi: ", wariancja)

    # to samo jak wyżej
    srednia, wariancja = srednia_wariancja([5, 6, 7, 8, 9])
    print("Średnia wynosi: ", srednia)
    print("Wariancja wynosi: ", wariancja)


if __name__ == "__main__":
    main()
