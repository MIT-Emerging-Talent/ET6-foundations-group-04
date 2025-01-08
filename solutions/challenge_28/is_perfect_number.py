#! user/bin/env python3
# _*_cooidng: utf-8
"""
Created on 01/03/2025

@Author: Cliforde Exael
"""


def is_perfect_number(n):
    """
    Check if a number is a perfect number.
    A perfect number is a number that is equal to the sum of its proper divisors (excluding itself).
    """
    if n <= 1:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n


def find_perfect_numbers(input_set):
    """
    Find all perfect numbers in the given set of positive numbers.
    """
    return [num for num in input_set if is_perfect_number(num)]


# Create a list of natural numbers from 1 to 1000
natural_numbers = set(range(1, 1001))

# Find all perfect numbers within this range
perfect_numbers = find_perfect_numbers(natural_numbers)

# Print the list of perfect numbers
print("Perfect numbers between 1 and 1000:", perfect_numbers)
