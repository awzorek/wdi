import math

class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def add(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def subtract(self, other):
        return ComplexNumber(self.re - other.re, self.im - other.im)

    def multiply(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def divide(self, other):
        denominator = other.re**2 + other.im**2
        return ComplexNumber((self.re * other.re + self.im * other.im) / denominator, (self.im * other.re - self.re * other.im) / denominator)

    def power(self, n):
        r = math.sqrt(self.re**2 + self.im**2)
        phi = math.atan2(self.im, self.re)
        r_n = r ** n
        phi_n = phi * n
        return ComplexNumber(r_n * math.cos(phi_n), r_n * math.sin(phi_n))

    def __str__(self):
        Re = int(self.re) if self.re.is_integer() else self.re
        Im = int(self.im) if self.im.is_integer() else self.im
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
            return ComplexNumber(Re, Im)
        except (ValueError, IndexError):
            print("Błąd: wprowadź poprawne liczby w formacie (Re Im).")

def print_equation(a, b, c):
    print(f"\nRównanie kwadratowe: ({a}) * z^2 + ({b}) * z + ({c}) = 0")

def solve_quadratic(a, b, c):
    if a.re == 0 and a.im == 0:
        print("To nie jest równanie kwadratowe - współczynnik a = 0.")
        return None, None

    delta = b.power(2).subtract(a.multiply(c).multiply(ComplexNumber(4, 0)))
    sqrt_delta = delta.power(0.5)
    
    z1 = sqrt_delta.subtract(b).divide(a.multiply(ComplexNumber(2, 0)))
    z2 = ComplexNumber(-sqrt_delta.re, -sqrt_delta.im).subtract(b).divide(a.multiply(ComplexNumber(2, 0)))
    
    if math.isclose(z1.re, z2.re, abs_tol=1e-9) and math.isclose(z1.im, z2.im, abs_tol=1e-9):
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
        print(f"z0 = {solutions[0]}")
    else:
        print(f"z1 = {solutions[0]}")
        print(f"z2 = {solutions[1]}")