# ocenione na 100%, bez komentarzy
def main():
    suma = 0
    # dodawaj do sumy iloczyny i * i (i rośnie)
    for i in range(1, 11):
        suma += i * i

    # string formatting
    # można zastąpić:
    # print("Suma =", suma)
    print("Suma = %d" % (suma))


if __name__ == "__main__":
    main()
