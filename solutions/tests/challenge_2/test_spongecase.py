#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for spongecase function.

Test categories:
    - Basic cases: typical strings, single words
    - Edge cases: empty string, all uppercase, all lowercase
    - Special characters: punctuation, digits, symbols

Created on 2024-12-28
Author: Chrismy Leprince Paul Augustin
"""

import unittest

from solutions.challenge_2.spongecase import spongecase


class TestSpongeCase(unittest.TestCase):
    """Test suite for the spongecase function."""

    def test_spongecase_basic(self):
        """
        It should convert a typical string containing spaces into SpongeCase.

        Example:
            "hello world" -> "hElLo wOrLd"
        """
        self.assertEqual(spongecase("hello world"), "hElLo wOrLd")

    def test_spongecase_single_word(self):
        """
        It should convert a single word into SpongeCase.

        Example:
            "Python" -> "pYtHoN"
        """
        self.assertEqual(spongecase("Python"), "pYtHoN")

    def test_spongecase_empty_string(self):
        """
        It should handle an empty string by returning an empty string.

        Example:
            "" -> ""
        """
        self.assertEqual(spongecase(""), "")

    def test_spongecase_all_caps(self):
        """
        It should convert an all-caps string into SpongeCase.

        Example:
            "HELLO" -> "hElLo"
        """
        self.assertEqual(spongecase("HELLO"), "hElLo")

    def test_spongecase_all_lowercase(self):
        """
        It should convert an all-lowercase string into SpongeCase.

        Example:
            "world" -> "wOrLd"
        """
        self.assertEqual(spongecase("world"), "wOrLd")

    def test_spongecase_special_characters(self):
        """
        It should alternate case while preserving special characters
        and digits in place.

        Mapping indices:
            Index:  0 1 2 3 4  5 6   7   8  9
            Char:   H e l l o  ? 1   #   A  b
            Case:   h E l L o  ? 1   #   a  B
            Result: "hElLo?1#aB"
        """
        self.assertEqual(spongecase("Hello?1#Ab"), "hElLo?1#aB")
