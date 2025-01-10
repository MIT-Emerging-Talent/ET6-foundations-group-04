#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for identifying perfect numbers in a given range
Created on 06 Jan 2025
@author: Arthur (Mr-Glucose)

"""


def get_divisors(n):
    """Checks if a list of divisors of n, excluding n itself"""
    if n <= 0:
        raise ValueError("Input must be a positive integer greater than 0")

    return [i for i in range(1, n) if n % i == 0]


def is_perfect_number(n):
    """
    Checks if a given number is perfect.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer greater than 0")

    return sum(get_divisors(n)) == n


def perfect_numbers_in_range(start, end):
    """
    Returns all perfect numbers in a specified range.
    """
    if start <= 0 or end <= 0:
        raise ValueError("Both start and end must be positive integers")
    if start > end:
        raise ValueError("Start should not be greater than end")

    return [num for num in range(start, end + 1) if is_perfect_number(num)]


if __name__ == "__main__":
    try:
        # Example usage
        found_perfect_numbers = perfect_numbers_in_range(1, 1000)
        print("Perfect numbers between 1 and 1000:", found_perfect_numbers)
    except ValueError as e:
        print(f"Error: {e}")
