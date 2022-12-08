# ocenione na 100%, bez komentarzy
from math import sin


def derivative(funkcja, punkt, przyrost=0.0001):
    # zwracanie wartości obliczonej ze wzoru na pochodną podanego w zadaniu
    return (funkcja(punkt + przyrost) - funkcja(punkt)) / przyrost


def main():
    # sep oddziela wartości podawane w print po przecinku podanym w nim napisem
    print("sin(x) w punkcie 1", derivative(sin, 1), sep=" = ")
    print("sin(x) w punkcie 0", derivative(sin, 0), sep=" = ")
    # lambda x: x ** 2
    # to jest shorthand od napisania oddzielnej funkcji liczącej kwadrat x i podanie tej funkcji jako argumentu

    # def kwadrat(x):
    #   return x ** 2
    # derivative(kwadrat, 1, 0.00001)

    print("x^2 w punkcie 1 z przyrostem 0.00001", derivative(lambda x: x ** 2, 1, 0.00001), sep=" = ")


if __name__ == "__main__":
    main()
