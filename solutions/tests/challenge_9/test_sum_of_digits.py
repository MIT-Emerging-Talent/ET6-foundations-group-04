#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the sum_of_digits function.
Created on January 3rd, 2025
"""

import unittest
from solutions.challenge_9.sum_of_digits import sum_of_digits


class TestSumOfDigits(unittest.TestCase):
    """Tests for the sum_of_digits function."""

    def test_positive_integer(self):
        """Ensure that the sum of digits of a positive integer is calculated correctly."""
        self.assertEqual(sum_of_digits(123), 6)

    def test_large_integer(self):
        """Ensure that the sum of digits of a large positive integer is calculated correctly."""
        self.assertEqual(sum_of_digits(4567), 22)

    def test_zero(self):
        """Ensure that the sum of digits of zero is zero."""
        self.assertEqual(sum_of_digits(0), 0)

    def test_invalid_input(self):
        """Ensure that the function raises an assertion error for invalid inputs."""
        with self.assertRaises(AssertionError):
            sum_of_digits(-5)
        with self.assertRaises(AssertionError):
            sum_of_digits(4.5)
        with self.assertRaises(AssertionError):
            sum_of_digits("123")


if __name__ == "__main__":
    unittest.main()
