def tribonacci(n: int) -> int:
    """
        Calculate the nth tribonacci number.

        Args:
            n (int): Index of the tribonacci number to calculate.

        Returns:
            int: The nth tribonacci number.

        Created on 1/01/2025
    Author: Ana Isabel Murillo
    """
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    a, b, c = 0, 1, 1

    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c

    return c
