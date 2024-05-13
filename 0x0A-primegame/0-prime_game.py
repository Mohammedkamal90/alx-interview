#!/usr/bin/python3
"""
Determines the winner of each round of the prime game.
"""

def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def isWinner(x, nums):
    """
    Determines the winner of each round of the prime game.

    Args:
        x: The number of rounds.
        nums: An array of n for each round.

    Returns:
        The name of the player that won the most rounds.
        If the winner cannot be determined, returns None.
    """
    if not nums:
        return None

    maria_wins = 0
    for n in nums:
        primes_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        if primes_count % 2 == 0:
            maria_wins += 1

    if maria_wins > x // 2:
        return "Maria"
    elif maria_wins == x // 2:
        return None
    else:
        return "Ben"

if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
