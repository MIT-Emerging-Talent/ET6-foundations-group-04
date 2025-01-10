def tribonacci(n: int) -> int:
    """
        Calculate the nth Tribonacci number.
        The objective is to write an efficient function to compute the nth Tribonacci number while handling edge cases and invalid inputs.

    The Tribonacci sequence starts as follows:
    T(0) = 0, T(1) = 1, T(2) = 1, and for n >= 3,
    T(n) = T(n-1) + T(n-2) + T(n-3).

    This function utilizes an iterative approach to calculate the Tribonacci sequence.
    It maintains a list of the last three calculated numbers and iteratively updates this list
    by adding the sum of the three numbers to the end, effectively simulating the Tribonacci sequence's definition.
    This iterative method provides efficient calculation without the overhead of recursive function calls.

    Returns the first n numbers of the tribonacci sequence.

    Args:

        n (int): A non-negative integer representing the index of the Tribonacci number to calculate.

    Returns:
        int: The nth Tribonacci number.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> tribonacci(0)
        0
        >>> tribonacci(2)
        1
        >>> tribonacci(5)
        7

        Created on 1/01/2025
    Author: Ana Isabel Murillo
    """

    if n < 0:
        raise ValueError("Index 'n' must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    a, b, c = 0, 1, 1

    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c

    return c
