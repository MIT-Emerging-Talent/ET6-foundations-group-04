"""
Unit test for the Voting age challenge.

This module runs 4 unit tests to verify the code can successfully refer the names back to the list
and verify their age against the minimum age
This test will include
- Basic cases: Test will calculate basic correct name inputs
- Defensive cases: Test will include: Inputs that may create an error for not being in the list
or not capitalized properly

Created on 2025-01-06
Author: Adolfo Fumero
"""

import unittest

from voting_age.main import check_voting_age

MIN_AGE = 18

participants = {
    "jackson": {"age": 18},
    "bob": {"age": 40},
    "charlotte": {"age": 17},
    "marley": {"age": 28},
    "erica": {"age": 6},
}


class TestCheckVotingAge(unittest.TestCase):
    """Tests the check_voting_age function"""

    def test1(self):
        """Test if a person exactly at the voting age is eligible."""
        jackson = participants["jackson"]
        self.assertTrue(check_voting_age(jackson))

    def test2(self):
        """Test if a person above the voting age is eligible."""
        bob = participants["bob"]
        self.assertTrue(check_voting_age(bob))

    def test3(self):
        """Test if a person below the voting age is not eligible."""
        charlotte = participants["charlotte"]
        self.assertFalse(check_voting_age(charlotte))

    def test4(self):
        """Test if a person far below the voting age is not eligible."""
        erica = participants["erica"]
        self.assertFalse(check_voting_age(erica))
