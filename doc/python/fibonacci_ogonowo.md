NA poprzednich zajęciach program liczący n-ty element ciągu Fibonacciego czas obliczeń 40-ego przekraczał pół minuty.

Winien jest algorytm - każde uruchomienie funkcji wywołuje 2 kolejne wywołania - czas obliczeń rośnie wykładniczo. W dodatku obliczenia powtarzają się:
F(5)=F(4)+F(3)
F(4)=F(3)+F(2)  -- tu F(3) liczone jest powtórnie.

Lepszym algorytmem będzie ogonowa wersja funkcji, która będzie zapamiętywała n-1-wszy  i n-2-gi element ciągu w dodatkowych parametrach.
Zauważ różnicę w czasie obliczeń dla dużych n (38, 39, 40 ....).