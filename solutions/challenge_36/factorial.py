def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Args:
        n (int): Non-negative integer whose factorial is to be calculated.

    Returns:
        int: Factorial of the input number n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        print(f"Factorial of {num} is {factorial(num)}")
    except ValueError as e:
        print(f"Error: {e}")
