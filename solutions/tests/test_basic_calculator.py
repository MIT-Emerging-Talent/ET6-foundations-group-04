"""
Test module for basic calculator.

Test categories:
    - Standard cases: addition, subtraction, multiplication, and division
    - Edge cases: division by zero, invalid operations
    - Defensive tests: ensure proper exceptions are raised for invalid inputs

Created on 2024-12-29
Author: Ana Isabel Murillo
"""

import unittest

from solutions.basic_calculator.main import calculate


class TestCalculate(unittest.TestCase):
    """Test suite for the calculate function."""

    def test_addition(self):
        """It should correctly add two numbers."""
        self.assertEqual(calculate("add", 5, 3), 8.0)
        self.assertEqual(calculate("add", -5, -3), -8.0)
        self.assertEqual(calculate("add", 0, 5), 5.0)

    def test_subtraction(self):
        """It should correctly subtract the second number from the first."""
        self.assertEqual(calculate("subtract", 10, 4), 6.0)
        self.assertEqual(calculate("subtract", -5, -5), 0.0)
        self.assertEqual(calculate("subtract", 0, 5), -5.0)

    def test_multiplication(self):
        """It should correctly multiply two numbers."""
        self.assertEqual(calculate("multiply", 7, 3), 21.0)
        self.assertEqual(calculate("multiply", -2, 3), -6.0)
        self.assertEqual(calculate("multiply", 0, 10), 0.0)

    def test_division(self):
        """It should correctly divide the first number by the second."""
        self.assertEqual(calculate("divide", 9, 3), 3.0)
        self.assertEqual(calculate("divide", -6, 3), -2.0)
        self.assertAlmostEqual(calculate("divide", 7, 2), 3.5)

    def test_division_by_zero(self):
        """It should raise a ValueError when attempting to divide by zero."""
        with self.assertRaises(ValueError) as context:
            calculate("divide", 5, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero.")

    def test_invalid_operation(self):
        """It should raise a ValueError for an invalid operation."""
        with self.assertRaises(ValueError) as context:
            calculate("invalid_op", 5, 3)
        self.assertIn("Invalid operation", str(context.exception))
