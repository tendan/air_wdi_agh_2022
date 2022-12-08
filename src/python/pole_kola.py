# ocenione na 100%, bez komentarzy
from math import pi


def pole_kola(r):
    # zwróć wartość pola koła obliczoną wzorem na pole koła
    return r * r * pi


def main():
    # wprowadzamy wartość podaną przez użytkownika w input i zamieniamy ją na wartość rzeczywistą (float())
    r = float(input("Proszę podać promień: "))

    # przypisz wartość pola koła do zmiennej pole
    pole = pole_kola(r)

    # string formatting, można zastąpić:
    # print("Pole koła wynosi", pole)
    print("Pole koła wynosi %f" % (pole))


if __name__ == "__main__":
    main()
