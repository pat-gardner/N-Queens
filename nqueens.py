import numpy as np
import sys
# import ipdb


num_sol = 0


def solve(n):
    """Solve n-queens by guessing"""
    # board[:, 0] = 1  # start all the queens on the first column
    # ipdb.set_trace()
    backtracking_solve(np.zeros((n, n), dtype=int), 0)
    print("Found %d solutions" % num_sol)


def backtracking_solve(board, row):
    global num_sol
    if row == board.shape[1]:  # We've placed a queen in every row, so we're done
        return True
    for col in range(board.shape[0]):
        board[row] = 0
        if no_conflicts(board, row, col):
            board[row, col] = 1
            if backtracking_solve(board.copy(), row+1):
                # print(board, '\n')
                num_sol += 1
    # No safe spots in current row, need to backtrack
    return False


def no_conflicts(board, row, col):
    """Check if a space is safe. Call before setting that spot to 1"""
    cols = board.any(axis=0)
    if cols[col]:
        return False  # There's another queen in this column
    for i in range(board.shape[0]):
        if i == row:
            continue
        delta = abs(i - row)
        left = col - delta
        right = col + delta
        if 0 <= left < board.shape[1]:
            if board[i, left]:
                return False
        if 0 <= right < board.shape[1]:
            if board[i, right]:
                return False
    return True


if __name__ == "__main__":
    if len(sys.argv) == 1:
        solve(4)
    else:
        solve(int(sys.argv[1]))
