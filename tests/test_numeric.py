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


if __name__ == "__main__":
    unittest.main()