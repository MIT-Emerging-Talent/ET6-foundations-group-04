#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from solutions.challenge_28.is_perfect_number import (
    find_perfect_numbers,
    is_perfect_number,
)


class TestPerfectNumber(unittest.TestCase):
    """Unit tests for perfect number functions."""

    def test_is_perfect_number(self):
        """
        Test cases for the is_perfect_number function.

        Positive cases:
        - Ensure that perfect numbers are correctly identified:
          6, 28, 496, 8128.

        Negative cases:
        - Ensure that non-perfect numbers are correctly identified:
          1, 12, 15, 1000.
        """
        # Positive cases
        self.assertTrue(
            is_perfect_number(6),
            f"Failed: expected True for 6, got {is_perfect_number(6)}",
        )
        self.assertTrue(
            is_perfect_number(28),
            f"Failed: expected True for 28, got {is_perfect_number(28)}",
        )
        self.assertTrue(
            is_perfect_number(496),
            f"Failed: expected True for 496, got {is_perfect_number(496)}",
        )
        self.assertTrue(
            is_perfect_number(8128),
            f"Failed: expected True for 8128, got {is_perfect_number(8128)}",
        )
        # Negative cases
        self.assertFalse(
            is_perfect_number(1),
            f"Failed: expected False for 1, got {is_perfect_number(1)}",
        )
        self.assertFalse(
            is_perfect_number(12),
            f"Failed: expected False for 12, got {is_perfect_number(12)}",
        )
        self.assertFalse(
            is_perfect_number(15),
            f"Failed: expected False for 15, got {is_perfect_number(15)}",
        )
        self.assertFalse(
            is_perfect_number(1000),
            f"Failed: expected False for 1000, got {is_perfect_number(1000)}",
        )

    def test_find_perfect_numbers(self):
        """
        Test cases for the find_perfect_numbers function.

        Cases:
        - Multiple numbers, including perfect and non-perfect ones.
        - Empty set.
        - No perfect numbers.
        - Single perfect number.
        """
        # Case with multiple numbers, including perfect and non-perfect ones
        input_set = {6, 28, 496, 8128, 12, 15, 1000}
        expected_output = {6, 28, 496, 8128}
        actual_output = find_perfect_numbers(input_set)
        self.assertEqual(
            actual_output,
            expected_output,
            f"Failed: expected {expected_output}, got {actual_output} for input {input_set}",
        )
        # Case with an empty set
        input_set = set()
        expected_output = set()
        actual_output = find_perfect_numbers(input_set)
        self.assertEqual(
            actual_output,
            expected_output,
            f"Failed: expected {expected_output}, got {actual_output} for input {input_set}",
        )
        # Case with no perfect numbers
        input_set = {10, 11, 12, 13, 14}
        expected_output = set()
        actual_output = find_perfect_numbers(input_set)
        self.assertEqual(
            actual_output,
            expected_output,
            f"Failed: expected {expected_output}, got {actual_output} for input {input_set}",
        )
        # Case with a single perfect number
        input_set = {28}
        expected_output = {28}
        actual_output = find_perfect_numbers(input_set)
        self.assertEqual(
            actual_output,
            expected_output,
            f"Failed: expected {expected_output}, got {actual_output} for input {input_set}",
        )
