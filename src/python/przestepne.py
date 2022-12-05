# ocenione na 100%, bez komentarzy
def lata_przestepne(od, do):
    return [rok for rok in range(od, do + 1)
            if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0]


def main():
    print(*lata_przestepne(1900, 2000), sep=", ")


if __name__ == "__main__":
    main()
