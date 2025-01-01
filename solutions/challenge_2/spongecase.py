#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting strings into SpongeCase (alternating lower and upper case).

Module contents:
    - spongecase: Converts a string into SpongeCase

Created on 28/12/2024
Author: Chrismy Leprince Paul Augustin
"""


def spongecase(text: str) -> str:
    """Converts a string into SpongeCase, where letters alternate between lower
    and upper case, starting with lower case.

    Parameters:
        text: str, a string to be converted into SpongeCase

    Returns -> str: The SpongeCase version of the input string

    Examples:
        >>> spongecase("hello world")
        'hElLo wOrLd'
        >>> spongecase("PYTHON")
        'pYtHoN'
        >>> spongecase("HELLO!")
        'hElLo!'
    """
    result_chars = []
    for index, char in enumerate(text):
        if index % 2 == 0:
            # Even index -> lowercase
            result_chars.append(char.lower())
        else:
            # Odd index -> uppercase
            result_chars.append(char.upper())
    return "".join(result_chars)
