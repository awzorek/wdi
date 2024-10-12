# Przechowywanie salda i PINu
balance = 1000.0
pin = 1234

# Funkcja sprawdzająca, czy podany PIN jest poprawny
def check_pin():
    entered_pin = int(input("Podaj PIN: "))
    if entered_pin == pin:
        return True
    else:
        print("Niepoprawny PIN.")
        return False

# Funkcja do dokonywania wpłaty
def deposit():
    global balance
    amount = float(input("Podaj kwotę do wpłaty: "))
    balance += amount
    print(f"Wpłacono {amount:.2f} PLN.")

# Funkcja do dokonywania wypłaty
def withdraw():
    global balance
    amount = float(input("Podaj kwotę do wypłaty: "))
    if amount > balance: # d. Użytkownik nie może wybrać większej kwoty niż ta na koncie.
        print("Niewystarczające środki na koncie.")
    else:
        balance -= amount
        print(f"Wypłacono {amount:.2f} PLN.")

# Funkcja sprawdzająca saldo
def check_balance():
    print(f"Saldo wynosi {balance:.2f} PLN.")

while True:
    print("Dostępne operacje:\n"
          "1. Wpłata\n"
          "2. Wypłata\n"
          "3. Sprawdź saldo\n"
          "4. Zakończ")

    operation = int(input("Wybierz operację: "))

    # f. (Użytkownik może też zakończyć korzystanie z programu).
    if operation == 4:
        print("Koniec programu.")
        break

    # c. Przed każdą operacją należy zapytać użytkownika o PIN.
    if not check_pin():
        continue

    # Wybór operacji
    if operation == 1:
        deposit()
    elif operation == 2:
        withdraw()
    elif operation == 3:
        check_balance()
    else:
        print("Nieprawidłowa operacja.")

    print("Co chcesz zrobić w kolejnym kroku?") # f. Po każdej operacji powinien zostać wypisany komunikat: “Co chcesz zrobić w kolejnym kroku?”.