class Board:
    # 2d array that represents the tic tac toe board 7 x 7 2d array purely for display

    display_board = [
        ["_", "_", "_", "_", "_", "_", "_"],
        ["|", " ", "|", " ", "|", " ", "|"],
        ["-", "-", "-", "-", "-", "-", "-"],
        ["|", " ", "|", " ", "|", " ", "|"],
        ["-", "-", "-", "-", "-", "-", "-"],
        ["|", " ", "|", " ", "|", " ", "|"],
        ["-", "-", "-", "-", "-", "-", "-"],
    ]
    # 2d array used for keeping track of the player's pieces
    # And for calculating the winner or draw
    game_board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ]

    available_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # method to reset available moves
    def reset_available_moves(self):
        self.available_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self):
        self.display_board = Board.display_board
        self.game_board = Board.game_board

    # Method to print the game board and display board
    def print_matrix(self, matrix):
        for row in matrix:
            print(" ".join(row))
        print()

    # Method to update the display board
    # Location will be a number between 1 - 9 always
    # Piece will either be "X" or "O"
    def update_display_board(self, location, piece):
        if location == 1:
            self.display_board[1][1] = piece
        elif location == 2:
            self.display_board[1][3] = piece
        elif location == 3:
            self.display_board[1][5] = piece
        elif location == 4:
            self.display_board[3][1] = piece
        elif location == 5:
            self.display_board[3][3] = piece
        elif location == 6:
            self.display_board[3][5] = piece
        elif location == 7:
            self.display_board[5][1] = piece
        elif location == 8:
            self.display_board[5][3] = piece
        elif location == 9:
            self.display_board[5][5] = piece

    # TODO
    # Method to update game board for proper winner testing
    # Location will always be 1 - 9
    def update_game_board(self, location, piece):
        if location == 1:
            self.game_board[0][0] = piece
        elif location == 2:
            self.game_board[0][1] = piece
        elif location == 3:
            self.game_board[0][2] = piece
        elif location == 4:
            self.game_board[1][0] = piece
        elif location == 5:
            self.game_board[1][1] = piece
        elif location == 6:
            self.game_board[1][2] = piece
        elif location == 7:
            self.game_board[2][0] = piece
        elif location == 8:
            self.game_board[2][1] = piece
        elif location == 9:
            self.game_board[2][2] = piece



    # Method to Clear Game Board
    def clear_game_board(self):
        for row in range(0, len(self.game_board)):
            for col in range(0, len(self.game_board[0])):
                self.game_board[row][col] = " "

    # Method to Clear Display Board

    def clear_display_board(self):
        self.display_board[1][1] = " "
        self.display_board[1][3] = " "
        self.display_board[1][5] = " "
        self.display_board[3][1] = " "
        self.display_board[3][3] = " "
        self.display_board[3][5] = " "
        self.display_board[5][1] = " "
        self.display_board[5][3] = " "
        self.display_board[5][5] = " "

    # Method to check if there is a winner
    # Takes a piece as a parameter (X or O)
    def winner(self, piece):
        # Check horizontally across top
        if ((self.game_board[0][0] == self.game_board[0][1]) and (self.game_board[0][0] == self.game_board[0][2])
                and (self.game_board[0][0] == piece)):
            return True
        # Check horizontally across middle
        elif (self.game_board[1][0] == self.game_board[1][1]) and (self.game_board[1][0] == self.game_board[1][2]) \
                and (self.game_board[1][0] == piece):
            return True
        # Check horizontally across bottom
        elif (self.game_board[2][0] == self.game_board[2][1]) and (self.game_board[2][0] == self.game_board[2][2]) \
                and (self.game_board[2][0] == piece):
            return True
        # Check vertically across left side
        elif (self.game_board[0][0] == self.game_board[1][0]) and (self.game_board[0][0] == self.game_board[2][0]) \
                and (self.game_board[0][0] == piece):
            return True
        # Check vertically across middle
        elif (self.game_board[0][1] == self.game_board[1][1]) and (self.game_board[0][1] == self.game_board[2][1]) \
                and (self.game_board[0][1] == piece):
            return True
        # Check vertically across right side
        elif (self.game_board[0][2] == self.game_board[1][2]) and (self.game_board[0][2] == self.game_board[2][2]) \
                and (self.game_board[0][2] == piece):
            return True
        # Check diagonal top left to bottom right
        elif (self.game_board[0][0] == self.game_board[1][1]) and (self.game_board[0][0] == self.game_board[2][2]) \
                and (self.game_board[0][0] == piece):
            return True
        # Check diagonal top right to bottom left
        elif (self.game_board[0][2] == self.game_board[1][1]) and (self.game_board[0][2] == self.game_board[2][0]) \
                and (self.game_board[0][2] == piece):
            return True
        else:
            return False
