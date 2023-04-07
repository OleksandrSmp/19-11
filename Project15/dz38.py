import math
class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.reduce_fraction()

    def reduce_fraction(self):
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        common_divisor = gcd(self.a, self.b)
        self.a //= common_divisor
        self.b //= common_divisor

    def __add__(self, other):
        lcm = self.b * other.b // math.gcd(self.b, other.b)
        a = lcm // self.b * self.a + lcm // other.b * other.a
        b = lcm
        return Fraction(a, b)

    def __sub__(self, other):
        lcm = self.b * other.b // math.gcd(self.b, other.b)
        a = lcm // self.b * self.a - lcm // other.b * other.a
        b = lcm
        return Fraction(a, b)

    def __mul__(self, other):
        a = self.a * other.a
        b = self.b * other.b
        return Fraction(a, b)

    def __eq__(self, other):
        return self.a // math.gcd(self.a, self.b) == other.a // math.gcd(other.a, other.b) and self.b // math.gcd(
            self.a, self.b) == other.b // math.gcd(other.a, other.b)

    def __gt__(self, other):
        return self.a * other.b > self.b * other.a

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True

