# Wprowadzenie 5. liczb do listy (z zabezpieczeniami)
numbers = []
while len(numbers) < 5:
    try:
        n = int(input(f"Podaj {len(numbers) + 1}. liczbę całkowitą: "))
        if len(numbers) == 0 or n != numbers[-1]:
            numbers.append(n)
        else:
            print("Dwie sąsiadujące ze sobą liczby nie mogą być takie same.")
    except ValueError:
        print("Podaj poprawną liczbę całkowitą.")

# Pętla przechodząca przez wszystkie n - 1 elementów listy
i = 0
while i < len(numbers) - 1:
    # Sprawdzanie, czy różnica między sąsiadującymi liczbami jest większa niż 1 - jeśli nie to nie wstawiamy żadnego elementu
    if abs(numbers[i] - numbers[i + 1]) > 1:
        if numbers[i] < numbers[i + 1]:
            numbers.insert(i + 1, numbers[i] + 1) # Jeśli pierwsza liczba jest mniejsza od drugiej - wstawienie liczby o 1 większej...
        else:
            numbers.insert(i + 1, numbers[i] - 1) # ...w przeciwnym razie - wstawienie liczby o 1 mniejszej
    i += 1

print(f"Uzupełniona lista: {numbers}")