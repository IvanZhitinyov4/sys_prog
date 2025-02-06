import math


class Rational:
    def __init__(self, m: int | float = 0, n: int | float = 1):

        '''
        Инициализация класса
        :param m: numerator
        :param n: denoominator
        '''

        if not isinstance(m, (int, float)):
            raise ValueError("Numerator must be integer or float")
        if not isinstance(n, (int, float)):
            raise ValueError("Denominator must be integer or float")
        if n == 0:
            raise ZeroDivisionError("Division by zero")

        # Упрощаем дробь
        common_div = math.gcd(m, n)
        self.__numerator = m // common_div
        self.__denominator = n // common_div

    # Геттеры и сеттеры для числителя и знаменателя
    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @numerator.setter
    def numerator(self, value: int | float):
        if not isinstance(value, (int, float)):
            raise ValueError
        self.__numerator = value

    @denominator.setter
    def denominator(self, value: int | float):
        if not isinstance(value, (int, float)):
            raise ValueError
        if value == 0:
            raise ZeroDivisionError
        self.__denominator = value

    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.__numerator * other.__denominator + self.__denominator * other.__numerator,
                            self.__denominator * other.__denominator)
        if isinstance(other, (int, float)):
            return Rational(self.__numerator + other * self.__denominator,
                            self.__denominator)
        else:
            raise TypeError("Unknown datatype")

    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator - self.denominator * other.numerator,
                            self.denominator * other.denominator)
        elif isinstance(other, (int, float)):
            return Rational(self.numerator - other * self.denominator,
                            self.denominator)
        else:
            raise TypeError("Unknown datatype")

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.numerator, self.denominator * other.denominator)
        elif isinstance(other, (int, float)):
            return Rational(self.numerator * other, self.denominator)
        else:
            raise TypeError("Unknown datatype")

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero")
            else:
                return Rational(self.numerator / other, self.denominator)
        else:
            raise TypeError("Unknown datatype")

    def __eq__(self, other):
        if isinstance(other, Rational):
            return (self.numerator * other.denominator) == (self.denominator * other.numerator)
        elif isinstance(other, (int, float)):
            return self.numerator == (other * self.denominator)
        else:
            raise TypeError("Unknown datatype")

    def __ne__(self, other):
        return not self.__eq__(other)

    def __iadd__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator + self.denominator * other.numerator
            self.denominator = self.denominator * other.denominator
        elif isinstance(other, (int, float)):
            self.numerator = self.numerator + other * self.denominator
        else:
            raise TypeError("Unknown datatype")
        return self

    def __isub__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator - self.denominator * other.numerator
            self.denominator = self.denominator * other.denominator
        elif isinstance(other, (int, float)):
            self.numerator = self.numerator - other * self.denominator
        else:
            raise TypeError("Unknown datatype")
        return self

    def __imul__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.numerator
            self.denominator = self.denominator * other.denominator
        elif isinstance(other, (int, float)):
            self.numerator = self.numerator * other
        else:
            raise TypeError("Unknown datatype")
        return self

    def __itruediv__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator
            self.denominator = self.denominator * other.numerator
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero")
            else:
                self.numerator = self.numerator / other
        else:
            raise TypeError("Unknown datatype")
        return self

    def __pow__(self, power: int):
        if not isinstance(power, int):
            raise TypeError("Power must be an integer")
        if power < 0:
            return Rational(self.denominator ** abs(power), self.numerator ** abs(power))
        elif power > 0:
            return Rational(self.numerator ** power, self.denominator ** power)
        else:
            return Rational(1)

    def __neg__(self):
        return Rational(-self.numerator, self.denominator)

    def __str__(self):
        return str(self.numerator / self.denominator)

    def __repr__(self):
        return f"Rational({self.numerator}/{self.denominator})"
