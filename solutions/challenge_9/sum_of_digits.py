#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the sum of the digits of a positive integer.

Module contents:
    sum_of_digits: calculates the sum of the digits of a positive integer.

Created on January 3rd, 2025
@author: Semira Tesfai
"""

def sum_of_digits(n: int) -> int:
    """Calculate the sum of the digits of a positive integer.

    Parameters
    ----------
    n : int
        The positive integer whose digits will be summed.

    Returns
    -------
    int
        The sum of the digits of the given integer.

    Raises
    ------
    AssertionError
        If the argument is not a positive integer.

    Examples
    --------
    >>> sum_of_digits(123)
    6
    >>> sum_of_digits(4567)
    22
    >>> sum_of_digits(0)
    0
    """
    assert isinstance(n, int) and n >= 0, "input must be a positive integer"
    return sum(int(digit) for digit in str(n))
