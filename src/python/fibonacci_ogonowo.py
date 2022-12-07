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
    if n <= 0:
        return None
    
    if n == 2 or n == 1:
        return b
    
    return element_fibonacciego(n - 1, b, a + b)

def main():
    print(element_fibonacciego(40))
    print(element_fibonacciego(1))


if __name__ == "__main__":
    main()