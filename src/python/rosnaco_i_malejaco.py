# ocenione na 100%, komentarz: "spacja jest domyslnym separatorem, nie trzeba jej podawać jako argument"
def main():
    n = int(input("Wprowadź n: "))

    for i in range(n + 1):
        print(i, n - i, sep=' ')


if __name__ == "__main__":
    main()
