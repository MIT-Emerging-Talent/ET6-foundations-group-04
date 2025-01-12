"""This unittest tests the python factorial program for positive numbers, negative numbers and zero"""

import unittest
from solutions.challenge_36.factorial import factorial


class TestFactorial(unittest.TestCase):
    """test the program for positive numbers, negative numbers and zero"""

    def test_factorial_with_positive(self):
        """test factorial of 5."""
        self.assertEqual(factorial(5), 120)

    def test_factorial_with_zero(self):
        """test factorial of 0"""
        self.assertEqual(factorial(0), 1)

    def test_factorial_with_negative(self):
        """test factorial of -1"""
        with self.assertRaises(ValueError):
            factorial(-1)
