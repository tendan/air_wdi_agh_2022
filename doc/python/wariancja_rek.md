Spróbujmy połączyć obie metody rekurencji, 'zwykłą' i ogonową, w jednej funkcji. Niech to będzie rekurencyjna wersja funkcji liczącej średnią i wariancję. Niech średnia będzie liczona jak w rekurencji ogonowej (w trakcie schodzenia 'w głąb'), a wariancja przy powrotach 'w górę'. Funkcja powinna mieć 3 parametry: listę, długość listy oraz sumę (do wyliczenia średniej, ustawiona na początku na 0).  UWAGA - parametr długość ma przechowywać początkową długość listy (tę z main-a), a nie długość pierwszego parametru z kolejnych wywołań.

Tak więc liczenie średniej może być identyczne jak ogonowe liczenie sumy elementów listy w poprzednim zadaniu. Jedynie na koniec, kiedy lista będzie pusta, należy zamiast zwrócenia sumy zwrócić krotkę: sumę podzieloną przez długość oraz 0 początkujące zliczanie sumy kwadratów. 

Natomiast zliczanie wariancji przebiega jak liczenie sumy w rekurencji zwykłej, tyle, że sumujemy kwadraty różnic dzielone przez długość i zwracamy krotkę: (średnia, dotychczasowa wariancja). 

W main-ie  dwukrotnie wywołaj napisaną funkcję z listami ```[3,3,3,3]``` oraz ```[5,6,7,8,9]``` i wypisz uzyskane wyniki