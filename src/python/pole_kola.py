# ocenione na 100%, bez komentarzy
from math import pi


def pole_kola(r):
    return r * r * pi


def main():
    r = float(input("Proszę podać promień: "))
    pole = pole_kola(r)

    print("Pole koła wynosi %f" % (pole))


if __name__ == "__main__":
    main()
