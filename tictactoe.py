"""
Tic Tac Toe Player
"""

from cmath import inf
import sys

from pygame import init

sys.setrecursionlimit(10000)
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
    cnt = 0
    for j in range(3):
        for k in range(3):
            if board[j][k] != EMPTY:
                cnt += 1
    if cnt % 2 == 0:
        return "X"
    return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for j in range(3):
        for k in range(3):
            if board[j][k] == EMPTY:
                action.add((j, k))
    action = list(action)
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new = [[EMPTY for j in range(3)] for k in range(3)]
    for j in range(3):
        for k in range(3):
            new[j][k] = board[j][k]
    turn = player(new)
    if new[action[0]][action[1]] != EMPTY:
        raise ValueError("cell already filled. Invalid action")
    new[action[0]][action[1]] = turn
    return new




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[1][1] and board [1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    for j in range(3):
        if board[j][0] == board[j][1] and board[j][1] == board[j][2]:
            return board[j][0]
        if board[0][j] == board[1][j] and board[1][j] == board[2][j]:
            return board[0][j]
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)
    if win == None:
        cnt = 0
        for j in range(3):
            for k in range(3):
                if board[j][k] != EMPTY:
                    cnt += 1
        if cnt == 9:
            return True 
    else:
        return win


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == "X":
        return 1
    if win == "O":
        return -1
    return 0

        

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    play = player(board)
    action = actions(board)
    if play == "X":
        v = -inf
        move = ()
        for j in range(len(action)):
            score = minval(result(board, action[j]), v)
            if score > v:
                move = action[j]
                v = score
                if v == 1:
                    break
    else:
        v = inf
        move = ()
        for j in range(len(action)):
            score = maxval(result(board, action[j]), v)
            if score < v:
                v = score
                move = action[j]
                if v == -1:
                    break
    return move

def maxval(board, alpha):
    if terminal(board):
        return utility(board)
    v = -inf
    action = actions(board)
    for j in range(len(action)):
        score = max(v, minval(result(board, action[j]), v))
        if score > v:
            v = score
        if v > alpha:
            break
    return v

def minval(board, alpha):
    if terminal(board):
        return utility(board)
    v = inf
    action = actions(board)
    for j in range(len(action)):
        score = min(v, maxval(result(board, action[j]), v))
        if score < v:
            v = score
        if v < alpha:
            break
    return v