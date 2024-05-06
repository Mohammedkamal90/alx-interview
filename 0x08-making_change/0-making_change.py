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
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total of 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp array for each total from coin value to target total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

if __name__ == "__main__":
    # Test cases
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
