import math
from rational_nums import Rational
from typing import Union


class Complex:
    def __init__(self, real: Union[int, float, Rational], image_buf: Union[int, float, Rational]) -> None:
        if not isinstance(real, Rational):
            real = Rational(real)
        if not isinstance(image_buf, Rational):
            image_buf = Rational(image_buf)
        self.__real = real
        self.__image_part = image_buf

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, real):
        self.__real = real

    @property
    def image_part(self):
        return self.__image_part

    @image_part.setter
    def image_part(self, image_buf):
        self.__image_part = image_buf

    def __add__(self, no):
        return Complex(self.real + no.real, self._image_part + no._image_part)

    def __sub__(self, no):
        return Complex(self.real - no.real, self._image_part - no._image_part)

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
        real = self.real * n.real - self._image_part * n.image_part
        _image_part = self.real * n.image_part + self._image_part * n.real
        self.real, self.image_part = real, _image_part
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
        real_str = str(self.__real)
        imag_str = str(abs(self._image_part)) + 'i' if self._image_part != 0 else ''
        sign = ' + ' if self._image_part > 0 else ' - ' if self._image_part < 0 else ''
        return real_str + sign + imag_str

    def __repr__(self):
        return f"Complex({self.real}, {self._image_part})"

    def __pow__(self, power: int):
        if power == 0:
            return Complex(1, 0)
        else:
            magnitude = self.abs() ** power
            angle = self.arg() * power
            real = magnitude * math.cos(angle)
            imag = magnitude * math.sin(angle)
            return Complex(real, imag)

    def arg(self):
        return math.atan2(self._image_part.fraction.numerator / self._image_part.fraction.denominator,
                          self.real.fraction.numerator / self.real.fraction.denominator)

    def abs(self):
        real_part = self.real.fraction.numerator / self.real.fraction.denominator
        imag_part = self.image_part.fraction.numerator / self.image_part.fraction.denominator
        return math.sqrt(real_part ** 2 + imag_part ** 2)

    def __int__(self):
        return int(self.real.fraction)

    def __float__(self):
        return float(self.real.fraction)

    def __complex__(self):
        return complex(float(self.real.fraction), float(self._image_part.fraction))


