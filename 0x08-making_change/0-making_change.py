#!/usr/bin/python3
'''
Given a pile of coins of different values,
determine the fewest number of coins needed to meet
a given amount total.
'''
import sys


def makeChange(coins, total):
    '''
    Return the fewest number of coins needed to meet total.
    If total is 0 or less, return 0.
    If total cannot be met by any number of coins you have, return -1.
    '''
    if total <= 0:
        return 0
    
    # Initialize a table to store minimum coins required for each total
    min_coins = [sys.maxsize for _ in range(total + 1)]
    min_coins[0] = 0
    
    num_coins = len(coins)
    
    # Iterate through each possible total amount
    for amount in range(1, total + 1):
        # Iterate through each coin denomination
        for coin_index in range(num_coins):
            coin_value = coins[coin_index]
            # Check if the coin value is less than or equal to the current total
            if coin_value <= amount:
                # Calculate the number of coins needed for the remaining amount
                sub_result = min_coins[amount - coin_value]
                # Update the minimum coins if using this coin results in fewer coins
                if sub_result != sys.maxsize and sub_result + 1 < min_coins[amount]:
                    min_coins[amount] = sub_result + 1

    # If the minimum coins for the total amount is still sys.maxsize, return -1
    return min_coins[total] if min_coins[total] != sys.maxsize else -1

# Test cases
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))   # Output should be 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output should be -1
