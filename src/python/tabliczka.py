# ocenione na 100%, bez komentarzy
def main():
    print(" ", end=" ")
    print(" | ", end=" ")

    for i in range(1, 10 + 1):
        print(f"{i:3}", end=" ")

    print()
    print("----------------------------------------------")

    for j in range(1, 10 + 1):
        print(f"{j:2}", "|", sep=" ", end=" ")
        for k in range(1, 10 + 1):
            print(f"{k * j:3}", end=" ")
        print()


if __name__ == "__main__":
    main()
