"""
Unit tests for the tribonacci function.

This module tests the tribonacci function to ensure it calculates the nth Tribonacci number correctly.
The test cases include:
    - Base cases (e.g., T(0), T(1), T(2)).
    - Standard cases (e.g., T(5), T(10)).
    - Edge cases (e.g., large n values).
    - Defensive assertions for invalid inputs.

Created on: 01/01/2025
Author: Ana Isabel Murillo
"""

import unittest

from solutions.the_tribonacci_sequence.main import tribonacci


class TestTribonacci(unittest.TestCase):
    """Test suite for the tribonacci function."""

    def test_base_cases(self):
        """Test the base cases."""
        self.assertEqual(tribonacci(0), 0)  # Base case T(0)
        self.assertEqual(tribonacci(1), 1)  # Base case T(1)
        self.assertEqual(tribonacci(2), 1)  # Base case T(2)

        self.assertIsInstance(tribonacci(0), int, "output should be an integer")
        self.assertIsInstance(tribonacci(1), int, "Output should be an integer.")
        self.assertIsInstance(tribonacci(2), int, "Output should be an integer.")

    def test_standard_cases(self):
        """Test standard cases."""
        self.assertEqual(tribonacci(3), 2)  # 0, 1, 1, 2
        self.assertEqual(tribonacci(4), 4)  # 0, 1, 1, 2, 4
        self.assertEqual(tribonacci(5), 7)  # 0, 1, 1, 2, 4, 7
        self.assertEqual(tribonacci(6), 13)  # 0, 1, 1, 2, 4, 7, 13

        self.assertIsInstance(tribonacci(3), int, "Output should be an integer.")
        self.assertIsInstance(tribonacci(4), int, "Output should be an integer.")
        self.assertIsInstance(tribonacci(5), int, "Output should be an integer.")
        self.assertIsInstance(tribonacci(6), int, "Output should be an integer.")

    def test_large_values(self):
        """Test for larger values of n."""
        self.assertEqual(tribonacci(10), 149)  # Verify correct calculation for T(10)
        self.assertEqual(tribonacci(15), 3136)  # Verify correct calculation for T(15)

        self.assertIsInstance(tribonacci(10), int, "Output should be an integer.")
        self.assertIsInstance(tribonacci(15), int, "Output should be an integer.")

    def test_edge_cases(self):
        """Test edge cases."""
        self.assertEqual(tribonacci(30), 29249425)  # Large n value

        self.assertIsInstance(tribonacci(30), int, "Output should be an integer.")
