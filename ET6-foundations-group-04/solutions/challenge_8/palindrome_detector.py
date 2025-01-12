#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if a given string or bytes is a palindrome.

Module contents:
    - is_palindrome: Determines if a string or bytes is a palindrome.

Created on 09/01/2025
Author: Semira Tesfai
"""

import re
from typing import Union


def is_palindrome(s: Union[str, bytes]) -> bool:
    """Determines if a given string or bytes is a palindrome.

    Parameters:
        s: Union[str, bytes], the input string or bytes to be checked

    Returns -> bool: True if the input is a palindrome, False otherwise

    Raises:
        TypeError: If the input is not a string or bytes

    Examples:
        >>> is_palindrome("A man, a plan, a canal, Panama")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome(b"racecar")
        True
        >>> is_palindrome(b"hello")
        False
    """
    if not isinstance(s, (str, bytes)):
        raise TypeError("Input must be a string or bytes")

    if isinstance(s, bytes):
        s = s.decode("utf-8")  # Decode bytes to string

    cleaned_s = re.sub(r"[^A-Za-z0-9]", "", s).lower()
    return cleaned_s == cleaned_s[::-1]
