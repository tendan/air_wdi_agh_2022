 Napisz funkcję derivative, która otrzyma jako parametry funkcję (f), punkt (x) i przyrost (h), a zwróci przybliżoną wartość pochodnej funkcji f w punkcie x. Przybliżoną wartość pochodnej uzyskuje się ze wzoru na iloraz różnicowy:


(f(x+h)−f(x)) / h


Niech w funkcji derivative h będzie parametrem z wartością domyślną równą 0.0001

W programie wypisz wartości funkcji:

sin(x) w punkcie 1

sin(x) w punkcie 0

x^2 (podniesienie do kwadratu) w punkcie 1 z przyrostem 0.00001

Funkcja sin jest dostępna w module math (należy zaimportować moduł przez:

```import math``` - wtedy funkcja sin będzie dostępna jako math.sin

Funkcję x^2 należy zaimplementować samemu.