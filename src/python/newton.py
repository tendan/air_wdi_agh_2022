# skończone
def dwumian(n, k):

    # gdy nie spełnia założeń dwumianu newtona, zwróć None
    if k < 0 or n < 0 or n < k:
        return None

    # gdy k == 0 lub k == n, kończ rekurencję, zwróć 1
    if k == 0 or k == n:
        return 1

    # zwracamy sumę dwumianów (jeden mniejszy w n o 1 i k o 1, drugi mniejszy w n o 1, a k nie zmienia wartości)
    # gdy skończy się schodzenie w dół, funkcja zwraca jedynkę, i sumuje w górę wynik zwracany ostatecznie
    return dwumian(n - 1, k - 1) + dwumian(n - 1, k)

def main():
    print(dwumian(8, 3))
    print(dwumian(-3, 5))
    print(dwumian(3, 5))
    print(dwumian(4, -5))

if __name__ == "__main__":
    main()