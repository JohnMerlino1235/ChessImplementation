from model.color import Color
from model.piece import Piece


class Pawn(Piece):
    def __init__(self, color: Color):
        self.color = color
        self.text_symbol = None
        self.image = None
        self.update_rep()

    # Updates representation of Pawn based on Color
    def update_rep(self):
        if self.color == Color.BLACK:
            self.text_symbol = '♙'
        else:
            self.text_symbol = '♟'

    # Takes in position of piece and returns list of valid moves based on current board state
    def get_possible_moves(self, i, j):
        valid_moves = []
        """
        Pawns can have a max amount of 4 moves:
        - Move forward twice if at starting square
        - Move forward once
        - Capture up 1 left 1
        - Capture up 1 right 1
        """
        # Check to see if pawn is unmoved and in starting spot based on color
        if self.color == Color.BLACK:
            # If BlackPawn is at starting row
            if i == 1:
                valid_moves.append((i, j + 2))
            valid_moves.append((i, j + 1))
            valid_moves.append((i + 1, j + 1))
            valid_moves.append((i - 1, j + 1))
        if self.color == Color.WHITE:
            # If WhitePawn is at starting row
            if i == 6:
                valid_moves.append((i, j + 2))
            valid_moves.append((i, j - 1))
            valid_moves.append((i + 1, j - 1))
            valid_moves.append((i - 1, j - 1))

        return valid_moves
