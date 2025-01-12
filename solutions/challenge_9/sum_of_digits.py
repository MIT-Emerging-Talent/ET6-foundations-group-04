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
    ValueError
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
<<<<<<< HEAD
    if not isinstance(n, int) or n < 0:
        raise ValueError("input must be a positive integer")

=======
    if not isinstance(n, int) or n < 0: 
        raise ValueError("input must be a positive integer") 
        
>>>>>>> fa9d0449dd92ca71f314a224b392f8f360892773
    return sum(int(digit) for digit in str(n))
