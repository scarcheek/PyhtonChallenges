from bots import random_bot, my_bot
from game_functions import *
from typing import Literal

MM_Game = True


# Made this so the source of user input being actually reliable is not "Trust me bro" anymore
def intTryParse(value):
  """A function that takes a value and tries to convert it to an integer. If it can, it returns the integer and True. If it can't, it returns the value and False."""
  try:
      return int(value), True
  except ValueError:
      return value, False

def select_players() -> tuple[int, int]:
    player_1 = -1; player_2 = -1
    while(player_1 == -1):
        print(f"Select Player {PLAYER_X}:")
        print("--== Your options are ==--")
        print(f"| 1 -> Human\n| 2 -> Random AI\n| 3 -> Minimax AI (Performance intensive)")
        print("--======================--")
        user_in = intTryParse(input())
        if user_in[1] and user_in[0] in [1,2,3]: player_1 = user_in[0] 

    while (player_2 == -1):
        print(f"Select Player {PLAYER_O}:")
        print("--== Your options are ==--")
        print(f"| 1 -> Human\n| 2 -> Random AI\n| 3 -> Minimax AI (Performance intensive)")
        print("--======================--")
        user_in = intTryParse(input())
        if user_in[1] and user_in[0] in [1,2,3]: player_2 = user_in[0]

    return player_1, player_2

def get_player_logic(board, turn, player):
    if(player == 1):
         # uncomment line 26 and comment line 27 and 28 to let your bot play against the random bot
        # position = my_bot(board, turn)
        user_in = input(f"Player {turn}, place your piece: ")

        vm_result = valid_move(user_in, board)
        while not vm_result[1]: 
            user_in = input(f"Incorrect input. Please retry: ")
            vm_result = valid_move(user_in, board)
        return vm_result[0]
    elif(player == 2):
        print(f"Random Bot {turn}:")
        return random_bot(board, turn)
    elif(player == 3):
        print(f"Minimax {turn}:")
        return my_bot(board, turn)


def play_game():
    """
    m12_tictactoe game logic
    :return: (no return value)
    """
    print("Welcome to the TicTacToe game!")
    player_1, player_2 = select_players()
    
    board = init_board()
    print("Game started!")
    print("X: Player X, O: Player O, -: Empty spot")
    print("Enter the number (0-8) of an empty spot to fill it\n")

    print_board(board)
    turn = PLAYER_O

    while not game_over(board):
        if turn == PLAYER_1:
           position = get_player_logic(board, turn, player_1)
        else:
           position = get_player_logic(board, turn, player_2)

        # place piece on board
        board = perform_move(turn, position, board)

        # print board to screen
        print_board(board)

        # switch turns
        turn = PLAYER_X if turn == PLAYER_O else PLAYER_O

    # determine winner
    winner(board)


if __name__ == '__main__':
    play_game()
