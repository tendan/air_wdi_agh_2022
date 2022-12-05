Napisz funkcję znajdującą wspólne elementy dwóch sekwencji (list, krotek lub napisów). Znalezione wspólne elementy mają być zwracane jako lista (każdy element w tej liście ma wystąpić tylko raz! - wykorzystaj konwersję do zbioru, ale proszę nie używać intersection - zależy mi na list comprehension)

Uzupełnienie wykładu:

W list comprehension może wystąpć pętla zagnieżdżona np.:

```
[x**y for x in range (1,4) for y in range (2,5) ]
```

stworzy listę liczb będących 2, 3 i 4 potęgą  liczb z zakresu 1-3