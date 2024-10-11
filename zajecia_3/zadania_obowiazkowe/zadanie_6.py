# Pobranie dwóch liczb od użytkownika
n1 = float(input("Podaj pierwszą liczbę: "))
n2 = float(input("Podaj drugą liczbę: "))

# d. Należy sprawdzić czy obie liczby są mniejsze od 0. Jeśli tak, należy zakończyć program i dać o tym znać użytkownikowi.
if n1 < 0 and n2 < 0:
    print("Obie liczby są mniejsze od 0. Koniec programu.")
else:
    # e. Jeśli tylko jedna liczba jest mniejsza od 0, należy wykorzystać jej wartość bezwzględną.
    if n1 < 0:
        n1 = abs(n1)
    if n2 < 0:
        n2 = abs(n2)

    # Obliczenia
    sum_res = n1 + n2
    diff = n1 - n2
    product = n1 * n2
    if n2 != 0:
        quotient = n1 / n2
    else:
        quotient = "Nie można dzielić przez 0."

    square_n1 = n1 ** 2
    square_n2 = n2 ** 2

    sqrt_n1 = n1 ** 0.5
    sqrt_n2 = n2 ** 0.5

    # Wypisanie wyników
    print(f"Suma: {sum_res}")
    print(f"Różnica: {diff}")
    print(f"Iloczyn: {product}")
    print(f"Różnica: {quotient}")
    print(f"Kwadrat pierwszej liczby: {square_n1}")
    print(f"Kwadrat drugiej liczby: {square_n2}")
    print(f"Pierwiastek kwadratowy pierwszej liczby: {sqrt_n1}")
    print(f"Pierwiastek kwadratowy drugiej liczby: {sqrt_n2}")

    # f. Jeśli wynik mnożenia liczb to 10, należy dodatkowo wypisać “Yay!”.
    if product == 10:
        print("Yay!")


# Przypadki testowe:

# 1. Obie liczby są większe niż 0
# Wejście: 4, 5
# Wyjście:
# Suma: 9.0
# Różnica: -1.0
# Iloczyn: 20.0
# Różnica: 0.8
# Kwadrat pierwszej liczby: 16.0
# Kwadrat drugiej liczby: 25.0
# Pierwiastek kwadratowy pierwszej liczby: 2.0
# Pierwiastek kwadratowy drugiej liczby: 2.23606797749979

# 2. Pierwsza liczba jest mniejsza niż 0, druga jest większa niż 0
# Wejście: -3, 6
# Wyjście:
# Suma: 9.0
# Różnica: -3.0
# Iloczyn: 18.0
# Różnica: 0.5
# Kwadrat pierwszej liczby: 9.0
# Kwadrat drugiej liczby: 36.0
# Pierwiastek kwadratowy pierwszej liczby: 1.7320508075688772
# Pierwiastek kwadratowy drugiej liczby: 2.449489742783178

# 3. Pierwsza liczba jest większa niż 0, druga jest mniejsza niż 0
# Wejście: 7, -2
# Wyjście:
# Suma: 9.0
# Różnica: 5.0
# Iloczyn: 14.0
# Różnica: 3.5
# Kwadrat pierwszej liczby: 49.0
# Kwadrat drugiej liczby: 4.0
# Pierwiastek kwadratowy pierwszej liczby: 2.6457513110645907
# Pierwiastek kwadratowy drugiej liczby: 1.4142135623730951

# 4. Obie liczby są mniejsze niż 0
# Wejście: -4, -5
# Wyjście:
# Obie liczby są mniejsze od 0. Koniec programu.

# 5. Jedna liczba to 0, druga większa niż 0
# Wejście: 0, 3
# Wyjście:
# Suma: 3.0
# Różnica: -3.0
# Iloczyn: 0.0
# Różnica: 0.0
# Kwadrat pierwszej liczby: 0.0
# Kwadrat drugiej liczby: 9.0
# Pierwiastek kwadratowy pierwszej liczby: 0.0
# Pierwiastek kwadratowy drugiej liczby: 1.7320508075688772

# 6. Jedna liczba to 0, druga mniejsza niż 0
# Wejście: 0, -7
# Wyjście:
# Suma: 7.0
# Różnica: -7.0
# Iloczyn: 0.0
# Różnica: 0.0
# Kwadrat pierwszej liczby: 0.0
# Kwadrat drugiej liczby: 49.0
# Pierwiastek kwadratowy pierwszej liczby: 0.0
# Pierwiastek kwadratowy drugiej liczby: 2.6457513110645907

# 7. Obie liczby to 0
# Wejście: 0, 0
# Wyjście:
# Suma: 0.0
# Różnica: 0.0
# Iloczyn: 0.0
# Różnica: Nie można dzielić przez 0.
# Kwadrat pierwszej liczby: 0.0
# Kwadrat drugiej liczby: 0.0
# Pierwiastek kwadratowy pierwszej liczby: 0.0
# Pierwiastek kwadratowy drugiej liczby: 0.0

# 8. Iloczyn wynosi 10
# Wejście: 2, 5
# Wyjście:
# Suma: 7.0
# Różnica: -3.0
# Iloczyn: 10.0
# Różnica: 0.4
# Kwadrat pierwszej liczby: 4.0
# Kwadrat drugiej liczby: 25.0
# Pierwiastek kwadratowy pierwszej liczby: 1.4142135623730951
# Pierwiastek kwadratowy drugiej liczby: 2.23606797749979
# Yay!