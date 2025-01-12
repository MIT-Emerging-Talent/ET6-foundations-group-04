#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for palindrome_detector.py

Created on 09/01/2025
Author: Semira Tesfai
"""

import unittest

from solutions.challenge_8.palindrome_detector import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """
    Test cases for the is_palindrome function.
    """

    def setUp(self):
        """
        Set up any state tied to the test execution. Invoked for every test method.
        """
        self.simple_palindromes = ["racecar", "madam"]
        self.complex_palindromes = ["A Santa at NASA", "A man, a plan, a canal, Panama"]
        self.non_palindromes = ["hello", "This is not a palindrome"]
        self.bytes_palindromes = [b"racecar", b"madam"]
        self.bytes_non_palindromes = [b"hello", b"This is not a palindrome"]

    def test_simple_palindrome(self):
        """
        Test that simple palindromes are correctly identified.
        """
        for sp in self.simple_palindromes:
            with self.subTest(sp=sp):
                self.assertTrue(is_palindrome(sp))

    def test_complex_palindrome(self):
        """
        Test that complex palindromes are correctly identified.
        """
        for cp in self.complex_palindromes:
            with self.subTest(cp=cp):
                self.assertTrue(is_palindrome(cp))

    def test_non_palindrome(self):
        """
        Test that non-palindromic words and phrases are correctly identified.
        """
        for np in self.non_palindromes:
            with self.subTest(np=np):
                self.assertFalse(is_palindrome(np))

    def test_bytes_palindrome(self):
        """
        Test that palindromes with bytes input are correctly identified.
        """
        for bp in self.bytes_palindromes:
            with self.subTest(bp=bp):
                self.assertTrue(is_palindrome(bp))

    def test_bytes_non_palindrome(self):
        """
        Test that non-palindromic words and phrases with bytes input are correctly identified.
        """
        for bnp in self.bytes_non_palindromes:
            with self.subTest(bnp=bnp):
                self.assertFalse(is_palindrome(bnp))

    def test_invalid_input(self):
        """
        Test that invalid input raises the appropriate exception.
        """
        with self.assertRaises(TypeError):
            is_palindrome(12345)
        with self.assertRaises(TypeError):
            is_palindrome(None)

    def tearDown(self):
        """
        Tear down any state that was previously set up with a call to setUp().
        """
        pass
