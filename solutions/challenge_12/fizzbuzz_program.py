#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for solving the FizzBuzz challenge.

Module contents:
    - fizzbuzz: Generates the FizzBuzz sequence for numbers from 1 to n.

Created on 06/01/2025
Author: Hector Colmenares
"""


def fizzbuzz(n: int) -> list[str]:
    """Generates the FizzBuzz sequence from 1 to n.

    Parameters:
        n (int): The upper limit of the sequence (must be a positive integer).
                 The range includes the limit n.

    Returns:
        list[str]: A list of strings where:
            - "Fizz" replaces multiples of 3,
            - "Buzz" replaces multiples of 5,
            - "FizzBuzz" replaces multiples of both,
            - Otherwise, the number itself as a string.

    Raises:
        ValueError: If n is not a positive integer.

    Examples:
        >>> fizzbuzz(3)
        ['1', '2', 'Fizz']

        >>> fizzbuzz(5)
        ['1', '2', 'Fizz', '4', 'Buzz']

        >>> fizzbuzz(15)[-1]
        'FizzBuzz'
    """
    assert isinstance(n, int), "n must be an integer"
    assert n > 0, "n must be a positive integer"

    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
