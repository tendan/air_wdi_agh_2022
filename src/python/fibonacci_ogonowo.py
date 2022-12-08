# ocenione na 60% (nierozpatrzenie przypadku, w którym n <= 0)
def element_fibonacciego(n, a=1, b=1):
    #n -= 2
    #a, b = 1, 1
    #i = 0
    #while (i < n):
    #    a, b = b, a + b
    #    i += 1
    #
    #return b

    # o tym przypadku mowa...
    # gdy nie spełnione są założenia ciągu zwróć None
    if n <= 0:
        return None

    # gdy dojdziemy do n == 2 lub n == 1, wtedy zwracamy wyliczony z rekurencji ogonowej b
    if n == 2 or n == 1:
        return b

    # zwracamy rekurencyjnie dla n zmniejszanego o 1 dla każdego powtórzenia
    # ale zamieniamy wartość z a pod wartość z pierwotnego b
    # a wartość b zamieniamy na sumę pierwotnego a i pierwotnego b
    return element_fibonacciego(n - 1, b, a + b)

def main():
    print(element_fibonacciego(40))
    print(element_fibonacciego(1))


if __name__ == "__main__":
    main()