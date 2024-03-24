#!/usr/bin/python3
""" single character H. Your text editor
can execute only two operations in this file: `Copy All` and `Paste`
"""


def minOperations(n):
    if n <= 0:
        return 0
    return minOperationsHelper(n, 1, 0, 0)

def minOperationsHelper(n, buffer, clipboard, operations):
    if buffer == n:
        return operations
    if buffer > n:
        return float('inf')
    # Copy All
    if clipboard == 0:
        return minOperationsHelper(n, buffer, buffer, operations + 1)
    # Paste
    return min(
        minOperationsHelper(n, buffer + clipboard, clipboard, operations + 1),
        minOperationsHelper(n, buffer + buffer, buffer, operations + 2)
    )

# Example usage:
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
