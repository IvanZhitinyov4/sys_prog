import unittest
import math
from rational_nums import Rational
from complex_nums import Complex


class TestRationalOperations(unittest.TestCase):
    def test_init(self):
        r = Rational(1, 2)
        self.assertEqual(r.numerator, 1)
        self.assertEqual(r.denominator, 2)

    def test_addition(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 3)
        result = r1 + r2
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 6)

    def test_subtraction(self):
        r1 = Rational(5, 6)
        r2 = Rational(1, 3)
        result = r1 - r2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 2)

    def test_multiplication(self):
        r1 = Rational(2, 3)
        r2 = Rational(3, 4)
        result = r1 * r2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 2)

    def test_division(self):
        r1 = Rational(3, 4)
        r2 = Rational(2, 3)
        result = r1 / r2
        self.assertEqual(result.numerator, 9)
        self.assertEqual(result.denominator, 8)

    def test_pow(self):
        r1 = Rational(2, 3)
        result = r1 ** 2
        self.assertEqual(result.numerator, 4)
        self.assertEqual(result.denominator, 9)

    def test_repr(self):
        r = Rational(5, 6)
        self.assertEqual(repr(r), "Rational(5/6)")

    def test_as_float(self):
        r = Rational(3, 4)
        self.assertEqual(r, 0.75)

    def test_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            Rational(1, 0)

    def test_eq(self):
        r1 = Rational(2, 3)
        r2 = Rational(2, 3)
        r3 = Rational(3, 4)
        self.assertTrue(r1 == r2)
        self.assertFalse(r1 == r3)

    def test_neq(self):
        r1 = Rational(2, 3)
        r2 = Rational(3, 4)
        self.assertTrue(r1 != r2)

    def test_neg(self):
        r1 = Rational(2, 3)
        result = -r1
        self.assertEqual(result.numerator, -2)
        self.assertEqual(result.denominator, 3)


class TestComplexOperations(unittest.TestCase):
    def test_init(self):
        c = Complex(1, 2)
        self.assertEqual(c.__real, 1)
        self.assertEqual(c.__image_part, 2)

        c = Complex(Rational(1, 2), Rational(3, 4))
        self.assertEqual(c.__real, Rational(1, 2))
        self.assertEqual(c.__image_part, Rational(3, 4))

    def test_addition(self):
        z1 = Complex(3, 2)
        z2 = Complex(1, 7)
        result = z1 + z2
        self.assertEqual(result, Complex(4, 9))

    def test_addition_with_int(self):
        z1 = Complex(3, 2)
        result = z1 + 5
        self.assertEqual(result, Complex(8, 2))

    def test_subtraction(self):
        z1 = Complex(5, 3)
        z2 = Complex(2, 1)
        result = z1 - z2
        self.assertEqual(result, Complex(3, 2))

    def test_multiplication(self):
        z1 = Complex(1, 2)
        z2 = Complex(3, 4)
        result = z1 * z2
        self.assertEqual(result, Complex(-5, 10))

    def test_division(self):
        z1 = Complex(3, 2)
        z2 = Complex(1, 7)
        result = z1 / z2
        self.assertEqual(result, Complex(Rational(17, 50), Rational(-19, 50)))

    def test_abs(self):
        z1 = Complex(3, 4)
        self.assertEqual(z1.abs(), Rational(5))

    def test_arg(self):
        z1 = Complex(1, 1)
        self.assertEqual(z1.arg(), Rational(math.pi / 4))

    def test_power(self):
        z1 = Complex(1, 0)
        result = z1 ** 2
        self.assertEqual(result, Complex(1, 0))

    def test_equality(self):
        z1 = Complex(3, 2)
        z2 = Complex(3, 2)
        self.assertTrue(z1 == z2)

    def test_inequality(self):
        z1 = Complex(1, 2)
        z2 = Complex(3, 4)
        self.assertTrue(z1 != z2)


if __name__ == '__main__':
    unittest.main()
