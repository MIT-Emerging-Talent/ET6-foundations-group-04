#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for process_elements function.

Created on 29/12/2024
Author: Ramon Colmenares
"""

import unittest

from solutions.challenge_4.use_of_operators import process_elements


class TestProcessElements(unittest.TestCase):
    """Test suite for the process_elements function."""

    def test_valid_input(self):
        """Test with a valid list of mixed elements."""
        elements_list = [10, -5, "Python", -20]
        threshold = -10
        result = process_elements(elements_list, threshold)
        self.assertEqual(result, {"approved": 1, "rejected": 2, "strings": 1})

    def test_all_numbers(self):
        """Test with a list of only numbers."""
        elements_list = [10, -5, -20, 15, 3]
        threshold = 0
        result = process_elements(elements_list, threshold)
        self.assertEqual(result, {"approved": 2, "rejected": 3, "strings": 0})

    def test_all_strings(self):
        """Test with a list of only strings."""
        elements_list = ["Python", "GPT-3", "AI"]
        threshold = 0
        result = process_elements(elements_list, threshold)
        self.assertEqual(result, {"approved": 0, "rejected": 0, "strings": 3})

    def test_mixed_with_threshold(self):
        """Test with a mix of numbers and strings and a custom threshold."""
        elements_list = [10, 3.14, -5, "Test", 0]
        threshold = 1
        result = process_elements(elements_list, threshold)
        self.assertEqual(result, {"approved": 2, "rejected": 2, "strings": 1})

    def test_invalid_elements_list(self):
        """Test with an invalid elements_list type."""
        with self.assertRaises(TypeError):
            process_elements("not a list", -10)

    def test_invalid_threshold(self):
        """Test with an invalid threshold type."""
        elements_list = [10, -5, "Python", -20]
        with self.assertRaises(TypeError):
            process_elements(elements_list, "not a number")

    def test_invalid_element_in_list(self):
        """Test with an invalid element in the list."""
        elements_list = [10, -5, ["not valid"], -20]
        with self.assertRaises(TypeError):
            process_elements(elements_list, -10)
