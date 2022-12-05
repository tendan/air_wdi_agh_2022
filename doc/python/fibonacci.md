Napisz funkcję liczącą wartość n-tego elementu ciągu Fibonacciego. Funkcja ma wykorzystywać rekurencyjną definicję tego ciągu:

```
Fn = 
{
    1           , dla n=1
    1           , dla n=2
    Fn−1+Fn−2   , dla n>2
}
```

Ponadto funkcja ma sprawdzać czy jako argument nie dostała wartości ujemnej  (lub zero) i w takim wypadku ma zwracać None

Zwróć uwagę na czas obliczeń. Spróbuj dla ilu elementów ciągu jesteś w stanie policzyć wartość funkcji w akceptowalnym czasie (38, 39, 40 ....)