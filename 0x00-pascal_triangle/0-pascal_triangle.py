#!/usr/bin/python3
"""
Generate Pascal's triangle up to the nth row.
"""
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        current_row = [1]

        for k in range(1, i):
            current_row.append(prev_row[k - 1] + prev_row[k])

        current_row.append(1)
        triangle.append(current_row)

    return triangle
