"""
Unit test for the Triangular number sequence.

This module runs 6 unit tests to verify the code can successfully calculate
The nth triangle side of the triangular number sequence
This test will include
- Basic cases: Test will calculate basic positive correct inputs
- Defensive cases: Test will include: Inputs that may create an error

Created on 2025-01-06
Author: Adolfo Fumero
"""

import unittest

from solutions.triangle_challenge.main import triangle_side


class TestTriangleSide(unittest.TestCase):
    """Tests the triangle_side function"""

    def test1(self):
        """Test valid positive integer input for the 1st number"""
        self.assertEqual(triangle_side(1), 1)  # First triangular number

    def test2(self):
        """Test valid positive integer inputs for the 5th number"""
        self.assertEqual(triangle_side(5), 15)  # 1 + 2 + 3 + 4 + 5 = 15

    def test3(self):
        """Test valid positive integer inputs for the 10th number"""
        self.assertEqual(triangle_side(10), 55)  # Sum of first 10 integers

    def test4(self):
        """Test input of 0."""
        self.assertEqual(triangle_side(0), "Input must be a positive integer.")

    def test5(self):
        """Test negative integer input."""
        self.assertEqual(triangle_side(-5), "Input must be a positive integer.")

    def test6(self):
        """Test a large input value."""
        self.assertEqual(triangle_side(100), 5050)  # Sum of first 100 integers
