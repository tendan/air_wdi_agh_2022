# ocenione na 100%, bez komentarzy
def intersection(set1, set2):
    return list(set([element for element in set1 if element in set2]))


def main():
    lista1 = [2, 3, 5, 1, 5]
    lista2 = [3, 9, 8, 5, 3]

    print(*intersection(lista1, lista2), sep=", ")

    krotka1 = (2, 3, 5, 1, 5)
    krotka2 = (3, 9, 8, 5, 3)

    print(*intersection(krotka1, krotka2), sep=", ")

    napis1 = "Ala ma kota"
    napis2 = "Ala ma psa"

    print(list(intersection(napis1, napis2)))


if __name__ == "__main__":
    main()
