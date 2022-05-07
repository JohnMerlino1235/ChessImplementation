from model.color import Color
from model.piece import Piece


class Knight(Piece):
    def __init__(self, color: Color):
        self.color = color
        self.text_symbol = None
        self.image = None
        self.update_rep()

    # Updates representation of Pawn based on Color
    def update_rep(self):
        if self.color == Color.BLACK:
            self.text_symbol = '♘'
        else:
            self.text_symbol = '♞'

    # Takes in position of piece and returns list of valid moves based on current board state
    """
    Knights can move ways:
    - Up 2 right 1
    - Up 2 left 1
    - Up 1 right 2
    - Up 1 left 2
    - Down 2 right 1
    - Down 2 left 1
    - Down 1 right 2
    - Down 1 left 2
    - Right 2 up 1
    - Right 2 down 1
    - Right 1 up 2
    - Right 1 down 2
    - Left 2 up 1
    - Left 2 down 1
    - Left 1 up 2
    - Left 1 down 2
    """

    def get_possible_moves(self, i, j):
        valid_moves = []

        valid_moves.append((i + 1, j + 2))  # Up 2 right 1
        valid_moves.append((i - 1, j + 2))  # Up 2 left 1
        valid_moves.append((i + 2, j + 1))  # Up 1 right 2
        valid_moves.append((i - 2, j + 1))  # Up 1 left 2
        valid_moves.append((i + 1, j - 2))  # Down 2 right 1
        valid_moves.append((i - 1, j - 2))  # Down 2 left 1
        valid_moves.append((i + 2, j - 1))  # Down 1 right 2
        valid_moves.append((i - 2, j - 1))  # Down 1 left 2

        return valid_moves
