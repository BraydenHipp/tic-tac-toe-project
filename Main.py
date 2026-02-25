import sys

from Board import Board
from Player import Player


def main():
    my_board = Board()


    print("Welcome to TicTacToe")
    print("Below, each number corresponds to a location on the board."
          " To move your piece there just enter that number")

    my_board.print_matrix(my_board.game_board)

    print("Player 1 Please Enter Your Name")
    player_one_name = input()

    print("Player 2 Please Enter Your Name")
    player_two_name = input()

    # Player 1 is X and goes first
    # Player 2 is O and goes second
    player_one = Player(player_one_name, 1, "X", 0)
    player_two = Player(player_two_name, 2, "O", 0)

    print("Game Starting")


    my_board.print_matrix(my_board.display_board)


    # Player turn are controlled by these two variables
    player_one_turn = True
    player_two_turn = False

    play_again = True

    while play_again: # Contains main game flow logic
        move = 0

        if player_one_turn:
            print("Player One Make Your Move")
            while True:
                try:
                    player_one_move = input()
                    move = int(player_one_move)
                    if 1 <= move <= 9 and move in my_board.available_moves: # Check number is between 1-9 and available
                        my_board.available_moves.remove(move)
                        break
                    else:
                        print("Please Enter A Number 1 - 9 That Isn't Already Taken")
                except ValueError:
                    print("Please Enter A Valid Number")

        # Print the display board
        my_board.update_display_board(move, player_one.piece)
        my_board.print_matrix(my_board.display_board)

        # Update Game Board
        my_board.update_game_board(move, player_one.piece)

        # Swap Player Control
        player_one_turn = False
        player_two_turn = True


        # Check Winner
        if my_board.winner(player_one.piece) == True or my_board.winner(player_two.piece) == True:
            if my_board.winner(player_one.piece):
                player_one.win_count += 1
                print(f"{player_one.name} WINS!")
            if my_board.winner(player_two.piece):
                player_two.win_count += 1
                print(f"{player_two.name} WINS!")

            print("Would you like to play again?")
            print("Enter 'Y' to play again.")
            print("Enter 'N' to quit")

            while True:
                yes_or_no = input()
                if yes_or_no == "N":
                    sys.exit()
                elif yes_or_no == "Y":
                    # Clear game and display board and print out score and reset available moves
                    my_board.clear_game_board()
                    my_board.clear_display_board()
                    my_board.reset_available_moves()
                    print(f"Current Score is\n {player_one.name}: {player_one.win_count}"
                          f" \n {player_two.name}: {player_two.win_count}")
                    break
                else:
                    print("Please Enter Y/N")


        if player_two_turn:
            print("Player Two Make Your Move")
            while True:
                try:
                    player_two_move = input()
                    move = int(player_two_move)
                    if 1 <= move <= 9 and move in my_board.available_moves:
                        my_board.available_moves.remove(move)
                        break
                    else:
                        print("Please Enter A Number 1 - 9 That Isn't Already Taken")
                except ValueError:
                    print("Please Enter A Valid Number")
        # Print Display Board
        my_board.update_display_board(move, player_two.piece)
        my_board.print_matrix(my_board.display_board)

        # Update Game Board
        my_board.update_game_board(move, player_two.piece)

        # Check Winner
        if my_board.winner(player_one.piece) == True or my_board.winner(player_two.piece) == True:
            if my_board.winner(player_one.piece):
                player_one.win_count += 1
                print(f"{player_one.name} WINS!")
            if my_board.winner(player_two.piece):
                player_two.win_count += 1
                print(f"{player_two.name} WINS!")

            print("Would you like to play again?")
            print("Enter 'Y' to play again.")
            print("Enter 'N' to quit")

            while True:
                yes_or_no = input()
                if yes_or_no == "N":
                    sys.exit()
                elif yes_or_no == "Y":
                    # Clear game and display board and print out score
                    my_board.clear_game_board()
                    my_board.clear_display_board()
                    my_board.reset_available_moves()
                    print(f"Current Score is\n {player_one.name}: {player_one.win_count}"
                          f" \n {player_two.name}: {player_two.win_count}")
                    break
                else:
                    print("Please Enter Y/N")

        # Swap Player Control
        player_one_turn = True
        player_two_turn = False


if __name__ == "__main__":
    main()
