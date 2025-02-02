import unittest
from fractions import Fraction
from com_nums.complex_nums import Rational, Complex


class TestRational(unittest.TestCase):
    def test_addition(self):
        r1 = Rational(1, 2)
        r2 = Rational(3, 4)
        result = r1 + r2
        self.assertEqual(result.fraction, Fraction(5, 4))

    def test_subtraction(self):
        r1 = Rational(1, 2)
        r2 = Rational(3, 4)
        result = r1 - r2
        self.assertEqual(result.fraction, Fraction(-1, 4))

    def test_multiplication(self):
        r1 = Rational(1, 2)
        r2 = Rational(3, 4)
        result = r1 * r2
        self.assertEqual(result.fraction, Fraction(3, 8))

    def test_division(self):
        r1 = Rational(1, 2)
        r2 = Rational(3, 4)
        result = r1 / r2
        self.assertEqual(result.fraction, Fraction(2, 3))

    def test_equality(self):
        r1 = Rational(1, 2)
        r2 = Rational(2, 4)
        self.assertEqual(r1, r2)


class TestComplex(unittest.TestCase):
    def test_addition(self):
        c1 = Complex(Rational(1, 2), Rational(1, 3))
        c2 = Complex(Rational(1, 4), Rational(1, 5))
        result = c1 + c2
        self.assertEqual(result.real.fraction, Fraction(3, 4))
        self.assertEqual(result.imag.fraction, Fraction(8, 15))

    def test_subtraction(self):
        c1 = Complex(Rational(1, 2), Rational(1, 3))
        c2 = Complex(Rational(1, 4), Rational(1, 5))
        result = c1 - c2
        self.assertEqual(result.real.fraction, Fraction(1, 4))
        self.assertEqual(result.imag.fraction, Fraction(2, 15))

    def test_multiplication(self):
        c1 = Complex(Rational(1, 2), Rational(1, 3))
        c2 = Complex(Rational(1, 4), Rational(1, 5))
        result = c1 * c2
        self.assertEqual(result.real.fraction, Fraction(7, 120))
        self.assertEqual(result.imag.fraction, Fraction(11, 60))

    def test_division(self):
        c1 = Complex(Rational(1, 2), Rational(1, 3))
        c2 = Complex(Rational(1, 4), Rational(1, 5))
        result = c1 / c2
        self.assertEqual(result.real.fraction, Fraction(230, 123))
        self.assertEqual(result.imag.fraction, Fraction(-20, 123))

    def test_equality(self):
        c1 = Complex(Rational(1, 2), Rational(1, 3))
        c2 = Complex(Rational(1, 2), Rational(1, 3))
        self.assertEqual(c1, c2)

    def test_unary_minus(self):
        c1 = Complex(Rational(1, 2), Rational(1, 3))
        result = -c1
        self.assertEqual(result.real.fraction, Fraction(-1, 2))
        self.assertEqual(result.imag.fraction, Fraction(-1, 3))

    def test_power(self):
        c1 = Complex(Rational(1, 2), Rational(1, 3))
        result = c1.pow(2)
        self.assertEqual(result.real.fraction, Fraction(5, 36))
        self.assertEqual(result.imag.fraction, Fraction(1, 3))

    def test_arg_and_abs(self):
        c1 = Complex(Rational(1, 2), Rational(1, 3))
        self.assertAlmostEqual(c1.arg(), 0.588002603547568)
        self.assertAlmostEqual(c1.abs(), 0.6009252125773316)


if __name__ == '__main__':
    unittest.main()
