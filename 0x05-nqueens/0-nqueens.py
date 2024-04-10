#!/usr/bin/python3
"""
N Queens Puzzle Solver
"""

import sys


class NQueensSolver:
    """
    Class to solve N queens problem
    """

    def __init__(self, n):
        """
        initialize solver with necessary attributes.

        Args:
            n (int): size of the chessboard.
        """
        self.n = n
        self.solutions = []
        self.pos = None

    def is_attacking(self, pos0, pos1):
        """
        check if positions of two queens are in an attacking mode.

        Args:
            pos0 (list or tuple): first queen's position.
            pos1 (list or tuple): second queen's position.

        Returns:
            bool: True if the queens are in an attacking position else False.
        """
        if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
            return True
        return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])

    def group_exists(self, group):
        """
        Checks if a group exists in list of solutions.

        Args:
            group (list of integers): group of possible positions.

        Return:
            bool: True if it exists, otherwise False
        """
        for stn in self.solutions:
            i = 0
            for stn_pos in stn:
                for grp_pos in group:
                    if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                        i += 1
            if i == self.n:
                return True
        return False

    def build_solution(self, row, group):
        """
        build solution for N queens problem

        Args:
            row (int): The current row in the chessboard.
            group (list of lists of integers): group of valid positions
        """
        if row == self.n:
            tmp0 = group.copy()
            if not self.group_exists(tmp0):
                self.solutions.append(tmp0)
        else:
            for col in range(self.n):
                a = (row * self.n) + col
                matches = zip(list([self.pos[a]]) * len(group), group)
                used_positions = map(lambda x: self.is_attacking(x[0], x[1]), matches)
                group.append(self.pos[a].copy())
                if not any(used_positions):
                    self.build_solution(row + 1, group)
                group.pop(len(group) - 1)

    def get_solutions(self):
        """
        get solution for given chessboard size
        """
        self.pos = list(map(lambda x: [x // self.n, x % self.n], range(self.n ** 2)))
        a = 0
        group = []
        self.build_solution(a, group)

    def solve(self):
        """
        solve N queens problem and print solutions.
        """
        self.get_solutions()
        for solution in self.solutions:
            print(solution)


def main():
    """
    Main function to parse command-line arguments and run solver
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueensSolver(n)
    solver.solve()


if __name__ == "__main__":
    main()
