Napisz funkcję tworzącą listę wszystkich lat przestępnych z podanego przedziału. Przypominam, że rok jest przestępny, jeżeli jest podzielny przez 4, ale nie jest podzielny przez 100, chyba, że jest podzielny przez 400. Ciało funkcji ma się składać z jednej linijki kodu zawierającej list comprehension.

Wywołaj napisaną funkcję do wygenerowania listy lat przestępnych w latach 1900-2000.

Uzupełnienie wykładu:

W list comprehension może też wystąpić warunek np.:

```
[x**2 for x in range (10) if x % 2 == 0 or x % 3 == 0]
```

stworzy listę kwadratów tych liczb z przedziału 0-9, które są podzielne przez2 lub przez 3