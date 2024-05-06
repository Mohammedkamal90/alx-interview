#!/usr/bin/python3
"""
Module for making change using the fewest number of coins
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total

    Args:
        coins (list): List of coin values
        total (int): Target total

    Returns:
        int: Fewest number of coins needed to meet total, or -1 if total cannot be met
    """
    if total < 1:
        return 0

    # Initialize an array to store the fewest coins needed for each total from 0 to target total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0  # Base case: 0 coins needed for total of 0

    # Iterate through each coin value
    for coin in coins:
        # Update min_coins array for each total from coin value to target total
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
