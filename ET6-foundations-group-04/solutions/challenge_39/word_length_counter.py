#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the lengths of words in a sentence.
created: 01/07/2025
@author: Arthur (Mr-Glucose)
"""

import string


def word_lengths(input_sentence: str) -> list[int]:
    """
    Takes a sentence and returns a list of word lengths, ignoring punctuation.

    Args:
        input_sentence (str): The input sentence.

    Returns:
        list: A list of integers representing word lengths.

    Assumptions:
        - If the input sentence is empty, the function will return an empty list.
        - Punctuation is ignored when calculating word lengths.
        - Case sensitivity does not affect word length calculation.

    Examples:
        >>> word_lengths("Hello world!")
        [5, 5]
        >>> word_lengths("Python is awesome.")
        [6, 2, 7]
        >>> word_lengths("co-op re-enter.")
        [4, 7]
        >>> word_lengths("")
        []
        >>> word_lengths("...?!")
        []
    """
    words = input_sentence.translate(str.maketrans("", "", string.punctuation)).split()
    return [len(word) for word in words]
