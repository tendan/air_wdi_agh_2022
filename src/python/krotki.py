# ocenione na 100%, bez komentarzy
def suma_krotek(lista):
    # utwórz pustą listę, by mieć do czego dodawać wyliczone elementy
    nowa_lista = []

    # (for element1, element2 in lista)
    # działa na podobnej zasadzie co:
    # a, b = (3, 5) => a == 3 i b == 5
    # wyodrębniamy wartości z krotki przypisując je automatycznie do utworzonych przez for eacha zmiennych
    # lista ma się składać z krotek
    for a, b in lista:
        nowa_lista.append(a + b)

    # zwróć wynikową listę
    return nowa_lista


def main():
    lista1 = [(1, 2), (3, 4), (5, 6), (7, 8)]
    lista2 = [('a', 'b'), ('a', 'c'), ('b', 'c')]

    print(suma_krotek(lista1))
    print(suma_krotek(lista2))


if __name__ == "__main__":
    main()
