Napisz program wypisujący tabliczkę mnożenia 10x10 w postaci jak poniżej:

```
   |  1  2  3  4  5  6  7  8  9 10
---------------------------------
 1 |  1  2  3  4  5  6  7  8  9 10
 2 |  2  4  6  8 10 12 14 16 18 20
 3 |  3  6  9 12 15 18 21 24 27 30
```
itd.

Liczby powinny być w kolumnach z wyrównaniem do prawej. W wersji uproszczonej można pominąć "ozdobniki" (linie oraz numery kolumn i wierszy).

UWAGA: Aby wypisywać liczby kilkoma printami w jednym wierszu należy ustawić dodatkowy parametr funkcji print - end:

Na przykład:

print( 5, end="")

print(6, end="")

wypisze:

56

Formatowania wydruku w Pythonie

Załóżmy, że chcemy wypisać liczbę 1-cyfrową na 9-ciu pozycjach (czyli dołożyć jej z przodu 8 spacji). Można to osiągnąć przez formatowanie wydruku.

W pythonie istnieje kilka sposobów na formatowanie wydruku (czyli np. tego jak wypisywane są liczby na ekran). Obecnie od Pythona 3.6 wprowadzone zostały f-napisy (f-strings). W tym podejściu przed napisem przekazywanym do funkcji print dodaje się literę f, natomiast zmienne, które do tej pory umieszczaliśmy po przecinkach są wstawiane do tego napisu otoczone nawiasami {} (czyli zamiast print("Promień koła wynosi", r, "cm") piszemy print(f"Promień koła wynosi  {r} cm")).

Taka notacja pozwala dołożyć informację o formatowaniu. Zadanie z wypisaniem liczby 5 na 9-ciu pozycjach wyglądałoby tak:

print(f"Liczba na dziewięciu pozycjach: {5:9}")  co wypisze:

Liczba na dziewięciu pozycjach:         5

Inne przykłady:

print(f"Liczba na trzech pozycjach uzupełniona zerami {5:03}" ) wypisze:

Liczba na trzech pozycjach uzupełniona zerami: 005

print(f"Liczba z dwoma miejscami po przecinku: {5:.2f}") wypisze:

Liczba z dwoma miejscami po przecinku: 5.00


Alternatywny, 'stary', zapis powyższych przykładów:

print("Liczba na dziewięciu pozycjach: {:9d}".format(5) )
print("Liczba na trzech pozycjach uzupełniona zerami {:03d}".format(5) )
print("Liczba z dwoma miejscami po przecinku: {:.2f}".format(5) ) 



Alternatywny, 'jeszcze starszy', zapis powyższych przykładów:

print("Liczba na dziewięciu pozycjach: %9d" %5 )

print("Liczba na trzech pozycjach uzupełniona zerami %03d" % 5 )

print("Liczba z dwoma miejscami po przecinku: %.2f"% 5 ):