import math

class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def add(self, other):
        return ComplexNumber(round(self.re + other.re, 2), round(self.im + other.im, 2))

    def subtract(self, other):
        return ComplexNumber(round(self.re - other.re, 2), round(self.im - other.im, 2))

    def multiply(self, other):
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + self.im * other.re
        return ComplexNumber(round(re, 2), round(im, 2))

    def divide(self, other):
        denominator = other.re**2 + other.im**2
        re = (self.re * other.re + self.im * other.im) / denominator
        im = (self.im * other.re - self.re * other.im) / denominator
        return ComplexNumber(round(re, 2), round(im, 2))

    def power(self, n):
        r = math.sqrt(self.re**2 + self.im**2)
        phi = math.atan2(self.im, self.re)
        r_n = r ** n
        phi_n = phi * n
        re = r_n * math.cos(phi_n)
        im = r_n * math.sin(phi_n)
        return ComplexNumber(round(re, 2), round(im, 2))

    def __str__(self):
        Re = round(self.re, 2)
        Im = round(self.im, 2)
        Re_str = f"{Re:.2f}".rstrip('0').rstrip('.')
        Im_str = f"{Im:.2f}".rstrip('0').rstrip('.')
        if Im == 0:
            return f"{Re_str}"
        elif Re == 0:
            return f"{Im_str}i"
        elif Im > 0:
            return f"{Re_str} + {Im_str}i"
        else:
            return f"{Re_str} - {Im_str.lstrip('-')}i"

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