# Pobranie liczby od użytkownika z obsługą wyjątków
while True:
    try:
        n = int(input("Podaj liczbę całkowitą: "))
        # Sprawdzenie, czy liczba jest różna od 0
        if n != 0: 
            break
        else:
            print("Podaj liczbę całkowitą różną od 0.")
    except ValueError:
        print("Podaj poprawną liczbę całkowitą.")

print(f"Podzielniki liczby {n}:", end=" ")

# Zmiana znaku n na dodatni i ustawienie flagi, jeśli n jest ujemne
negative = False
if n < 0:
    n = -n
    negative = True

# Inicjalizacja zmiennej (dzielnika) i = 1
i = 1   

# Pętla while wykonująca się, dopóki i * i <= n (sprawdzanie do pierwiastka kwadratowego z n)
while i * i <= n:
    # Sprawdzenie, czy i jest dzielnikiem n
    if n % i == 0:
        if negative:
            print(i, -i, end=" ") # Wypisanie dodatnich i ujemnych podzielników
        else:
            print(i, end=" ") # Wypisanie dodatnich podzielników
        # Sprawdzenie, czy i != n // i (aby nie wyświetlać tego samego podzielnika dwa razy)
        if i != n // i:
            if negative:
                print(n // i, -(n // i), end=" ") # Wypisanie dodatnich i ujemnych podzielników
            else:
                print(n // i, end=" ") # Wypisanie dodatnich podzielników
    i += 1

# Przypadki testowe
# 0, "abc", 2.5, 100, -12