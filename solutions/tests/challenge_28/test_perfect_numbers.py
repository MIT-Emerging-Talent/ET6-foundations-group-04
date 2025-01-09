#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for identifying perfect numbers in a given range
Created on 06 Jan 2025
@author: Arthur (Mr-Glucose)
"""

import unittest

from solutions.challenge_28.perfect_numbers import (  # type: ignore
    get_divisors,
    is_perfect_number,
    perfect_numbers_in_range,
)


class TestPerfectNumbers(unittest.TestCase):
    """
    Test suite for the Perfect Numbers module.
    This class tests the functionality of the functions:
    get_divisors, is_perfect_number, and perfect_numbers_in_range.
    """

    def test_get_divisors_valid_input(self):
        """
        Tests the get_divisors function with valid input.
        Checks that the divisors of a number are correctly returned.
        """
        self.assertEqual(get_divisors(6), [1, 2, 3])
        self.assertEqual(get_divisors(28), [1, 2, 4, 7, 14])

    def test_is_perfect_number(self):
        """
        Tests the is_perfect_number function.
        Checks whether a number is a perfect number.
        """
        self.assertTrue(is_perfect_number(6))
        self.assertTrue(is_perfect_number(28))
        self.assertFalse(is_perfect_number(12))

    def test_perfect_numbers_in_range(self):
        """
        Tests the perfect_numbers_in_range function.
        Checks whether the function returns perfect numbers in a given range.
        """
        self.assertEqual(perfect_numbers_in_range(1, 100), [6, 28])
        self.assertEqual(perfect_numbers_in_range(1, 1000), [6, 28, 496])
