"""
Module for the Triangular number sequence and a code that can calculate it.

Contents:
- A formula that establishes the triangular number sequence n(n+1)/2
- Code for the formula to be able to take input

Created on 2025-01-03
Author: Adolfo Fumero
"""


def triangle_side(n):
    """
    Calculate the nth triangular number.
    Uses a formula of n(n+1)/2 to calculate the number of sides of the triangle in the sequence

    Parameters:
        n (int): The position in the triangular number sequence.

    Returns:
        int: The nth triangular number.

    Raises:
        If any value below 0 is input, it will throw an Error message
        If any non-integer value is input also, same output will occur
    """
    if n < 1:
        return "Input must be a positive integer."
    return n * (n + 1) // 2


# Example usage
try:
    user_input = int(
        input("Enter an integer value for the triangular number sequence: ")
    )
    result = triangle_side(user_input)
    print(f"The {user_input}th triangular number is: {result}")
except ValueError:
    print("Please enter a valid integer.")
