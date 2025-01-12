#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for the FizzBuzz module.

This file contains unit tests for the fizzbuzz function.

Created on 06/01/2025
Author: Hector Colmenares
"""

import unittest

from solutions.challenge_12.fizzbuzz_program import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    """Unit tests for the fizzbuzz function."""

    def test_returns_first_value_as_1_for_n_5(self):
        """Test if the first value is '1' when n=5."""
        self.assertEqual(fizzbuzz(5)[0], "1")

    def test_returns_second_value_as_2_for_n_5(self):
        """Test if the second value is '2' when n=5."""
        self.assertEqual(fizzbuzz(5)[1], "2")

    def test_returns_third_value_as_fizz_for_n_5(self):
        """Test if the third value is 'Fizz' when n=5."""
        self.assertEqual(fizzbuzz(5)[2], "Fizz")

    def test_returns_fourth_value_as_4_for_n_5(self):
        """Test if the fourth value is '4' when n=5."""
        self.assertEqual(fizzbuzz(5)[3], "4")

    def test_returns_fifth_value_as_buzz_for_n_5(self):
        """Test if the fifth value is 'Buzz' when n=5."""
        self.assertEqual(fizzbuzz(5)[4], "Buzz")

    def test_returns_third_value_as_fizz_for_n_3(self):
        """Test if the third value is 'Fizz' when n=3."""
        self.assertEqual(fizzbuzz(3)[2], "Fizz")

    def test_returns_last_value_as_buzz_for_n_10(self):
        """Test if the last value is 'Buzz' when n=10."""
        self.assertEqual(fizzbuzz(10)[-1], "Buzz")

    def test_returns_last_value_as_fizzbuzz_for_n_15(self):
        """Test if the last value is 'FizzBuzz' when n=15."""
        self.assertEqual(fizzbuzz(15)[-1], "FizzBuzz")

    def test_raises_assertion_error_for_input_zero(self):
        """Test if fizzbuzz raises AssertionError for input 0."""
        with self.assertRaises(AssertionError):
            fizzbuzz(0)

    def test_raises_assertion_error_for_negative_input(self):
        """Test if fizzbuzz raises AssertionError for negative input."""
        with self.assertRaises(AssertionError):
            fizzbuzz(-5)

    def test_raises_assertion_errors_for_non_integer_input(self):
        """Test if fizzbuzz raises AssertionError for non-integer input."""
        with self.assertRaises(AssertionError):
            fizzbuzz("a")

    def test_returns_1_for_boundary_case_n_1(self):
        """Test if fizzbuzz returns ['1'] for the smallest valid input n=1."""
        self.assertEqual(fizzbuzz(1), ["1"])
