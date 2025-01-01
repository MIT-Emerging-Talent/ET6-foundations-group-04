#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for binary_to_decimal function.

Test categories:
    - Standard cases: typical binary strings
    - Edge cases: single-bit binary strings, leading zeros
    - Defensive tests: invalid inputs, non-binary strings

Created on 28/12/2024
Author: Ramon Colmenares
"""

import unittest

from solutions.challenge_15.binary_to_decimal import binary_to_decimal


class TestBinaryToDecimal(unittest.TestCase):
    """Test suite for the binary_to_decimal function."""

    def test_simple_binary(self):
        """
        It should return the correct decimal
        value for typical binary strings
        """
        self.assertEqual(binary_to_decimal("1010"), 10)
        self.assertEqual(binary_to_decimal("1111"), 15)
        self.assertEqual(binary_to_decimal("1001"), 9)

    def test_single_bit_binary(self):
        """
        It should return the correct decimal
        value for single-bit binary strings
        """
        self.assertEqual(binary_to_decimal("0"), 0)
        self.assertEqual(binary_to_decimal("1"), 1)

    def test_leading_zeros(self):
        """It should correctly handle binary strings with leading zeros"""
        self.assertEqual(binary_to_decimal("0000"), 0)
        self.assertEqual(binary_to_decimal("0001"), 1)
        self.assertEqual(binary_to_decimal("001010"), 10)

    def test_invalid_binary_string(self):
        """It should raise a ValueError for invalid binary strings"""
        with self.assertRaises(ValueError):
            binary_to_decimal("2")
        with self.assertRaises(ValueError):
            binary_to_decimal("abc")
        with self.assertRaises(ValueError):
            binary_to_decimal("10.01")
