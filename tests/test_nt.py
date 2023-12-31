import unittest
import lib_path_from_tests
from smalllab.nt import *

class TestIsSquare(unittest.TestCase):
    # smalllab.nt.is_square

    def test_negative_is_not_square(self):
        self.assertFalse(is_square(-4))

    def test_non_integer_is_not_square(self):
        self.assertFalse(is_square(2.5))
    
    def test_float_equivalent_to_square_number(self):
        self.assertTrue(is_square(9.0))
    
    def test_square_number(self):
        self.assertTrue(is_square(100))


class TestGcd(unittest.TestCase):
    # smalllab.nt.gcd

    def test_gcd_of_0_and_0_is_0(self):
        self.assertEqual(0, gcd(0, 0))

    def test_one_of_the_number_is_zero(self):
        self.assertEqual(4, gcd(4, 0))
        self.assertEqual(21, gcd(0, 21))
    
    def test_can_find_gcd_of_negatives(self):
        self.assertEqual(2, gcd(-6, -20))

    def test_some_pairs(self):
        self.assertEqual(3, gcd(6, 21))
        self.assertEqual(7, gcd(21, 49))

    def test_only_integer_arguments(self):
        with self.assertRaises(ValueError):
            gcd(2.5, 5)


class TestIsCoprime(unittest.TestCase):
    # smalllab.nt.is_coprime

    def test_coprime_pairs(self):
        self.assertTrue(is_coprime(4, 21))
        self.assertTrue(is_coprime(7, 81))
    
    def test_not_coprime_pairs(self):
        self.assertFalse(is_coprime(5, 20))
        self.assertFalse(is_coprime(9, 30))


class TestIsPrime(unittest.TestCase):
    # smalllab.nt.is_prime

    def test_prime(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        are_primes = map(is_prime, primes)
        self.assertTrue(all(are_primes))
    
    def test_non_prime(self):
        non_primes = [-10, -3, 0, 1, 4, 9, 12, 15, 20, 33, 49, 72, 105]
        are_primes = map(is_prime, non_primes)
        self.assertFalse(any(are_primes))
    
    def test_non_int_type(self):
        with self.assertRaises(TypeError):
            is_prime(9.0)


class TestSmallestPrimeFactor(unittest.TestCase):
    # smalllab.nt.smallest_prime_factor

    def test_some_valid_values(self):
        self.assertEqual(3, smallest_prime_factor(15))
        self.assertEqual(7, smallest_prime_factor(49))
    
    def test_number_must_be_greater_than_1(self):
        with self.assertRaises(ValueError):
            smallest_prime_factor(1)


class TestDecompose(unittest.TestCase):
    # smalllab.nt.decompose

    def test_some_numbers(self):
        D = {2: 2, 3: 1}
        self.assertEqual(D, decompose(12))
        D = {17: 1, 2: 1}
        self.assertEqual(D, decompose(34))
        D = {2017: 1} # prime number
        self.assertEqual(D, decompose(2017))

    def test_number_must_be_greater_than_1(self):
        with self.assertRaises(ValueError):
            decompose(1)


class TestRecompose(unittest.TestCase):
    # smalllab.nt.recompose

    def test_some_dicts(self):
        D = {2: 2, 3: 1}
        self.assertEqual(12, recompose(D))
        D = {17: 1, 2: 1}
        self.assertEqual(34, recompose(D))
        D = {2017: 1} # prime number
        self.assertEqual(2017, recompose(D))


class TestDivisorNum(unittest.TestCase):
    # smalllab.nt.divisor_num

    def test_some_values(self):
        self.assertEqual(6, divisor_num(124))
        self.assertEqual(2, divisor_num(97))
        self.assertEqual(1, divisor_num(1))

    def test_negative_value(self):
        self.assertEqual(9, divisor_num(-100))

    def test_nonzero_argument(self):
        with self.assertRaises(ValueError):
            divisor_num(0)


class TestDivisorSum(unittest.TestCase):
    # smalllab.nt.divisor_sum

    def test_some_values(self):
        self.assertEqual(31, divisor_sum(25))
        self.assertEqual(98, divisor_sum(97))
        self.assertEqual(1, divisor_sum(1))

    def test_negative_value(self):
        self.assertEqual(217, divisor_sum(-100))

    def test_nonzero_argument(self):
        with self.assertRaises(ValueError):
            divisor_sum(0)


class TestIsPerfect(unittest.TestCase):
    # smalllab.nt.is_perfect

    def test_perfect_numbers(self):
        self.assertTrue(is_perfect(6))
        self.assertTrue(is_perfect(28))
        self.assertTrue(is_perfect(496))
    
    def test_non_perfect_numbers(self):
        self.assertFalse(is_perfect(10))
        self.assertFalse(is_perfect(100))
    

class TestTotient(unittest.TestCase):
    # smalllab.nt.totient

    def test_some_values(self):
        self.assertEqual(1, totient(1))
        self.assertEqual(6, totient(9))
        self.assertEqual(2016, totient(2017))
    
    def test_only_for_positive_integer(self):
        with self.assertRaises(ValueError):
            totient(0)


class TestDecimal2Binary(unittest.TestCase):
    # smalllab.nt.decimal2binary

    def test_some_values(self):
        self.assertEqual("0", decimal2binary(0))
        self.assertEqual("10", decimal2binary(2))
        self.assertEqual("111", decimal2binary(7))
        self.assertEqual("1001010110001", decimal2binary(4785))

    def test_only_for_integer(self):
        with self.assertRaises(TypeError):
            decimal2binary(0.5)

    def test_only_for_nonnegative_integer(self):
        with self.assertRaises(ValueError):
            decimal2binary(-2)


class TestBinary2Decimal(unittest.TestCase):
    # smalllab.nt.binary2decimal

    def test_some_values(self):
        self.assertEqual(0, binary2decimal("0"))
        self.assertEqual(2, binary2decimal("10"))
        self.assertEqual(7, binary2decimal("111"))
        self.assertEqual(4785, binary2decimal("1001010110001"))
    
    def test_only_for_string(self):
        with self.assertRaises(TypeError):
            binary2decimal(1101)


class TestPowerMod(unittest.TestCase):
    # smalllab.nt.power_mod

    def test_some_values(self):
        self.assertEqual(286, power_mod(7, 327, 853))
        self.assertEqual(280196559097287, power_mod(2, 283976710803262, 283976710803263))
        self.assertEqual(1, power_mod(3, 630249099480, 630249099481))

if __name__ == "__main__":
    unittest.main()