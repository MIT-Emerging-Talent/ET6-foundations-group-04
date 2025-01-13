#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test suite for the Euclidean distance function.
This module contains unit tests for verifying the correctness of the
euclidean_distance function across different cases.
"""

import unittest

from solutions.challenge_34.euclidean_distance import euclidean_distance


class TestEuclideanDistance(unittest.TestCase):
    """
    Unit tests for the `euclidean_distance` function.
    This class includes test cases for 2D, 3D, and error scenarios like
    different dimensions and negative coordinates.
    """

    def test_same_point(self):
        """
        Test case where both points are the same.
        The Euclidean distance between the same points should be 0.
        """
        p1 = (1, 2, 3)
        p2 = (1, 2, 3)
        actual = euclidean_distance(p1, p2)
        expected = 0
        self.assertEqual(actual, expected)

    def test_two_dimensional_points(self):
        """Test case with 2D points."""
        p1 = (1, 2)
        p2 = (4, 6)
        actual = euclidean_distance(p1, p2)
        expected = 5.0
        self.assertEqual(actual, expected)

    def test_three_dimensional_points(self):
        """Test case with 3D points."""
        p1 = (1, 2, 3)
        p2 = (4, 5, 6)
        actual = euclidean_distance(p1, p2)
        expected = 5.196152422706632
        self.assertEqual(actual, expected)

    def test_different_dimensions(self):
        """Test case where points have different dimensions."""
        p1 = (1, 2)
        p2 = (4, 5, 6)
        with self.assertRaises(ValueError):
            euclidean_distance(p1, p2)

    def test_negative_coordinates(self):
        """Test case with negative coordinates."""
        p1 = (-1, -2, -3)
        p2 = (1, 2, 3)
        actual = euclidean_distance(p1, p2)
        expected = 7.483314773547883
        self.assertEqual(actual, expected)
