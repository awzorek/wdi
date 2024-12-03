def pascal_triangle(n, triangle = None):
    if triangle is None:
        triangle = []

    if n == 0:
        return triangle

    if not triangle:
        triangle.append([1])
    else:
        last_row = triangle[-1]
        new_row = [1]
        for i in range(1, len(last_row)):
            new_row.append(last_row[i - 1] + last_row[i])
        new_row.append(1)
        triangle.append(new_row)

    return pascal_triangle(n - 1, triangle)

def format_triangle(triangle):
    print("Trójkąt Pascala:")
    width = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        line = " ".join(map(str, row))
        print(line.center(width))

try:
    rows = int(input("Podaj liczbę rzędów: "))
    if rows <= 0:
        raise ValueError("Liczba rzędów musi być > 0.")
    triangle = pascal_triangle(rows)
    format_triangle(triangle)
except ValueError as e:
    print("Błąd:", e)