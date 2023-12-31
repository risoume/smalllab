import unittest
import lib_path_from_tests
from smalllab.algebra import *

class TestUnits(unittest.TestCase):
    # smalllab.algebra.units

    def test_some_values(self):
        self.assertEqual([1, 3, 5, 7], units(8))
        self.assertEqual([1, 2, 4, 7, 8, 11, 13, 14], units(15))
        self.assertEqual(list(range(1, 11)), units(11))
    
    def test_must_be_greater_than_1(self):
        with self.assertRaises(ValueError):
            units(1)    


if __name__ == "__main__":
    unittest.main()