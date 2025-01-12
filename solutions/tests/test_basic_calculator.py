"""
Test module for basic calculator.

Test categories:
    - Standard cases: addition, subtraction, multiplication, and division
    - Edge cases: division by zero, invalid operations
    - Defensive tests: ensure proper exceptions are raised for invalid inputs

Created on 2024-12-29
Author: Ana Isabel Murillo
"""

from solutions.basic_calculator.basic_calculator import calculate

import unittest


class TestCalculate(unittest.TestCase):
    """Test suite for the calculate function."""

    def test_addition_positive_numbers(self):
        """It should correctly add two positive numbers."""
        self.assertEqual(calculate("add", 5, 3), 8.0)

    def test_addition_negative_numbers(self):
        """It should correctly add two negative numbers."""
        self.assertEqual(calculate("add", -5, -3), -8.0)

    def test_addition_zero(self):
        """It should correctly add zero to a number."""
        self.assertEqual(calculate("add", 0, 5), 5.0)

    def test_subtraction_positive_numbers(self):
        """It should correctly subtract two positive numbers."""
        self.assertEqual(calculate("subtract", 10, 4), 6.0)

    def test_subtraction_negative_numbers(self):
        """It should correctly subtract two negative numbers."""
        self.assertEqual(calculate("subtract", -5, -5), 0.0)

    def test_subtraction_zero(self):
        """It should correctly subtract a number from zero."""
        self.assertEqual(calculate("subtract", 0, 5), -5.0)

    def test_multiplication_positive_numbers(self):
        """It should correctly multiply two positive numbers."""
        self.assertEqual(calculate("multiply", 7, 3), 21.0)

    def test_multiplication_negative_numbers(self):
        """It should correctly multiply a negative and a positive number."""
        self.assertEqual(calculate("multiply", -2, 3), -6.0)

    def test_multiplication_with_zero(self):
        """It should return zero when multiplying by zero."""
        self.assertEqual(calculate("multiply", 0, 10), 0.0)

    def test_division_positive_numbers(self):
        """It should correctly divide two positive numbers."""
        self.assertEqual(calculate("divide", 9, 3), 3.0)

    def test_division_negative_numbers(self):
        """It should correctly divide a negative and a positive number."""
        self.assertEqual(calculate("divide", -6, 3), -2.0)

    def test_division_result_with_float(self):
        """It should correctly handle division resulting in a float."""
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
