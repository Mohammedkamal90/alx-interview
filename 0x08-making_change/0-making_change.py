#!/usr/bin/python3
"""
change comes from within
"""

def makeChange(coins, total):
    # Base cases
    if total < 0:
        return -1
    if total == 0:
        return 0
    
    # Initialize a table to store minimum coins required for each total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins needed to make total 0
    
    # Iterate over each coin denomination
    for coin in coins:
        # For each coin denomination, iterate over possible amounts
        # starting from the value of the coin up to the total amount
        for amount in range(coin, total + 1):
            # Update dp[amount] if using this coin results in fewer coins
            # The minimum number of coins for the current amount (amount) is
            # the minimum of the current value in dp[amount] and the value of
            # dp[amount - coin] + 1 (where dp[amount - coin] represents the
            # minimum number of coins needed for the remaining amount after
            # subtracting the value of the current coin)
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If the final entry in dp is still infinity, it means the total amount
    # cannot be made up using the available coins, so return -1
    return dp[total] if dp[total] != float('inf') else -1

# Test cases
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))   # Output should be 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output should be -1
