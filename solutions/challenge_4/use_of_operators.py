#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for processing a list of elements based on a threshold.

Module contents:
    - process_elements: Analyzes a list to count approved, rejected,
    and string elements.

Created on 29/12/2024
Author: Ramon Colmenares
"""


def process_elements(elements_list: list, threshold: float) -> dict:
    """Processes a list of elements to count approvals, rejections,
    and strings.

    Parameters:
        elements_list: list, the list of elements to process
        threshold: float, the value below which numbers are "approved"

    Returns -> dict: A dictionary with counts of approved, rejected,
    and string elements.

    Raises:
        TypeError: if elements_list is not a list or threshold is not a number
        TypeError: if elements_list contains elements not of type int,
        float, or str

    Examples:
        >>> process_elements([10, -5, "Python", -20], -10)
        {'approved': 1, 'rejected': 2, 'strings': 1}

        >>> process_elements([10, "lol", -15.5, 0, ":p"], 0)
        {'approved': 1, 'rejected': 2, 'strings': 2}

        >>> process_elements([":O", 100.5, -50, "Test"], -5)
        {'approved': 1, 'rejected': 1, 'strings': 2}
    """
    if not isinstance(elements_list, list):
        raise TypeError("elements_list must be a list.")
    if not isinstance(threshold, (int, float)):
        raise TypeError("threshold must be an int or float.")

    approved = 0
    rejected = 0
    string_count = 0

    for element in elements_list:
        if isinstance(element, (int, float)):
            if element < threshold:
                approved += 1
            else:
                rejected += 1
        elif isinstance(element, str):
            string_count += 1
        else:
            raise TypeError(
                f"Invalid element type: {type(element)}. "
                f"Only int, float, and str are allowed."
            )

    approved_dict = {"approved": approved}
    rejected_dict = {"rejected": rejected}
    strings_dict = {"strings": string_count}

    result = {**approved_dict, **rejected_dict, **strings_dict}

    return result
