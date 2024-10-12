# Biblioteka random do losowania
import random

# Pobranie od użytkownika liczby całkowitej (nieujemnej)
h = int(input("Podaj wysokość choinki: "))

# Wypisanie wierzchołka choinki (gwiazda)
print(" " * (h - 1) + "X")

# Wypisanie choinki
for i in range(1, h):
    spaces = " " * (h - i - 1) # Spacje do przesunięcia w prawo
    stars = 2 * i + 1 # Liczba gwiazdek/bombek

    line = spaces  # Linia

    for j in range(stars):
        # Losowanie, czy w danym miejscu ma być "o" czy "*"
        if random.choice([True, False]):
            line += "o"
        else:
            line += "*"

    print(line) # Wypisanie linii

# Pień choinki
spaces = " " * (h - 1) # Spacje
print(spaces + "U") # Wypisujemy pień choinki