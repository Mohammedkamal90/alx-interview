#!/usr/bin/python3
"""Prime Game: A game between Maria and Ben"""

def isWinner(x, nums):
    """
    Determine the winner of the prime game

    Args:
    - x: number of rounds
    - nums: list of integers representing n for each round

    Returns:
    - The name of the player who won the most rounds (or None if the winner cannot be determined)
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben_wins = 0
    maria_wins = 0

    prime_flags = [1] * (max(nums) + 1)
    prime_flags[0], prime_flags[1] = 0, 0

    for num in range(2, len(prime_flags)):
        remove_multiples(prime_flags, num)

    for n in nums:
        if sum(prime_flags[:n + 1]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    if maria_wins > ben_wins:
        return "Maria"
    return None

def remove_multiples(prime_flags, num):
    """
    Remove multiples of a prime number from the list of flags

    Args:
    - prime_flags: list of flags indicating whether a number is prime
    - num: the prime number whose multiples should be removed
    """
    for i in range(2 * num, len(prime_flags), num):
        prime_flags[i] = 0
