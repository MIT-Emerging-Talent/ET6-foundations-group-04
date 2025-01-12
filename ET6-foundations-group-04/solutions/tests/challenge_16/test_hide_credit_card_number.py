#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the hide_credit_card function.

Class:
    TestHideCreditCard: Contains tests for various cases.

Created on 04/01/2025
Author: Hector Colmenares
"""

import unittest

from solutions.challenge_16.hide_credit_card_number import hide_credit_card


class TestHideCreditCard(unittest.TestCase):
    """Tests for the hide_credit_card function."""

    def test_regular_number(self):
        """Test with a regular 16-digit credit card number."""
        self.assertEqual(hide_credit_card("1234567812345678"), "************5678")

    def test_short_number(self):
        """Test with a short credit card number."""
        self.assertEqual(hide_credit_card("12345"), "*2345")

    def test_exactly_four_digits(self):
        """Test with a credit card number of exactly four digits."""
        self.assertEqual(hide_credit_card("1234"), "1234")

    def test_non_digit_characters_raises_value_error(self):
        """Test with a credit card number containing non-digit characters."""
        with self.assertRaises(ValueError):
            hide_credit_card("1234abcd5678")

    def test_empty_string_raises_value_error(self):
        """Test with an empty string."""
        with self.assertRaises(ValueError):
            hide_credit_card("")

    def test_non_string_input_raises_value_error(self):
        """Test with non-string input."""
        with self.assertRaises(ValueError):
            hide_credit_card(12345678)
