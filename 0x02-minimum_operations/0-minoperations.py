#!/usr/bin/env python3
""" single character H. Your text editor
can execute only two operations in this file: `Copy All` and `Paste`
"""

def minOperations(n: int) -> int:
    if n <= 1:
        return n

    operations = 0
    clipboard = 1  # Initially, the clipboard contains one 'H'
    result = 1  # Initially, we have one 'H' in the file

    while result < n:
        if n % result == 0:  # If result is a divisor of n, perform Copy All
            clipboard = result
            operations += 1
        result += clipboard  # Paste the content of the clipboard
        operations += 1

    return operations

# Example usage
if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
