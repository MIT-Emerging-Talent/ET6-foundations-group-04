#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for find_heaviest_coin function.

Test categories:
    - Basic cases: test the function with specific coin arrangements
    - Edge cases: test cases such as heavy coin in the last group
    - Random cases: test cases with varied arrangements

Created on 2024-12-28
Author: Chrismy Leprince Paul Augustin
"""

import unittest
from solutions.challenge_5.find_the_heaviest_coin import find_heaviest_coin


class TestFindHeaviestCoin(unittest.TestCase):
    """Unit tests for the find_heaviest_coin function."""

    def test_heaviest_in_first_group(self):
        """Test when the heaviest coin is in the first group."""
        coins = [1, 1, 5, 1, 1, 1, 1, 1]
        self.assertEqual(find_heaviest_coin(coins), 3)

    def test_heaviest_in_second_group(self):
        """Test when the heaviest coin is in the second group."""
        coins = [1, 1, 1, 6, 1, 1, 1, 1]
        self.assertEqual(find_heaviest_coin(coins), 4)

    def test_heaviest_in_third_group(self):
        """Test when the heaviest coin is in the third group."""
        coins = [1, 1, 1, 1, 1, 1, 7, 1]
        self.assertEqual(find_heaviest_coin(coins), 7)

    def test_heaviest_is_last_coin(self):
        """Test when the heaviest coin is the last coin."""
        coins = [1, 1, 1, 1, 1, 1, 1, 8]
        self.assertEqual(find_heaviest_coin(coins), 8)

    def test_all_equal_except_one(self):
        """Test when all coins are equal except one."""
        coins = [2, 2, 2, 2, 2, 3, 2, 2]
        self.assertEqual(find_heaviest_coin(coins), 6)
