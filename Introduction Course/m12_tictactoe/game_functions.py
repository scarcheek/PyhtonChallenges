from copy import copy, deepcopy


EMPTY = '-'
PLAYER_X = 'X'
PLAYER_O = 'O'

PLAYER_1 = PLAYER_X
PLAYER_2 = PLAYER_O if PLAYER_1 == PLAYER_X else PLAYER_X
TIE = 'tie'


N_FIELDS = 9


def print_board(board):
    """
    Prints the current board in a readable form to the screen
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: (No return value)
    """
    
    # If you want dynamic board sizes tictactoe breaks anyways 
    displayBoard = deepcopy(board)
    for index in range(0, len(displayBoard)):
        if (displayBoard[index] == EMPTY): displayBoard[index] = index
    i = 0
    print('=============')
    while i < N_FIELDS:
      print(f'| {displayBoard[i]} | {displayBoard[i+1]} | {displayBoard[i+2]} |')
      i+=3
    print('=============\n')


def perform_move(player, position, board):
    """
    Places the piece for a player on the given position of the board
    :param player: the player which performs the move
    :param position: the position where to place the stone (0-8)
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: board after move was performed
    """
    board[position] = player

    return board


def board_full(board):
    """
    Checks if there is an empty spot on the board
    :param board: list with all board elements
    :return: True if there is no empty spot otherwise False
    """

    return not(EMPTY in board)


def iterate_board(board, player, indexes: list[int, int, int]):
    return all(x == player for x in [board[indexes[0]], board[indexes[1]], board[indexes[2]]])


def has_won(board, player):
    """
    Check if there are three equal pieces for this player in some row, column or one of the two diagonals

    :param board: list of length N_FIELDS with all board elements representing the current game state
    :param player: symbol of player that should be checked
    :return: True if three pieces in a row
    """
    # Rows
    if(iterate_board(board, player, [0,1,2]) or 
        iterate_board(board, player, [3,4,5]) or
        iterate_board(board, player, [6,7,8])): return True
    # Columns
    if(iterate_board(board, player, [0,3,6]) or 
        iterate_board(board, player, [1,4,7]) or
        iterate_board(board, player, [2,5,8])): return True

    # Diagonals
    if (iterate_board(board, player, [0,4,8]) or 
        iterate_board(board, player, [2,4,6])): return True

    return False


def game_over(board):
    """
    Checks if the game is over, i.e., no more moves are possible
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: True if the game is over (no more empty pieces left or one of the players won the game) otherwise False
    """

    
    return not(EMPTY in board) or has_won(board, PLAYER_O) or has_won(board, PLAYER_X)


def valid_move(user_in, board):
    """
    Checks whether the input of the user is a valid move.
    A move is valid if it is a number between 0 and 8 (inclusive) and if the position on the board is empty.
    :param user_in: string input of the user
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: integer between 0-8 indicating a valid position where the piece should be placed otherwise -1
    """

    if(not user_in.isnumeric()): return any, False
    user_pos = int(user_in)

    if(user_pos not in range(0,N_FIELDS) or board[user_pos] is not EMPTY): return any, False

    return user_pos, True


def init_board():
    """
    Initializes the game board
    :return: list of length N_FIELDS filled with the EMPTY symbol representing the board
    """
    board = []
    for x in range(N_FIELDS):
        board.append(EMPTY)
    return board


def winner(board):
    """
    Prints the outcome of the game to the console. Either PLAYER_X or PLAYER_O has won or it is a tie.
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: (no return value)
    """
    winner = checkWinner(board)
    if winner == PLAYER_X:
        print(f'Player {PLAYER_X} won!')
    elif winner == PLAYER_O:
        print(f'Player {PLAYER_O} won!')
    elif winner == TIE:
        print('Tie!')

def checkWinner(board):
    """
    Calculates the outcome of the game and returns it.  Either PLAYER_X or PLAYER_O has won or it is a tie.
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: ['X', 'O', 'tie']
    """
    if has_won(board, PLAYER_X):
        return PLAYER_X
    elif has_won(board, PLAYER_O):
        return PLAYER_O
    elif board_full(board):
        return TIE

# I didnt see this when programming the valid_moves function. Oopsies
def get_valid_moves(board):
    """
    Get all valid moves for the current game state
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: list off all possible moves, i.e., all position of the board that are filled with EMPTY
    """

    valid_moves = []
    for i in range(N_FIELDS):
        if board[i] == EMPTY:
            valid_moves.append(i)

    return valid_moves

