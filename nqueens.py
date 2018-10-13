import numpy as np


def solve(n):
    """Solve n-queens by guessing"""
    board = np.zeros((n, n), dtype=int)
    # board[:, 0] = 1  # start all the queens on the first column
    recursive_solve(board, 0,0)
    print(board)


def recursive_solve(board, y, x):
    pass


if __name__ == "__main__":
    solve(4)
