#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for masking sensitive credit card numbers.

Module contents:
    - hide_credit_card: masks all but the last four digits of a credit card number.

Created on 04/01/2025
Author: Hector Colmenares
"""


def hide_credit_card(card_number: str) -> str:
    """Masks all but the last four digits of a credit card number.

    Parameters:
        card_number: str, a valid credit card number as a string

    Returns -> str with the masked credit card number, keeping only the last four digits visible

    Raises:
        ValueError: if the input is not a string
        ValueError: if the input is empty or contains non-digit characters

    >>> hide_credit_card('1234567812345678')
    '************5678'

    >>> hide_credit_card('9876543210987654')
    '************7654'

    >>> hide_credit_card('1234')
    '1234'
    """
    # Ensure the input is a valid string of digits
    if not isinstance(card_number, str):
        raise ValueError("Input must be a string.")
    if not card_number.isdigit() or len(card_number) == 0:
        raise ValueError("Input must be a non-empty string of digits.")

    # If the length is less than or equal to 4, return the card number unchanged
    if len(card_number) <= 4:
        return card_number

    # Mask all but the last four digits
    return "*" * (len(card_number) - 4) + card_number[-4:]
