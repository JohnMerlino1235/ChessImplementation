from model.color import Color
from model.piece import Piece


class Rook(Piece):
    def __init__(self, color: Color):
        super().__init__(color, 5)

    # Updates representation of Pawn based on Color
    def update_rep(self):
        if self.color == Color.BLACK:
            self.text_symbol = '♖'
        else:
            self.text_symbol = '♜'

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
        return valid_moves

    def check_move(self, piece_x, piece_y, move_x, move_y, board):
        if board[move_x][move_y].color == self.color:  # board[move_x][move_y] != 0 and board[move_x][move_y].color == self.color:
            return False

        if move_x > piece_x:
            right = True
        elif move_x < piece_x:
            left = True
        elif move_y > piece_y:
            up = True
        elif move_y < piece_y:
            down = True

        if right or left:
            in_between = abs(piece_x - move_x) - 1
        elif up or down:
            in_between = abs(piece_y - move_y) - 1

        for change in range(in_between):
            if right and board[piece_x + (change + 1)][piece_y] != 0:
                return False

            elif left and board[piece_x - (change + 1)][piece_y] != 0:
                return False

            elif up and board[piece_x][piece_y + (change + 1)] != 0:
                return False

            elif down and board[piece_x][piece_y - (change + 1)] != 0:
                return False

        return True
