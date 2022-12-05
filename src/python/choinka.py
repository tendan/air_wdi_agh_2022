# ocenione na 100%, bez komentarzy
def main():
    n = int(input("Wprowadź n: "))
    for i in range(1, n + 1):
        for _ in range(n - i):
            print(" ", end="")
        for _ in range(i + (i - 1)):
            print("*", end="")
        print()


if __name__ == "__main__":
    main()
