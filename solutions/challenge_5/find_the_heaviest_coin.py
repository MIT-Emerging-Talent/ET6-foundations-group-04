#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding the heaviest coin among 8 coins using a balance scale.

Module contents:
    - find_heaviest_coin: Identifies the heaviest coin with the minimum number of weigh-ings

Created on 29/12/2024
Author: Chrismy Leprince Paul Augustin
"""


def find_heaviest_coin(coins):
    """
    Finds the heaviest coin among 8 coins using a balance scale with the minimum number of weighings.

    Parameters:
        coins (list): A list of integers representing the weights of the 8 coins.

    Returns:
        int: The index of the heaviest coin (1-based index).
    """
    # Split coins into three groups: first three, second three, and the last two
    group1 = coins[:3]
    group2 = coins[3:6]
    group3 = coins[6:]

    # First weigh-ing: compare group1 and group2
    if sum(group1) > sum(group2):
        heavier_group = group1
    elif sum(group1) < sum(group2):
        heavier_group = group2
    else:
        heavier_group = group3

    # Second weighing: compare coins within the heavier group
    if len(heavier_group) == 3:
        if heavier_group[0] > heavier_group[1]:
            if heavier_group[0] > heavier_group[2]:
                return coins.index(heavier_group[0]) + 1
            else:
                return coins.index(heavier_group[2]) + 1
        else:
            if heavier_group[1] > heavier_group[2]:
                return coins.index(heavier_group[1]) + 1
            else:
                return coins.index(heavier_group[2]) + 1
    else:
        # If the heavier group contains only 2 coins, compare them
        return coins.index(max(heavier_group)) + 1
