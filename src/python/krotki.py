# ocenione na 100%, bez komentarzy
def suma_krotek(lista):
    nowa_lista = []

    for a, b in lista:
        nowa_lista.append(a + b)

    return nowa_lista


def main():
    lista1 = [(1, 2), (3, 4), (5, 6), (7, 8)]
    lista2 = [('a', 'b'), ('a', 'c'), ('b', 'c')]

    print(suma_krotek(lista1))
    print(suma_krotek(lista2))


if __name__ == "__main__":
    main()
