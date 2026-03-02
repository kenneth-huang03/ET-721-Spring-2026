"""
Kenneth Huang
Lab 9 | Unit Testing
Feb 26th, 2026
"""
import unittest

from calculation import *

def add_two_numbers(a, b):
    return a + b

class UnitTestClass(unittest.TestCase):
    # Example 1
    def test_add_two_numbers(self):
        self.assertEqual(add_two_numbers(1, 2), 3)
        return

    # Example 2
    def test_subtract_two_numbers(self):
        self.assertEqual(subtract_two_numbers(6, 4), 2)
        self.assertEqual(subtract_two_numbers(4, 6), -2)
        self.assertEqual(subtract_two_numbers(5), 5)
        self.assertEqual(subtract_two_numbers(), 0)
        return

    def test_multiply_three_numbers(self):
        self.assertEqual(multiply_three_numbers(1, 2, 3), 6)
        self.assertEqual(multiply_three_numbers(1, -2, 3), -6)
        self.assertEqual(multiply_three_numbers(-1, -2, 3), 6)
        self.assertEqual(multiply_three_numbers(-1, -2, -3), -6)
        return

    def test_divide_two_numbers(self):
        self.assertEqual(divide_two_numbers(6, 3), 2)
        self.assertAlmostEqual(divide_two_numbers(10, 3), 3.3333, places = 4) # pyright: ignore
        return

    def test_divide_two_numbers_errors(self):
        self.assertIsNone(divide_two_numbers(1, 0))
        self.assertIsNone(divide_two_numbers(1, "a"))
        return

    def test_unexpected(self):
        with self.assertRaises(Exception):
            divide_two_numbers() # pyright: ignore
        return


if  __name__ == "__main__":
    unittest.main()
