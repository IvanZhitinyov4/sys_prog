from fractions import Fraction
from typing import Union


class Rational:
    def __init__(self, m: Union[int, float, Fraction] = 0, n: Union[int, float] = 1):
        if isinstance(m, (int, float)):
            m = Fraction(m)
        else:
            raise ValueError
        if isinstance(n, (int, float)):
            n = Fraction(n)
        else:
            raise ValueError
        if n == 0:
            raise ZeroDivisionError("Division by zero")

        self.fraction = Fraction(m, n)

    def __add__(self, no):
        return Rational(self.fraction + no.fraction)

    def __sub__(self, no):
        return Rational(self.fraction - no.fraction)

    def __mul__(self, no):
        return Rational(self.fraction * no.fraction)

    def __truediv__(self, no):
        if no.fraction == 0:
            raise ZeroDivisionError("Division by zero")
        return Rational(self.fraction / no.fraction)

    def __eq__(self, n):
        return self.fraction == n.fraction

    def __ne__(self, n):
        return not self.__eq__(n)

    def __iadd__(self, n):
        self.fraction += n.fraction
        return self

    def __isub__(self, n):
        self.fraction -= n.fraction
        return self

    def __imul__(self, n):
        self.fraction *= n.fraction
        return self

    def __itruediv__(self, n):
        if n.fraction == 0:
            raise ZeroDivisionError("Division by zero")
        self.fraction /= n.fraction
        return self

    def __pow__(self, power):
        if power == 0:
            return Rational(1)
        return Rational(self.fraction.numerator ** power, self.fraction.denominator ** power)

    def __neg__(self):
        return Rational(-self.fraction)

    def __str__(self):
        return str(self.fraction)

    def __repr__(self):
        return f"Rational({self.fraction})"


mommy = Rational(1, 3)
print(mommy)