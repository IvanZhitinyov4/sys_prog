import math
from rational_nums import Rational
from typing import Union


class Complex:
    def __init__(self, real: Union[int, float, Rational], image_buf: Union[int, float, Rational] = 0):
        """
        Инициализация комплексных чисел
        :param real: действительная часть
        :param image_buf: мнимая часть
        """
        if not isinstance(image_buf, Rational):
            image_buf = Rational(image_buf)
        self.__real = real if isinstance(real, Rational) else Rational(real)
        self.__image_part = image_buf if isinstance(image_buf, Rational) else Rational(image_buf)

    # Геттеры и сеттеры действ и мним частей
    @property
    def __real(self):
        return self.__real

    @__real.setter
    def __real(self, value):
        self.__real = value if isinstance(value, Rational) else Rational(value)

    @property
    def __image_part(self):
        return self.__image_part

    @__image_part.setter
    def __image_part(self, value):
        self.__image_part = value if isinstance(value, Rational) else Rational(value)

    def __add__(self, no):
        if isinstance(no, (int, float)):
            no = Complex(no)
        return Complex(self.__real + no.__real, self.__image_part + no.__image_part)

    def __sub__(self, no):
        if isinstance(no, (int, float)):
            no = Complex(no)
        return Complex(self.__real - no.__real, self.__image_part - no.__image_part)

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            n = Complex(n)
        __real = self.__real * n.__real - self.__image_part * n.__image_part
        __image_part = self.__real * n.__image_part + self.__image_part * n.__real
        return Complex(__real, __image_part)

    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            n = Complex(n)
        denom = n.__real * n.__real + n.__image_part * n.__image_part
        __real = (self.__real * n.__real + self.__image_part * n.__image_part) / denom
        __image_part = (self.__image_part * n.__real - self.__real * n.__image_part) / denom
        return Complex(__real, __image_part)

    def __eq__(self, n):
        if isinstance(n, (int, float)):
            n = Complex(n)
        return self.__real == n.__real and self.__image_part == n.__image_part

    def __ne__(self, n):
        if isinstance(n, (int, float)):
            n = Complex(n)
        return not self.__eq__(n)

    def __iadd__(self, n):
        if isinstance(n, (int, float)):
            n = Complex(n)
        self.__real += n.__real
        self.__image_part += n.__image_part
        return self

    def __isub__(self, n):
        if isinstance(n, (int, float)):
            n = Complex(n)
        self.__real -= n.__real
        self.__image_part -= n.__image_part
        return self

    def __imul__(self, n):
        if isinstance(n, (int, float)):
            n = Complex(n)
        __real = self.__real * n.__real - self.__image_part * n.__image_part
        __image_part = self.__real * n.__image_part + self.__image_part * n.__real
        self.__real, self.__image_part = __real, __image_part
        return self

    def __itruediv__(self, n):
        if isinstance(n, (int, float)):
            n = Complex(n)
        denom = n.__real * n.__real + n.__image_part * n.__image_part
        __real = (self.__real * n.__real + self.__image_part * n.__image_part) / denom
        __image_part = (self.__image_part * n.__real - self.__real * n.__image_part) / denom
        self.__real, self.__image_part = __real, __image_part
        return self

    def __neg__(self):
        return Complex(-self.__real, -self.__image_part)

    def __str__(self):
        """
        Представление числа в строковом виде
        :return: строковый вид ком числа
        """
        real_str = str(self.__real)
        imag_str = str(abs(self.__image_part)) + 'i' if self.__image_part != 0 else ''
        sign = ' + ' if self.__image_part > 0 else ' - ' if self.__image_part < 0 else ''
        return real_str + sign + imag_str

    def __repr__(self):
        """
        Представление ком числа как объекта
        :return: строковое предстаавление ком числа как объекта
        """
        return f"Complex({self.__real}, {self.__image_part})"

    def __pow__(self, power: int):
        if power == 0:
            return Complex(1, 0)
        else:
            magnitude = self.abs() ** power
            angle = self.arg() * power
            __real = magnitude * math.cos(angle)
            imag = magnitude * math.sin(angle)
            return Complex(__real, imag)

    def arg(self):
        """
        Нахождение аргумента - угла между положительной вещественной осью и вектором ком числа
        :return: угол между положительной вещественной осью и вектором ком числа
        """
        return math.atan2(self.__image_part.numerator / self.__image_part.denominator,
                          self.__real.numerator / self.__real.denominator)

    def abs(self):
        """
        Нахождение модуля ком числа
        :return: модуль ком числа
        """
        real_part = self.__real.numerator / self.__real.denominator
        imag_part = self.__image_part.numerator / self.__image_part.denominator
        return math.sqrt(real_part ** 2 + imag_part ** 2)



