"""
Tic Tac Toe Player
"""

import copy
import math

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
    xs= 0
    os = 0
    for arr in board:
        for item in arr:
            if item == X: xs+=1
            if item == O: os+=1
    if xs % 2 == os % 2:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY: action.add((i,j))
    return action



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turn = player(board)
    copboard = copy.deepcopy(board)
    
    i, j = action
    if board[i][j] != None:
        raise Exception
    else:
        copboard[i][j] = turn
    return copboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2]: return board[0][0]
    if board[2][0] == board[1][1] == board[0][2]: return board[1][1]
    return None                 

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    result = winner(board)
    if result != None: return True
    return actions(board) == set()


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None
    turn = player(board)
    if turn == X:
        return myMAX(board)[0]
    else:
        return myMIN(board)[0]


def myMAX(board, alpha=-10, beta=10):
    """
    Returns the max value of the board.
    Returns the action first with its value second.
    """
    action_highest_value = ()
    if terminal(board): return action_highest_value, utility(board)
    highest_value = -10
    myactions = actions(board)
    for action in myactions:
        value = myMIN(result(board, action), alpha, beta)[1]
        if value > highest_value:
            highest_value = value
            action_highest_value = action
        alpha = max(alpha, value)
        if beta <= alpha:
            break
    return action_highest_value, highest_value


def myMIN(board, alpha=-10, beta=10):
    """
    Returns the min value of the board.
    Returns the action first with its value second.
    """
    action_lowest_value = ()
    if terminal(board): return action_lowest_value, utility(board)
    lowest_value = 10
    myactions = actions(board)
    for action in myactions:
        value = myMAX(result(board, action), alpha, beta)[1]
        if value < lowest_value:
            lowest_value = value
            action_lowest_value = action
        beta = min(beta, value)
        if beta <= alpha:
            break
    return action_lowest_value, lowest_value

    
