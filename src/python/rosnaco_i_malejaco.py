# ocenione na 100%, komentarz: "spacja jest domyslnym separatorem, nie trzeba jej podawać jako argument"
def main():
    n = int(input("Wprowadź n: "))

    # przejdź się po liście utworzonej w funkcji range
    for i in range(n + 1):
        # podaj indeks i (wartość, która rośnie)
        # podaj n - i (wartość, która maleje) (n jest stałe, i rośnie, więc ich różnica będzie zwracała malejący wynik)
        print(i, n - i, sep=' ')


if __name__ == "__main__":
    main()
