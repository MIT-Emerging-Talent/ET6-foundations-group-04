"""Test the celsius_to_fahrenheit function from the challenge_23 module."""

import unittest
from solutions.challenge_23.celsius_to_fahrenheit import celsius_to_fahrenheit


class TestCelsiusToFahrenheit(unittest.TestCase):
    """Unit tests for the celsius_to_fahrenheit function."""

    def test_positive_temperatures(self):
        """Test the program with positive temperature list."""
        self.assertEqual(celsius_to_fahrenheit([0, 100]), [32.0, 212.0])

    def test_negative_temperatures(self):
        """Test the program with negative temperatures list."""
        self.assertEqual(celsius_to_fahrenheit([-40, -10]), [-40.0, 14.0])

    def test_mixed_temperatures(self):
        """Test the program with mixed temperatures list"""
        self.assertEqual(celsius_to_fahrenheit([-10, 0, 25]), [14.0, 32.0, 77.0])

    def test_float_temperatures(self):
        """Test the program with  float temperatures."""
        result = celsius_to_fahrenheit([0.5, -0.5])
        self.assertAlmostEqual(result[0], 32.9, places=1)
        self.assertAlmostEqual(result[1], 31.1, places=1)

    def test_invalid_input_non_list(self):
        """Test invalid input that is not a list."""
        with self.assertRaises(ValueError):
            celsius_to_fahrenheit("not a list")

    def test_invalid_input_non_numeric_elements(self):
        """Test invalid input that contains non-numeric elements."""
        with self.assertRaises(ValueError):
            celsius_to_fahrenheit([30, "a string", 45])
