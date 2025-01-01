#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday 31 17:00:00 2024

@author: Cliforde Exael
"""


def prime_numbers(number: int) -> str:
    """
    Determines whether a given number is a prime number.

    A prime number is a natural number greater than 1 that has no divisors other than 1 and itself.
    This function checks if the input number meets the criteria of being a prime number.

    Args:
        number (int): The number to be checked.

    Returns:
        str: A string indicating whether the number is prime or not.
             Returns "is prime" if the number is prime, otherwise "not prime".

    Algorithm:
        1. If the number is less than or equal to 1, it is not a prime number.
        2. Iterate from 2 to the square root of the number (inclusive).
           - If the number is divisible by any of these values, it is not a prime number.
        3. If no divisors are found, the number is a prime number.

    Example Usage:
        >>> prime_numbers(9)
        'not prime'
        >>> prime_numbers(7)
        'is prime'
        >>> prime_numbers(1)
        'not prime'
        >>> prime_numbers(13)
        'is prime'

    Note:
        - This function uses a simple algorithm to check for primality by testing divisors
          up to the square root of the input number for efficiency.
        - The result is returned as a string, which may be useful for simple display or testing.
    """
    if number <= 1:
        return "not prime"
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return "not prime"
    return "is prime"


# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = prime_numbers(number)
    print(result)
