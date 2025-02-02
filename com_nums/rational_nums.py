#from fractions import Fraction

class Rational:
    def __init__(self, m: int | None, n: int | None):
        if not isinstance(m, int):
            raise ValueError()
        if not isinstance(n, int):
            raise ValueError()
        self.__num = m
        if n == 0:
            raise ZeroDivisionError("Division by zero")
        self.__den = n

    def __add__(self, no):
        if isinstance(no, Rational):
            return Rational(self.__num * no.__den + self.__den * no.__num,
                            self.__den * no.__den)
        elif isinstance(no, int):
            return Rational(self.__num + no * self.__den,
                            self.__den)
        else:
            raise TypeError("other operand must be an integer or Rational")

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

    def __neg__(self):
        return Rational(-self.__num, self.__den)

    def __str__(self):
        return str(self.__num / self.__den)

    def __repr__(self):
        return f"Rational({self.__num}, {self.__den})"