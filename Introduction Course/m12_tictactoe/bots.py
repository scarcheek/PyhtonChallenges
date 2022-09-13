import random

from game_functions import *


def my_bot(board, current_player):
    """
    Uses the minimax algorithm to determine the best possible move for the bot
    :param board: list with all board elements representing the current game state
    :param current_player: string indicating the current player (either PLAYER_X or PLAYER_O)
    :return: number between 0 and 8 indicating the chosen move
    """
    # First time i try implementing the MM algorithm, wish me luck
    valid_moves = get_valid_moves(board)
    

    # TODO return the chosen move your bot thinks is the best
    return pos


def random_bot(board, current_player):
    """
    Bot that selects a random valid move
    :param board: list with all board elements representing the current game state
    :param current_player: string indicating the current player (either PLAYER_X or PLAYER_O)
    :return: number between 0 and 8 indicating a random (valid) move
    """

    # get all valid moves in the current board state
    valid_moves = get_valid_moves(board)

    # return a random move
    return random.choice(valid_moves)
