# ocenione na 100%, bez komentarzy
from math import sin


def derivative(funkcja, punkt, przyrost=0.0001):
    return (funkcja(punkt + przyrost) - funkcja(punkt)) / przyrost


def main():
    print("sin(x) w punkcie 1", derivative(sin, 1), sep=" = ")
    print("sin(x) w punkcie 0", derivative(sin, 0), sep=" = ")
    print("x^2 w punkcie 1 z przyrostem 0.00001", derivative(lambda x: x ** 2, 1, 0.00001), sep=" = ")


if __name__ == "__main__":
    main()
