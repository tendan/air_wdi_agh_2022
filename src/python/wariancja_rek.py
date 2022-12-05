# nieocenione przez Pawlika
def wariancja_rek(lista, dlugosc, suma=0):
    if len(lista) == 0:
        return (suma / dlugosc, 0)
        
    krotka = wariancja_rek(lista[1:], dlugosc, suma + lista[0])
    
    return krotka[0], krotka[1] + ((lista[0] - krotka[0]) ** 2 / (dlugosc - 1))
    

def main():
    print(wariancja_rek([3, 3, 3, 3], 4))
    print(wariancja_rek([5, 6, 7, 8, 9], 5))


if __name__ == "__main__":
    main()