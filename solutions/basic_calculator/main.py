"""
A module for performing basic arithmetic operations: addition, subtraction,
multiplication, and division.

Module contents:
    - calculate: Performs the specified arithmetic operation on two numbers

Created on 28/12/2024
Author: Ana Isabel Murillo
"""


def calculate(operation: str, num1: float, num2: float) -> float:
    """Performs the specified arithmetic operation on two numbers.

    Parameters:
        operation: str, the operation to perform
        ('add', 'subtract', 'multiply', 'divide')
        num1: float, the first number
        num2: float, the second number

    Returns -> float: the result of the arithmetic operation

    Raises:
        ValueError: if the operation is invalid or division by zero occurs

    Examples:
        >>> calculate('add', 5, 3)
        8.0
        >>> calculate('subtract', 10, 4)
        6.0
        >>> calculate('multiply', 7, 3)
        21.0
        >>> calculate('divide', 9, 3)
        3.0
        >>> calculate('divide', 5, 0)
        Traceback (most recent call last):
            ...
        ValueError: Cannot divide by zero.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError(
            f"Invalid operation '{operation}'. Valid operations are: "
            "add, subtract, multiply, divide."
        )
