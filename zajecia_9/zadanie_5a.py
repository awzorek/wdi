import math

def add(z1, z2):
    return (z1[0] + z2[0], z1[1] + z2[1])

def subtract(z1, z2):
    return (z1[0] - z2[0], z1[1] - z2[1])

def multiply(z1, z2):
    return (z1[0] * z2[0] - z1[1] * z2[1], z1[0] * z2[1] + z1[1] * z2[0])

def divide(z1, z2):
    denominator = z2[0]**2 + z2[1]**2
    return ((z1[0] * z2[0] + z1[1] * z2[1]) / denominator, (z1[1] * z2[0] - z1[0] * z2[1]) / denominator)

def power(z, n):
    r = math.sqrt(z[0]**2 + z[1]**2)
    phi = math.atan2(z[1], z[0])
    r_n = r ** n
    phi_n = phi * n
    return (r_n * math.cos(phi_n), r_n * math.sin(phi_n))

def print_complex(z):
    Re = int(z[0]) if z[0].is_integer() else z[0]
    Im = int(z[1]) if z[1].is_integer() else z[1]
    if Im == 0:
        return f"{Re}"
    else:
        return f"{Re} + {Im}i"

def read_complex(coefficient):
    while True:
        try:
            components = input(f"Podaj współczynnik {coefficient}: ").split()
            Re = float(components[0])
            Im = float(components[1])
            return (Re, Im)
        except (ValueError, IndexError):
            print("Błąd: wprowadź poprawne liczby w formacie (Re Im).")

def print_equation(a, b, c):
    a_str = print_complex(a)
    b_str = print_complex(b)
    c_str = print_complex(c)
    print(f"\nRównanie kwadratowe: ({a_str}) * z^2 + ({b_str}) * z + ({c_str}) = 0")

def solve_quadratic(a, b, c):
    if a == (0, 0):
        print("To nie jest równanie kwadratowe - współczynnik a = 0.")
        return None, None

    delta = subtract(power(b, 2), multiply((4, 0), multiply(a, c)))
    sqrt_delta = power(delta, 0.5)
    
    z1 = divide(subtract(sqrt_delta, b), multiply((2, 0), a))
    z2 = divide(subtract((-sqrt_delta[0], -sqrt_delta[1]), b), multiply((2, 0), a))
    
    if math.isclose(z1[0], z2[0], abs_tol=1e-9) and math.isclose(z1[1], z2[1], abs_tol=1e-9):
        return z1, None
    return z1, z2

print("Wczytaj współczynniki zespolone równania kwadratowego (część rzeczywista i urojona oddzielone spacją):")
a = read_complex("a")
b = read_complex("b")
c = read_complex("c")
print_equation(a, b, c)
solutions = solve_quadratic(a, b, c)
if solutions[0] is not None:
    print("\nRozwiązania równania kwadratowego:")
    if solutions[1] is None:
        print(f"z0 = {print_complex(solutions[0])}")
    else:
        print(f"z1 = {print_complex(solutions[0])}")
        print(f"z2 = {print_complex(solutions[1])}")