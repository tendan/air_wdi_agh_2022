# skończone
def suma_rek_zwykla(lista):
    if len(lista) == 0:
        return None
    if len(lista) == 1:
        return lista[0]
    
    return lista[0] + suma_rek_zwykla(lista[1:])

def suma_rek_ogonowa(lista, suma=0):
    if len(lista) == 0:
        return None
    if len(lista) == 1:
        return suma + lista[0]
    
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