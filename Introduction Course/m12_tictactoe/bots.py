from asyncio.windows_events import INFINITE
import random

from game_functions import *

scores = {
    PLAYER_X: 1,
    PLAYER_O: -1,
    TIE: 0
}

def my_bot(board, current_player):
    """
    Calculates the best move for the bot player in a current boardstate based on the minimax algorithm
    :param board: list with all board elements representing the current game state
    :param current_player: string indicating the current player (either PLAYER_X or PLAYER_O)
    :return: number between 0 and 8 indicating the chosen move
    """
    best_score = -INFINITE
    move = None
    valid_moves = get_valid_moves(board)
    for currMove in valid_moves:
        board[currMove] = PLAYER_1
        # Maximizing False it tries the possible moves of the other player
        score = minimax(board, 0, False)
        board[currMove] = EMPTY
        if(score > best_score):
            best_score = max(score, best_score)
            move = currMove
    
    return move

def minimax(board, depth, isMaximizing):
    """
    A recursive function which follows the minimax algorithm. 
    This was the first attempt of me coding this algorithm and it gave me a massive headache
    I tried not to follow any tutorial on the topic of it but soly rely on this source: https://www.youtube.com/watch?v=l-hh51ncgDI
    Hope you like my effort!

    I am aware of a weird problem that makes MM make a very obvious mistake when it goes first but I do not know how to fix it
    :param board: list with all board elements representing the current game state
    :param depth: An integer that indicates the depth of the recursive calls. May be implemented to limit the minimax's power which i opted not to do
    :return: integer [-1,0,1] displaying the score of the currently selected option 
    """
    result = checkWinner(board)
    if result is not None:
        return scores[result]
    
    valid_moves = get_valid_moves(board)
    
    best_score = -INFINITE if isMaximizing else INFINITE

    for currMove in valid_moves:
        # You could also shallow copy the board object but it would be less performant and MM is already quite performance intensive so I chose this solution
        board[currMove] = PLAYER_1 if isMaximizing else PLAYER_2
        # Maximizing False it tries the possible moves of the other player
        score = minimax(board, depth + 1, not(isMaximizing))
        board[currMove] = EMPTY
        best_score = max(score, best_score) if isMaximizing else min(score, best_score)
    return best_score
    
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
