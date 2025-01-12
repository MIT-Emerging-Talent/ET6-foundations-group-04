#!/usr/bin/env python3
# _*_coding:utf-8_*_
"""
Created on Tuesday  31 17:00:00 2024


@author:    Cliforde Exael
"""

import unittest

from solutions.challenge_26.prime_numbers import prime_numbers


class TestPrimeNumbers(unittest.TestCase):
    """
    Unit tests for the prime_numbers function, which checks if a number is a prime number.
    These tests cover typical cases, boundary cases, and defensive assertions.
    """

    def test_prime_number(self):
        """
        Test that the function correctly identifies a prime number.
        """
        number = 7
        expected = "is prime"
        actual = prime_numbers(number)
        self.assertEqual(
            actual, expected, f"Expected {expected} but got {actual} for input {number}"
        )

    def test_non_prime_number(self):
        """
        Test that the function correctly identifies a non-prime number.
        """
        number = 9
        expected = "not prime"
        actual = prime_numbers(number)
        self.assertEqual(
            actual, expected, f"Expected {expected} but got {actual} for input {number}"
        )

    def test_one_is_not_prime(self):
        """
        Test that the function correctly identifies that 1 is not a prime number.
        """
        number = 1
        expected = "not prime"
        actual = prime_numbers(number)
        self.assertEqual(
            actual, expected, f"Expected {expected} but got {actual} for input {number}"
        )

    def test_zero_is_not_prime(self):
        """
        Test that the function correctly identifies that 0 is not a prime number.
        """
        number = 0
        expected = "not prime"
        actual = prime_numbers(number)
        self.assertEqual(
            actual, expected, f"Expected {expected} but got {actual} for input {number}"
        )

    def test_negative_number_is_not_prime(self):
        """
        Test that the function correctly identifies that negative numbers are not prime.
        """
        number = -5
        expected = "not prime"
        actual = prime_numbers(number)
        self.assertEqual(
            actual, expected, f"Expected {expected} but got {actual} for input {number}"
        )

    def test_large_prime_number(self):
        """
        Test that the function correctly identifies a large prime number.
        """
        number = 29
        expected = "is prime"
        actual = prime_numbers(number)
        self.assertEqual(
            actual, expected, f"Expected {expected} but got {actual} for input {number}"
        )

    def test_large_non_prime_number(self):
        """
        Test that the function correctly identifies a large non-prime number.
        """
        number = 100
        expected = "not prime"
        actual = prime_numbers(number)
        self.assertEqual(
            actual, expected, f"Expected {expected} but got {actual} for input {number}"
        )

    def test_smallest_prime_number(self):
        """
        Test that the function correctly identifies the smallest prime number (2).
        """
        number = 2
        expected = "is prime"
        actual = prime_numbers(number)
        self.assertEqual(
            actual, expected, f"Expected {expected} but got {actual} for input {number}"
        )

    def test_defensive_type_check_string_input(self):
        """
        Test that the function raises a TypeError when given a string input.
        """
        number = "text"
        with self.assertRaises(TypeError, msg=f"Expected TypeError for input {number}"):
            prime_numbers(number)

    def test_boundary_case_next_to_prime(self):
        """
        Test that the function correctly identifies a number next to a prime number.
        """
        number = 4
        expected = "not prime"
        actual = prime_numbers(number)
        self.assertEqual(
            actual, expected, f"Expected {expected} but got {actual} for input {number}"
        )

    def test_boundary_case_very_large_number(self):
        """
        Test that the function correctly identifies a very large non-prime number.
        """
        number = 10**6
        expected = "not prime"
        actual = prime_numbers(number)
        self.assertEqual(
            actual, expected, f"Expected {expected} but got {actual} for input {number}"
        )
