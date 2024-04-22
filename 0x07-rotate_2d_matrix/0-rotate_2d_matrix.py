#!/usr/bin/python3
"""
rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """
    rotate 2D matrix 90 degrees clockwise in place
    """
    if not matrix:
        return

    n = len(matrix)

    # transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse rows
    for row in matrix:
        row.reverse()

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
