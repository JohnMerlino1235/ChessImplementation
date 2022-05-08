from model.color import Color
from model.piece import Piece


class Queen(Piece):
    def __init__(self, color: Color):
        super().__init__(color, 10)

    # Updates representation of Pawn based on Color
    def update_rep(self):
        if self.color == Color.BLACK:
            self.text_symbol = '♕'
        else:
            self.text_symbol = '♛'

    # Takes in position of piece and returns list of valid moves based on current board state
    def get_possible_moves(self, i, j):
        valid_moves = []
        for change in range(14):
            # Going Up
            if 0 <= i < 8 and 0 <= j + (change + 1) < 8:
                valid_moves.append((i, j + (change + 1)))
            # Going Left
            if 0 <= i - (change + 1) < 8 and 0 <= j < 8:
                valid_moves.append((i - (change + 1), j))
            # Going Right
            if 0 <= i + (change + 1) < 8 and 0 <= j < 8:
                valid_moves.append((i + (change + 1), j))
            # Going Down
            if 0 <= i < 8 and 0 <= j - (change + 1) < 8:
                valid_moves.append((i, j - (change + 1)))
        for change in range(13):
            # Top Left
            if 0 <= i - (change + 1) < 8 and 0 <= j + (change + 1) < 8 \
                    and (i - (change + 1), j + (change + 1)) not in valid_moves:
                valid_moves.append((i - (change + 1), j + (change + 1)))
            # Bottom left
            if 0 <= i - (change + 1) < 8 and 0 <= j - (change + 1) < 8 \
                    and (i - (change + 1), j - (change + 1)) not in valid_moves:
                valid_moves.append((i - (change + 1), j - (change + 1)))
            # Top Right
            if 0 <= i + (change + 1) < 8 and 0 <= j + (change + 1) < 8 \
                    and (i + (change + 1), j + (change + 1)) not in valid_moves:
                valid_moves.append((i + (change + 1), j + (change + 1)))
            # Bottom Right
            if 0 <= i + (change + 1) < 8 and 0 <= j - (change + 1) < 8 \
                    and (i - (change + 1), j - (change + 1)) not in valid_moves:
                valid_moves.append((i + (change + 1), j - (change + 1)))
        return valid_moves


