#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 01/03/2025

@Author: Clifford Exael
"""

import math


def euclidean_distance(point1, point2):
    """
    Calculates the Euclidean distance between two points point1 and point2 in an n-dimensional space.

    :param point1: List or tuple representing the coordinates of the first point.
    :param point2: List or tuple representing the coordinates of the second point.
    :return: The Euclidean distance between point1 and point2.
    """
    # Check that both points have the same dimension
    if len(point1) != len(point2):
        raise ValueError("The points must have the same dimension.")

    # Calculate the Euclidean distance
    distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))
    return distance


# Input coordinates for the first point
p1 = tuple(
    map(
        float,
        input(
            "Enter the coordinates of the first point (separated by spaces): "
        ).split(),
    )
)

# Input coordinates for the second point
p2 = tuple(
    map(
        float,
        input(
            "Enter the coordinates of the second point (separated by spaces): "
        ).split(),
    )
)

# Calculate and display the distance
dist = euclidean_distance(p1, p2)
print(f"The Euclidean distance between the two points is: {dist}")
