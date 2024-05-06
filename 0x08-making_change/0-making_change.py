#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    # Initialize a list to store minimum number of coins for each amount from 0 to total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0  # Base case

    for amount in range(1, total + 1):
        # For each coin value, calculate minimum coins needed for current amount
        for coin in coins:
            if coin <= amount:
                min_coins[amount] = min(min_coins[amount], min_coins[amount - coin] + 1)

    if min_coins[total] == float('inf'):
        return -1  # If total cannot be met by any number of coins you have

    return min_coins[total]
