# ocenione na 100%, bez komentarzy
def intersection(set1, set2):
    # tworzymy za pomocą list compehension listę
    # elementy z set1 są dodawane, tylko wtedy, gdy zawarte są one w set2
    # żeby pozbyć się duplikatów używamy set() (taka sympatyczna struktura danych, która zawiera jedynie
    # elementy o unikalnych wartościach
    # potem konwertujemy to na listę (żeby móc potem operować na tym, jak na liście)
    return list(set([element for element in set1 if element in set2]))


def main():
    lista1 = [2, 3, 5, 1, 5]
    lista2 = [3, 9, 8, 5, 3]

    # spread operator
    # przekazywanie do print elementów, jakby każdy był przekazywany jak po przecinku
    # sep, żeby każdy element był rozdzielony ", "
    print(*intersection(lista1, lista2), sep=", ")

    # dla krotek też działa
    krotka1 = (2, 3, 5, 1, 5)
    krotka2 = (3, 9, 8, 5, 3)

    # jak wyżej
    print(*intersection(krotka1, krotka2), sep=", ")

    # dla napisów też działa
    napis1 = "Ala ma kota"
    napis2 = "Ala ma psa"

    # tym razem przekazujemy bezpośrednią listę, żeby ułatwić sobie czytelność unikalnych wspólnych elementów
    print(list(intersection(napis1, napis2)))


if __name__ == "__main__":
    main()
