# Pobranie od użytkownika liczby całkowitej (nieujemnej)
h = int(input("Podaj wysokość choinki: "))

# Wypisanie choinki
for i in range(h):
    spaces = " " * (h - i - 1) # Spacje do przesunięcia w prawo
    stars = "*" * (2 * i + 1) # Liczba gwiazdek
    print(spaces + stars) # Wypisanie linii