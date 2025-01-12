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
    """
    if number <= 1:
        return "not prime"
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return "not prime"
    return "is prime"


# Main program to take user input and call the prime_numbers function
if __name__ == "__main__":
    try:
        # Demander à l'utilisateur d'entrer un nombre
        number = int(input("Enter a number to check if it is prime: "))
        
        # Appeler la fonction et afficher le résultat
        result = prime_numbers(number)
        print(f"The number {number} is {result}.")
    
    except ValueError:
        print("Please enter a valid integer.")
