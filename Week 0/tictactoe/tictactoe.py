"""
Tic Tac Toe Player
"""

import math
import copy

from pygame.constants import CONTROLLER_BUTTON_LEFTSHOULDER

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_num = 0
    o_num = 0
    empty_num = 0
    for i in board:
        for j in i:
            if j == X:
                x_num += 1
            elif j == O:
                o_num += 1
            else:
                empty_num += 1

    # Compare amount to determine whose turn
    if empty_num == 9 or x_num == o_num:
        return X
    elif x_num > o_num:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception(f"Action {action}, is not valid in this State")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    p = O if player(board) == X else X
    # Check horizontally
    for row in board:
        if row == [p, p, p]:
            return p
    # Check vertically
    for i in range(3):
        if board[0][i] == p and board[1][i] == p and board[2][i] == p:
            return p
    # Check Diagonally
    if (board[0][0] == p and board[1][1] == p and board[2][2] == p) or (board[0][2] == p and board[1][1] == p and board[2][0] == p):
        return p
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    full_board = 0
    for i in board:
        for j in i:
            if j != EMPTY:
                full_board += 1

    if winner(board) or full_board == 9:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board)

    best_move = None
    if player(board) == X:
        best_value = -math.inf
        for action in actions(board):
            x = Min(result(board, action))
            if x > best_value:
                best_value = x
                best_move = action
    elif player(board) == O:
        best_value = math.inf
        for action in actions(board):
            x = Max(result(board, action))
            if x < best_value:
                best_value = x
                best_move = action
    print(best_move)
    return best_move


def Max(board):
    if terminal(board):
        return utility(board)
    best_value = -math.inf
    for action in actions(board):
        best_value = max(best_value, Min(result(board, action)))
    return best_value


def Min(board):
    if terminal(board):
        return utility(board)
    best_value = math.inf
    for action in actions(board):
        best_value = min(best_value, Max(result(board, action)))
    return best_value
