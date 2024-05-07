#!/usr/bin/python3
"""
0-island_perimeter module
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.

    Args:
        grid (list[list[int]]): A list of lists of integers representing the island.

    Returns:
        int: The perimeter of the island.

    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # If the cell is land
                perimeter += 4  # Initialize perimeter assuming all sides are contributing

                # Check adjacent cells
                if i > 0 and grid[i - 1][j] == 1:  # Check top neighbor
                    perimeter -= 2  # Subtract 2 since the top side is shared
                if j > 0 and grid[i][j - 1] == 1:  # Check left neighbor
                    perimeter -= 2  # Subtract 2 since the left side is shared

    return perimeter
