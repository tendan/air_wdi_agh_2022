# skończone
def suma_rek_zwykla(lista):
    # kiedy lista jest pusta (jej długość jest równa 0), wtedy zwróć None
    if len(lista) == 0:
        return None

    # kiedy lista ma jeden element, zwróć go
    # tutaj się kończy rekurencja
    if len(lista) == 1:
        return lista[0]

    # zwróć sumę pierwszego elementu listy i wywołania funkcji z tą samą listą, w której pomijamy pierwszy element
    # list[<from>:<to>]
    # listy zaczynają się od indeksu 0
    # gdy to jest puste, lista idzie do końca (kończymy na indeksie o jeden mniejszym od podanego w to)
    # gdy from jest puste, lista idzie od początku (zaczynamy wprost od indeksu podanego w from)
    return lista[0] + suma_rek_zwykla(lista[1:])


def suma_rek_ogonowa(lista, suma=0):
    # gdy lista jest pusta, zwróć None
    if len(lista) == 0:
        return None

    # gdy lista ma jeden element, zwróć jego sumę z sumą przekazywaną przez rekurencję ogonową
    # kończymy rekurencję
    if len(lista) == 1:
        return suma + lista[0]

    # zwracamy funkcję z listą pomijającą pierwszy element i dodajemy jej pierwszy element do istniejącej już sumy
    # wartość sumy wynika z wartości przekazanej w parametrze sumy
    # przy pierwszym wywołaniu suma jest równa 0 z uwagi na argument domyślny
    return suma_rek_ogonowa(lista[1:], suma + lista[0])
    

def main():
    lista = [1, 2, 3, 4, 5]
    lista2 = []
    print(suma_rek_zwykla(lista))
    print(suma_rek_ogonowa(lista))
    print(suma_rek_zwykla(lista2))
    print(suma_rek_ogonowa(lista2))

if __name__ == "__main__":
    main()