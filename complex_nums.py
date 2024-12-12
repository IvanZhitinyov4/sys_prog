import math
from fractions import Fraction


class Rational:
    def __init__(self, numerator: int | Fraction, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.fraction = Fraction(numerator, denominator)

    def __add__(self, no):
        return Rational(self.fraction + no.fraction)

    def __sub__(self, no):
        return Rational(self.fraction - no.fraction)

    def __mul__(self, no):
        return Rational(self.fraction * no.fraction)

    def __truediv__(self, no):
        if no.fraction == 0:
            raise ValueError("Division by zero")
        return Rational(self.fraction / no.fraction)

    def __eq__(self, no):
        return self.fraction == no.fraction

    def __ne__(self, no):
        return not self.__eq__(no)

    def __iadd__(self, no):
        self.fraction += no.fraction
        return self

    def __isub__(self, no):
        self.fraction -= no.fraction
        return self

    def __imul__(self, no):
        self.fraction *= no.fraction
        return self

    def __itruediv__(self, no):
        if no.fraction == 0:
            raise ValueError("Division by zero")
        self.fraction /= no.fraction
        return self

    def __neg__(self):
        return Rational(-self.fraction)

    def __str__(self):
        return str(self.fraction)

    def __repr__(self):
        return f"Rational({self.fraction.numerator}, {self.fraction.denominator})"


class Complex:
    def __init__(self, real: int | Rational, imag: int | Rational):
        self.real = real
        self.imag = imag

    @property
    def get_real(self):
        return self.real

    @property
    def get_imag(self):
        return self.imag

    def set_real(self, real):
        self.real = real

    def set_imag(self, imag):
        self.imag = imag

    def __add__(self, no):
        return Complex(self.real + no.real, self.imag + no.imag)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imag - no.imag)

    def __mul__(self, no):
        real = self.real * no.real - self.imag * no.imag
        imag = self.real * no.imag + self.imag * no.real
        return Complex(real, imag)

    def __truediv__(self, no):
        denom = no.real * no.real + no.imag * no.imag
        real = (self.real * no.real + self.imag * no.imag) / denom
        imag = (self.imag * no.real - self.real * no.imag) / denom
        return Complex(real, imag)

    def __eq__(self, no):
        return self.real == no.real and self.imag == no.imag

    def __ne__(self, no):
        return not self.__eq__(no)

    def __iadd__(self, no):
        self.real += no.real
        self.imag += no.imag
        return self

    def __isub__(self, no):
        self.real -= no.real
        self.imag -= no.imag
        return self

    def __imul__(self, no):
        real = self.real * no.real - self.imag * no.imag
        imag = self.real * no.imag + self.imag * no.real
        self.real, self.imag = real, imag
        return self

    def __itruediv__(self, no):
        denom = no.real * no.real + no.imag * no.imag
        real = (self.real * no.real + self.imag * no.imag) / denom
        imag = (self.imag * no.real - self.real * no.imag) / denom
        self.real, self.imag = real, imag
        return self

    def __neg__(self):
        return Complex(-self.real, -self.imag)

    def __str__(self):
        real_str = str(self.real)
        imag_str = str(abs(self.imag)) + 'i' if self.imag != 0 else ''
        sign = ' + ' if self.imag > 0 else ' - ' if self.imag < 0 else ''
        return real_str + sign + imag_str

    def __repr__(self):
        return f"Complex({self.real}, {self.imag})"

    def pow(self, n):
        if n == 0:
            return Complex(Rational(1), 0)
        result = Complex(self.real, self.imag)
        for _ in range(1, n):
            result *= self
        return result

    def arg(self):
        return math.atan2(self.imag.fraction.numerator / self.imag.fraction.denominator,
                          self.real.fraction.numerator / self.real.fraction.denominator)

    def abs(self):
        real_part = self.real.fraction.numerator / self.real.fraction.denominator
        imag_part = self.imag.fraction.numerator / self.imag.fraction.denominator
        return math.sqrt(real_part ** 2 + imag_part ** 2)

    def __int__(self):
        return int(self.real.fraction)

    def __float__(self):
        return float(self.real.fraction)

    def __complex__(self):
        return complex(float(self.real.fraction), float(self.imag.fraction))
