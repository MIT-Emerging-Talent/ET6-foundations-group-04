"""
Module for the Voting age challenge.

Contents: 
- Contextual code for names and a list to refer back to
- Code that can refer back to minimum age and name list and produce an output base on name selection

Created on 2025-01-03
Author: Adolfo Fumero
""" 

min_age = 18 # this states the minimum age for voting

participants = {
    'Jackson': {'age': 18},
    'Bob': {'age': 40},
    'Charlotte': {'age': 17},
    'Marley': {'age': 28},
    'Erica':{'age': 6},
}

def check_voting_age(person):
    """
General: 
    This function's goal is to check the age of the participants and if they are equal or above the minimum voting age based on input of name
    It pulls name and age from the Participants list and provides a Boolean output
    
Parameters:
    Name: Correct name from Participants list 
    Name list: Jackson , Bob, Charlotte, Marley, Erica
    
Raises: 
    If an invalid name is written, it will provide a "Participant not found." Output
    Correct capitalization is required, otherwise "Participant not found" Error will be raised 
"""
    return person['age'] >= min_age

# Ask for the name input
name = input("Enter the participant's name (Jackson, Bob, Charlotte, Marley, Erica): ")

# Check if the name exists in the participants dictionary
if name in participants:
    result = check_voting_age(participants[name])
    print(f"Can {name} vote?: {result}")
else:
    print("Participant not found.")
