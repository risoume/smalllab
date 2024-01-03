import unittest
import lib_path_from_tests
from smalllab.calculus import *

class TestSign(unittest.TestCase):
    # smalllab.calculus.sign

    def test_some_values(self):
        self.assertEqual(1, sign(12))
        self.assertEqual(0, sign(0.0))
        self.assertEqual(-1, sign(-1.3))


if __name__ == "__main__":
    unittest.main()