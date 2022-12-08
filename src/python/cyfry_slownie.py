# ocenione na 100%, bez komentarzy
slownik = {
    '0': 'zero',
    '1': 'jeden',
    '2': 'dwa',
    '3': 'trzy',
    '4': 'cztery',
    '5': 'pięć',
    '6': 'sześć',
    '7': 'siedem',
    '8': 'osiem',
    '9': 'dziewięć',
}


def slownie(ciag_cyfr):
    # utwórz pusty napis do którego będziemy dodawać elementy ze słownika
    literal = ""

    # przejdź po wszystkim elementach ciągu cyfr podanego jako argument metody slownie
    for cyfra in ciag_cyfr:
        # jeżeli cyfra z ciągu jest zawarta w słowniku, dodaj wartość przypisaną pod klucz do pierwotnie pustego napisu
        if cyfra in slownik:
            # x += 1 to jest "shorthand" od x = x + 1
            # oprócz dodania wyrazu ze słownika znajdującego się pod kluczem "cyfra"
            # dodaj na końcu pusty znak jako odstęp
            literal += slownik[cyfra] + ' '

    # zwróć wyprodukowany literał
    return literal


def main():
    print(slownie("1410"))


if __name__ == "__main__":
    main()
