"""
Tic Tac Toe Player
"""

import math
import copy

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
    countX = 0
    countO = 0
    for row in board:
        for element in row:
            if element == X: countX += 1
            elif element == O: countO += 1
    if countX > countO:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                actions.add((row, col))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row = action[0]
    col = action[1]
    
    if board[row][col] != EMPTY:
        raise Exception
    
    turn = player(board)
    new_board = copy.deepcopy(board)
    new_board[row][col] = turn
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winners = []
    slant1 = []
    slant2 = []
    for i in range(3):
        winners.append(board[i])
        vertical = []
        for j in range(3):
            vertical.append(board[j][i])
            if i == j:
                slant1.append(board[i][j])
            if j == 2 - i:
                slant2.append(board[i][j])
        winners.append(vertical)
    winners.append(slant1)
    winners.append(slant2)
    
    for line in winners:
        if len(set(line)) == 1:
            return line[0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        for element in row:
            if element == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    turn = player(board)
    moves = actions(board)
    values = {}
    if turn == X:
        for move in moves:
            value = min_value(result(board, move))
            if value == 1:
                return move
            values[move] = value
        elements = list(values.values())
        return (list(values.keys())[elements.index(max(elements))])
    else:
        for move in moves:
            value = max_value(result(board, move))
            if value == -1:
                return move
            values[move] = value
        elements = list(values.values())
        return (list(values.keys())[elements.index(min(elements))])

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -2
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
        if v == 1:
            return v
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = 2
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
        if v == -1:
            return v
    return v