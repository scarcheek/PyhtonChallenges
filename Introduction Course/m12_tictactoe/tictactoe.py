from bots import random_bot, my_bot
from game_functions import *


def play_game():
    """
    m12_tictactoe game logic
    :return: (no return value)
    """

    board = init_board()
    print("Game started!")
    print("X: Player X, O: Player O, -: Empty spot")
    print("Enter the number (0-8) of an empty spot to fill it\n")

    print_board(board)
    turn = PLAYER_O

    while not game_over(board):

        if turn == PLAYER_X:
            print(f"Player {turn}:")
            position = random_bot(board, turn)
        else:
            # uncomment line 26 and comment line 27 and 28 to let your bot play against the random bot
            # position = my_bot(board, turn)
            user_in = input(f"Player {turn}, place your piece: ")

            vm_result = valid_move(user_in, board)
            while not vm_result[1]: 
                user_in = input(f"Incorrect input. Please retry: ")
                vm_result = valid_move(user_in, board)
            position = vm_result[0]

        
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
