def check_prime(lst):
    primes = ("2", "3", "5", "7")
    for row in lst:
        all_prime = True # Czy wszystkie liczby w wierszu zawierają cyfrę pierwszą
        for num in row:
            has_prime = False # Czy liczba zawiera cyfrę pierwszą
            for digit in str(num):
                if digit in primes:
                    has_prime = True
                    break
            if not has_prime:
                all_prime = False
                break
        if all_prime:
            return True
    return False

# Wprowadzanie wymiaru tablicy
while True:
    try:
        n = int(input("Podaj wymiar tablicy: "))
        if n <= 0:
            raise ValueError("Wymiar tablicy musi być > 0")
        break
    except ValueError as e:
        print(f"Błąd: {e}.")

lst = []
print("Podaj liczby dla tablicy:")
# Wprowadzanie wierszy z liczbami
for i in range(n):
    while True:
        try:
            row = list(map(int, input(f"Wiersz {i + 1}: ").split()))
            if len(row) != n:
                raise ValueError(f"Wiersz musi zawierać dokładnie {n} liczb")
            lst.append(row)
            break
        except ValueError as e:
            print(f"Błąd: {e}.")

if check_prime(lst):
    print("W tablicy ISTNIEJE wiersz, w którym każda liczba zawiera co najmniej jedną cyfrę będącą liczbą pierwszą.")
else:
    print("W tablicy NIE ISTNIEJE wiersz, w którym każda liczba zawiera co najmniej jedną cyfrę będącą liczbą pierwszą.")