# skończone
def element_fibonacciego(n):
    # gdy n <= 0 (bo nie spełnia założeń ciągu), wtedy zwróć None
    if n <= 0:
        return None
    # gdy n == 1 lub n == 2 zwróć 1
    # (działa zarówno przy podaniu tych wartości jako argumentu, jak i przy zakończeniu rekurencji)
    if n == 1 or n == 2:
        return 1
    # gdy n > 2 wtedy wywołuj rekurencyjnie sumę elementu o 1 mniejszego i o 2 mniejszego
    # w momencie kiedy n == 1 lub n == 2, rekurencja się kończy i wracamy z powrotem w górę
    elif n > 2:
        return element_fibonacciego(n - 1) + element_fibonacciego(n - 2)

def main():
    print(element_fibonacciego(-1))
    print(element_fibonacciego(40))

if __name__ == "__main__":
    main()