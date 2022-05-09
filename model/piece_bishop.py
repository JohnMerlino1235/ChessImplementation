from model.color import Color
from model.piece import Piece


class Bishop(Piece):
    def __init__(self, color: Color):
        super().__init__(color, 3)

    # Updates representation of Pawn based on Color
    def update_rep(self):
        if self.color == Color.BLACK:
            self.text_symbol = '♗'
        else:
            self.text_symbol = '♝'

    # Takes in position of piece and returns list of valid moves based on current board state
    def get_possible_moves(self, i, j):
        valid_moves = []
        for change in range(13):
            # Up left
            if 0 <= i - (change + 1) < 8 and 0 <= j + (change + 1) < 8:
                valid_moves.append((i - (change + 1), j + (change + 1)))
            # Down left
            if 0 <= i - (change + 1) < 8 and 0 <= j - (change + 1) < 8:
                valid_moves.append((i - (change + 1), j - (change + 1)))
            # Up right
            if 0 <= i + (change + 1) < 8 and 0 <= j + (change + 1) < 8:
                valid_moves.append((i + (change + 1), j + (change + 1)))
            # Down right
            if 0 <= i + (change + 1) < 8 and 0 <= j - (change + 1) < 8:
                valid_moves.append((i + (change + 1), j - (change + 1)))
        return valid_moves

    def check_move(self, piece_x, piece_y, move_x, move_y, board):
        if board[move_x][move_y] != 0 and board[move_x][move_y].color == self.color:
            return False

        if move_x > piece_x and move_y > piece_y:
            up_right = True
        elif move_x > piece_x and move_y < piece_y:
            down_right = True
        elif move_x < piece_x and move_y > piece_y:
            up_left = True
        elif move_x < piece_x and move_y < piece_y:
            down_left = True

        in_between = abs(piece_x - move_x) - 1

        for change in range(in_between):
            if up_right and board[piece_x + (change + 1)][piece_y + (change + 1)] != 0:
                return False
            elif down_right and board[piece_x + (change + 1)][piece_y - (change + 1)] != 0:
                return False
            elif up_left and board[piece_x - (change + 1)][piece_y + (change + 1)] != 0:
                return False
            elif down_left and board[piece_x - (change + 1)][piece_y - (change + 1)] != 0:
                return False

        return True




