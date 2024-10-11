# a. Aby zdefiniować zakres, użytkownik wprowadza 2 liczby.
# c. Operujemy na liczbach całkowitych.
start = int(input("Podaj pierwszą liczbę (początek zakresu): "))
end = int(input("Podaj drugą liczbę (koniec zakresu): "))

# Utworzenie listy z liczbami w zadanym zakresie i określenie jej rozmiaru
numbers = list(range(start, end + 1))
size = len(numbers)

# d. Jeśli zakres jest większy niż 20, należy wypisać tylko 6 liczb z tego zakresu, które są najbliżej średniej (bez samej średniej).
if size > 20:
    # Obliczenie średniej
    average = int(sum(numbers) / size)
    
    # Lista odległości od średniej (bez samej średniej)
    distances = []
    for n in numbers:
        if n != average:
            distances.append((abs(n - average), n))
    
    # Sortowanie odłegłości (rosnąco)
    distances.sort()
    
    # Wybranie 6 liczb najbliższych od średniej (oraz sortowanie rosnąco)
    closest_numbers = []
    for n in distances[:6]:
        closest_numbers.append(n[1])
    closest_numbers.sort()
    
    # Wypisanie liczb
    print("Liczby najbliższe średniej w tym zakresie:")
    i = 0
    while i < len(closest_numbers):
        print(closest_numbers[i]) # b. Po kolei, w kolejnych linijkach.
        i += 1
else:
    # Wypisanie liczb
    print("Liczby w tym zakresie:")
    for i in numbers:
        print(i) # b. Po kolei, w kolejnych linijkach.