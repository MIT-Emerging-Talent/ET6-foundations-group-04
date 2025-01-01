#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting binary numbers to decimal equivalents.

Module contents:
    - binary_to_decimal: Converts a binary string to its decimal equivalent

Created on 28/12/2024
Author: Ramon Colmenares
"""


def binary_to_decimal(binary_str: str) -> int:
    """Converts a binary string to its decimal equivalent.

    Parameters:
        binary_str: str, a binary number as a string

    Returns -> int: the decimal equivalent of the binary number

    Raises:
        ValueError: if the input is not a valid binary string

    Examples:
        >>> binary_to_decimal('1010')
        10
        >>> binary_to_decimal('1111')
        15
        >>> binary_to_decimal('1001')
        9
    """
    decimal_value = 0
    for i, digit in enumerate(reversed(binary_str)):
        if digit not in {"0", "1"}:
            raise ValueError(f"Invalid binary digit '{digit}' in input")
        decimal_value += int(digit) * (2**i)
    return decimal_value
