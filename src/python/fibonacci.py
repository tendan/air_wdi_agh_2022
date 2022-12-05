# skończone
def element_fibonacciego(n):
    if n <= 0:
        return None
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return element_fibonacciego(n - 1) + element_fibonacciego(n - 2)

def main():
    print(element_fibonacciego(-1))
    print(element_fibonacciego(40))

if __name__ == "__main__":
    main()