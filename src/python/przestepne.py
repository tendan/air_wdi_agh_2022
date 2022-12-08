# ocenione na 100%, bez komentarzy
def lata_przestepne(od, do):
    # utwórz listę lat za pomocą list comprehension w latach <od>-<do>
    return [rok for rok in range(od, do + 1)
            # wstaw element do listy tylko wtedy gdy spełnia podany warunek
            # rok jest przestępny gdy jest podzielny przez 4, jednocześnie nie będąc podzielnym przez 100
            # chyba że jest podzielny przez 400
            # wtedy rok jest przestępny
            if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0]


def main():
    # * to spread operator w Pythonie,
    # dzięki temu zamiast listy przekazujemy do printa elementy tak, jakby były podawane po przecinkach w print
    print(*lata_przestepne(1900, 2000), sep=", ")


if __name__ == "__main__":
    main()
