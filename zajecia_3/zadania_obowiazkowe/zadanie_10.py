# c. W przypadku losowania liczby należy skorzystać z biblioteki random.
import random

def calculator():
    while True:
        # a. Użytkownik powinien wpisywać liczby po kolei zatwierdzając je przy pomocy klawisza ENTER...
        n1 = float(input("Wpisz pierwszą liczbę: "))
        n2 = float(input("Wpisz drugą liczbę: "))
        print("Dostępne operacje:\n"
              "+ Dodawanie\n"
              "- Odejmowanie\n"
              "* Mnożenie\n"
              "/ Dzielenie\n"
              "# Potęgowanie\n"
              "^ Pierwiastkowanie\n"
              "x Losowanie liczby z zakresu")
        # a. ...a następnie podać jeden z 6 symboli: +, -, *, /, #, ^, x.
        operation = input("Wybierz operację: ")

        if operation == "+":
            result = n1 + n2
        elif operation == "-":
            result = n1 - n2
        elif operation == "*":
            result = n1 * n2
        elif operation == "/":
            if n2 != 0:
                result = n1 / n2
            else:
                result = "Dzielenie przez 0 jest niemożliwe."
        elif operation == "^":
            result = n1 ** n2
        elif operation == "#":
            result = n1 ** 0.5, n2 ** 0.5
        elif operation == "x":
            result = random.uniform(n1, n2)
        else:
            result = "Nieprawidłowa operacja."

        print(f"Wynik: {result}")
        # b. Po zakończeniu obliczeń powinien zostać wypisany komunikat: “Czy chcesz wprowadzić nowe dane?”. W zależności od odpowiedzi “T”/“N” należy umożliwić wprowadzenie nowych danych.
        continue_calc = input("Czy chcesz wprowadzić nowe dane? (T/N): ")
        if continue_calc != "T":
            print("Koniec programu.")
            break

calculator()