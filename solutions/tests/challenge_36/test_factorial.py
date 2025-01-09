"""test the program factorial"""

import unittest
from solutions.challenge_36.factorial import factorial


class TestFactorial(unittest.TestCase):
    """test the program for positive numbers, negative numbers and zero"""

    def test_factorial_positive(self):
        """test the program for positive numbers"""
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(1), 1)

    def test_factorial_zero(self):
        """test the program for zero"""
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self):
        """test the program for negative numbers"""
        with self.assertRaises(ValueError):
            factorial(-1)
