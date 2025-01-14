#!/usr/bin/env python3
# -*- coding: utf-8 -*--
"""
Created on 01/03/2025

 Description of the module, its purpose, and its functionality.

Feedback: It would be useful to put a docstring on the top of the module and explain its functionality.

"""

import math

# The rest of the code goes here...


"""
Created on 01/03/2025

@Author: Clifford Exael
"""


def euclidean_distance(point1, point2):
    """
    Calculates the Euclidean distance between two points point1
    and point2 in an n-dimensional space.

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
