import numpy as np
import sys
import random

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
        print(board)
        return True
    for col in range(board.shape[0]):
        board[row] = 0
        if not conflicted(board, row, col):
            board[row, col] = 1
            if backtracking_solve(board.copy(), row+1):
                # print(board, '\n')
                # num_sol += 1
                return True
    # No safe spots in current row, need to backtrack
    return False


def iterative_solve(n):
    board = np.zeros((n, n), dtype=int)
    board[:, 0] = 1
    # import ipdb; ipdb.set_trace()
    while not is_solved(board):
        row = random.randrange(n)
        board[row] = 0
        conflicts = np.zeros(n, dtype=int)
        # Place the queen in the least conflicted spot
        for i in range(n):
            conflicts[i] = count_conflicts(board, row, i)
        cols = np.where(conflicts == np.min(conflicts))[0]
        col = np.random.choice(cols)  # If ties, choose a random good spot
        board[row, col] = 1

    print(board)


def is_solved(board):
    for row in range(len(board)):
        col = np.argmax(board[row])  # Find the index of the queen in this row
        if count_conflicts(board, row, col) > 1:
            return False

    return True


def count_conflicts(board, row, col):
    n = board.shape[0]
    conflicts = 0
    conflicts += board.sum(axis=0)[col]  # Number of queens sharing this column
    for i in range(n):  # Count the queens sharing a diagonal
        if i == row:
            continue
        delta = abs(i - row)
        left = col - delta
        right = col + delta
        if 0 <= left < board.shape[1]:
            if board[i, left]:
                conflicts += 1
        if 0 <= right < board.shape[1]:
            if board[i, right]:
                conflicts += 1
    return conflicts


def conflicted(board, row, col):
    """Check if a space is safe. Call before setting that spot to 1"""
    cols = board.any(axis=0)
    if cols[col]:
        return True  # There's another queen in this column
    for i in range(board.shape[0]):
        if i == row:
            continue
        delta = abs(i - row)
        left = col - delta
        right = col + delta
        if 0 <= left < board.shape[1]:
            if board[i, left]:
                return True
        if 0 <= right < board.shape[1]:
            if board[i, right]:
                return True
    return False


if __name__ == "__main__":
    if len(sys.argv) == 1:
        solve(4)
    elif len(sys.argv) != 3:
        print('Bad input')
        exit(-1)
    elif sys.argv[1] == 'b':
        solve(int(sys.argv[2]))
    else:
        iterative_solve(int(sys.argv[2]))
