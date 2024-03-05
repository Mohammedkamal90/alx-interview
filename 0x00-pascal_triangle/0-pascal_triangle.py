#!/usr/bin/python3
""" pascal triangle
"""

def pascal_triangle(n):
    """Returns Pascal's triangle as a list of lists."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1] + [prev_row[j - 1] + prev_row[j] for j in range(1, i)] + [1]
        triangle.append(current_row)

    return triangle
