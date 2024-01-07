import unittest
import lib_path_from_tests
from smalllab.calculus import *

class TestSign(unittest.TestCase):
    # smalllab.calculus.sign

    def test_some_values(self):
        self.assertEqual(1, sign(12))
        self.assertEqual(0, sign(0.0))
        self.assertEqual(-1, sign(-1.3))


class TestList2Poly(unittest.TestCase):
    # smalllab.calculus.list2poly
    
    def test_some_values(self):
        f1 = lambda x: -3*x**3 - 2*x + 17
        L = [-3, 0, -2, 17]
        f2 = list2poly(L)
        for x in range(5):
            self.assertEqual(f1(x), f2(x))

    def test_cannot_be_empty(self):
        with self.assertRaises(ValueError):
            list2poly([])


class TestFormatPoly(unittest.TestCase):
    # smalllab.calculus.format_poly
    
    def test_dont_display_0(self):
        self.assertEqual('', format_poly(3, 0))
        self.assertEqual('', format_poly(3, 0, True))
    
    def test_display_0_for_zero_polynomial(self):
        self.assertEqual('0', format_poly(0, 0, True))

    def test_degree_zero(self):
        self.assertEqual('', format_poly(0, 0))
        self.assertEqual('0', format_poly(0, 0, True))
        self.assertEqual('+2', format_poly(0, 2))
        self.assertEqual('2', format_poly(0, 2, True))
        self.assertEqual('-2', format_poly(0, -2))
    
    def test_degree_1(self):
        self.assertEqual('', format_poly(1, 0))
        self.assertEqual('+2x', format_poly(1, 2))
        self.assertEqual('2x', format_poly(1, 2, True))
        self.assertEqual('-2x', format_poly(1, -2))
    
    def test_higher_degree(self):
        self.assertEqual('', format_poly(2, 0))
        self.assertEqual('+2x^2', format_poly(2, 2))
        self.assertEqual('2x^2', format_poly(2, 2, True))
        self.assertEqual('-2x^2', format_poly(2, -2))
    
    def test_degree_must_be_nonnegative(self):
        with self.assertRaises(ValueError):
            format_poly(-1, 3)


class TestList2PolyStr(unittest.TestCase):
    # smalllab.calculus.list2polystr

    def test_degree_less_than_1(self):
        self.assertEqual('', list2polystr([]))
        self.assertEqual('0', list2polystr([0]))
        self.assertEqual('-1.3', list2polystr([-1.3]))
    
    def test_degree_1(self):
        self.assertEqual('1x+1', list2polystr([1, 1]))
        self.assertEqual('-2x-2', list2polystr([-2, -2]))
        self.assertEqual('2x', list2polystr([2, 0]))
    
    def test_higher_degree(self):
        self.assertEqual('3x^2-2x+1', list2polystr([3, -2, 1]))
        self.assertEqual('-3x^6+2x^3-1x^2', list2polystr([-3, 0, 0, 2, -1, 0, 0]))


if __name__ == "__main__":
    unittest.main()