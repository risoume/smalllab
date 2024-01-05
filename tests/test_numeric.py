import unittest
import lib_path_from_tests
from smalllab.numeric import *

class TestBisect(unittest.TestCase):
    # smalllab.numeric.bisect
    # these tests only for exceptions
    # todo: use scipy to test the result

    def test_only_positive_tolerance(self):
        with self.assertRaises(ValueError):
            bisect(lambda x: x, 1, 2, 0)
    
    def test_must_be_different_sign(self):
        with self.assertRaises(ValueError):
            bisect(lambda x: x, 1, 2, 0.01)
    
    def test_a0_less_than_b0(self):
        with self.assertRaises(ValueError):
            bisect(lambda x: x, 2, 1, 0.01)


class TestNewton(unittest.TestCase):
    # smalllab.numeric.newton
    # todo: use scipy to test the result
    
    def test_max_iteration_exceeded(self):
        f = lambda x: x**6 - x - 1
        df = lambda x: 6 * x**5 - 1
        self.assertEqual(None, newton(f, df, 1.5, 1e-8, 3))
    
    def test_derivative_is_not_zero(self):
        with self.assertRaises(ValueError):
            f = lambda x: x**3 - 1
            df = lambda x: 3 * x**2
            newton(f, df, 0, 0.001, 3)


class TestSecant(unittest.TestCase):
    # smalllab.numeric.secant
    # todo: - use scipy to test the result
    #       - find example where f(x0)==f(x1)

    def test_max_iteration_exceeded(self):
        f = lambda x: x**6 - x - 1
        self.assertEqual(None, secant(f, 2, 1, 1e-8, 5))


class TestLagrange(unittest.TestCase):
    # smalllab.numeric.lagrange

    def test_length_greater_than_1(self):
        with self.assertRaises(ValueError):
            X = [0.82]
            Y = [2.2705]
            xp = 0.826
            lagrange(X, Y, xp)

    def test_same_length(self):
        with self.assertRaises(ValueError):
            X = [0.82, 0.83, 0.84, 0.85]
            Y = [2.2705, 2.293319, 2.316367]
            xp = 0.826
            lagrange(X, Y, xp)
    
    def test_X_entries_must_be_distinct(self):
        with self.assertRaises(ValueError):
            X = [0.82, 0.83, 0.83]
            Y = [2.2705, 2.293319, 2.316367]
            xp = 0.826
            lagrange(X, Y, xp)
        

if __name__ == "__main__":
    unittest.main()