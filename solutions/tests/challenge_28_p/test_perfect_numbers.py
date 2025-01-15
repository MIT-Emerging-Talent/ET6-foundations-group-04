#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the perfect_numbers module.
Created on 06 Jan 2025
@author: Arthur (Mr-Glucose)
"""

import unittest
from solutions.challenge_28_p.perfect_numbers import (
    get_divisors,
    is_perfect_number,
    perfect_numbers_in_range,
)


class TestGetDivisors(unittest.TestCase):
    def test_returns_divisors_for_positive_integer(self):
        """Test that get_divisors returns correct divisors for a positive number."""
        self.assertEqual(get_divisors(6), [1, 2, 3])

    def test_raises_value_error_for_zero(self):
        """Test that get_divisors raises ValueError for input zero."""
        with self.assertRaises(ValueError):
            get_divisors(0)

    def test_raises_value_error_for_negative_number(self):
        """Test that get_divisors raises ValueError for a negative number."""
        with self.assertRaises(ValueError):
            get_divisors(-10)


class TestIsPerfectNumber(unittest.TestCase):
    def test_returns_true_for_perfect_number(self):
        """Test that is_perfect_number correctly identifies a perfect number."""
        self.assertTrue(is_perfect_number(28))

    def test_returns_false_for_non_perfect_number(self):
        """Test that is_perfect_number correctly identifies a non-perfect number."""
        self.assertFalse(is_perfect_number(10))

    def test_raises_value_error_for_negative_number(self):
        """Test that is_perfect_number raises ValueError for negative input."""
        with self.assertRaises(ValueError):
            is_perfect_number(-1)

    def test_raises_value_error_for_zero(self):
        """Test that is_perfect_number raises ValueError for input zero."""
        with self.assertRaises(ValueError):
            is_perfect_number(0)


class TestPerfectNumbersInRange(unittest.TestCase):
    def test_returns_perfect_numbers_in_valid_range(self):
        """Test that perfect_numbers_in_range returns all perfect numbers in a valid range."""
        self.assertEqual(perfect_numbers_in_range(1, 30), [6, 28])

    def test_returns_empty_list_when_no_perfect_numbers_in_range(self):
        """Test that perfect_numbers_in_range returns an empty list when no perfect numbers are in range."""
        self.assertEqual(perfect_numbers_in_range(1, 5), [])

    def test_raises_value_error_for_negative_start(self):
        """Test that perfect_numbers_in_range raises ValueError for a negative start."""
        with self.assertRaises(ValueError):
            perfect_numbers_in_range(-10, 100)

    def test_raises_value_error_for_zero_start_or_end(self):
        """Test that perfect_numbers_in_range raises ValueError for start or end being zero."""
        with self.assertRaises(ValueError):
            perfect_numbers_in_range(0, 100)

    def test_raises_value_error_when_start_is_greater_than_end(self):
        """Test that perfect_numbers_in_range raises ValueError when start is greater than end."""
        with self.assertRaises(ValueError):
            perfect_numbers_in_range(100, 1)


if __name__ == "__main__":
    unittest.main()
