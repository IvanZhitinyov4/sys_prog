import math
from fractions import Fraction


class Rational:
    def __init__(self, numerator: int | Fraction, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Division by zero")
        self.fraction = Fraction(numerator, denominator)

    def __add__(self, n: int | Fraction):
        '''

        :param n:
        :return:
        '''
        return Rational(self.fraction + n.fraction)

    def __sub__(self, n):
        return Rational(self.fraction - n.fraction)

    def __mul__(self, n):
        return Rational(self.fraction * n.fraction)

    def __truediv__(self, n):
        if n.fraction == 0:
            raise ZeroDivisionError("Division by zero")
        return Rational(self.fraction / n.fraction)

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

    def __neg__(self):
        return Rational(-self.fraction)

    def __str__(self):
        return str(self.fraction)

    def __repr__(self):
        return f"Rational({self.fraction.numerator}, {self.fraction.denominator})"


class Complex:
    @property
    def _image_part(self):
        return self.__image_part

    def __init__(self, real: int | Rational, image_buf: int | Rational) -> None:
        self._real = real
        self._image_part = image_buf

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, real):
        self._real = real

    @property
    def image_part(self):
        return self._image_part

    @_image_part.setter
    def _image_part(self, image_buf):
        self._image_part = image_buf

    def __add__(self, n):
        return Complex(self.real + n.real, self._image_part + n._image_part)

    def __sub__(self, n):
        return Complex(self.real - n.real, self._image_part - n._image_part)

    def __mul__(self, n):
        real = self.real * n.real - self._image_part * n._image_part
        _image_part = self.real * n._image_part + self._image_part * n.real
        return Complex(real, _image_part)

    def __truediv__(self, n):
        denom = n.real * n.real + n._image_part * n._image_part
        real = (self.real * n.real + self._image_part * n._image_part) / denom
        _image_part = (self._image_part * n.real - self.real * n._image_part) / denom
        return Complex(real, _image_part)

    def __eq__(self, n):
        return self.real == n.real and self._image_part == n._image_part

    def __ne__(self, n):
        return not self.__eq__(n)

    def __iadd__(self, n):
        self.real += n.real
        self._image_part += n._image_part
        return self

    def __isub__(self, n):
        self.real -= n.real
        self._image_part -= n._image_part
        return self

    def __imul__(self, n):
        real = self.real * n.real - self._image_part * n._image_part
        _image_part = self.real * n._image_part + self._image_part * n.real
        self.real, self._image_part = real, _image_part
        return self

    def __itruediv__(self, n):
        denom = n.real * n.real + n._image_part * n._image_part
        real = (self.real * n.real + self._image_part * n._image_part) / denom
        _image_part = (self._image_part * n.real - self.real * n._image_part) / denom
        self.real, self._image_part = real, _image_part
        return self

    def __neg__(self):
        return Complex(-self.real, -self._image_part)

    def __str__(self):
        real_str = str(self._real)
        imag_str = str(abs(self._image_part)) + 'i' if self._image_part != 0 else ''
        sign = ' + ' if self._image_part > 0 else ' - ' if self._image_part < 0 else ''
        return real_str + sign + imag_str

    def __repr__(self):
        return f"Complex({self.real}, {self._image_part})"

    def pow(self, n):
        if n == 0:
            return Complex(Rational(1), 0)
        result = Complex(self.real, self._image_part)
        for _ in range(1, n):
            result *= self
        return result

    def arg(self):
        return math.atan2(self._image_part.fraction.numerator / self._image_part.fraction.denominator,
                          self.real.fraction.numerator / self.real.fraction.denominator)

    def abs(self):
        real_part = self.real.fraction.numerator / self.real.fraction.denominator
        imag_part = self._image_part.fraction.numerator / self._image_part.fraction.denominator
        return math.sqrt(real_part ** 2 + imag_part ** 2)

    def __int__(self):
        return int(self.real.fraction)

    def __float__(self):
        return float(self.real.fraction)

    def __complex__(self):
        return complex(float(self.real.fraction), float(self._image_part.fraction))

    @_image_part.setter
    def _image_part(self, value):
        self.__image_part = value


n = Complex(1, 3)
print(n)