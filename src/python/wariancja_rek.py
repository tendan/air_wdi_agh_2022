# ocenione na 100%
def wariancja_rek(lista, dlugosc, suma=0):
    # gdy lista jest pusta (jej długość jest równa 0) zwróć krotkę, która zwraca:
    # w pierwszym elemencie wyliczoną średnią
    # w drugim elemencie wyliczoną wariancję, która początkowo wynosi 0
    # kończymy pierwszy etap rekurencyjności (rekurencji ogonowej)
    if len(lista) == 0:
        return (suma / dlugosc, 0)

    # przypisujemy do krotka, rezultat wyliczony rekurencyjnie
    krotka = wariancja_rek(lista[1:], dlugosc, suma + lista[0])

    # zwracamy wyliczoną średnią jako pierwszy element krotki
    # i wyliczoną póki co wariancję w drugim elemencie
    # dodajemy do poprzednio wyliczonej wariancji, wyliczony składnik ze wzoru
    return krotka[0], krotka[1] + ((lista[0] - krotka[0]) ** 2 / (dlugosc - 1))
    

def main():
    print(wariancja_rek([3, 3, 3, 3], 4))
    print(wariancja_rek([5, 6, 7, 8, 9], 5))


if __name__ == "__main__":
    main()