from tkinter import PhotoImage

from model.color import Color
from model.piece import Piece


class Knight(Piece):
    def __init__(self, color: Color):
        super().__init__(color, 3)

    # Updates representation of Pawn based on Color
    def update_rep(self):
        if self.color == Color.BLACK:
            self.text_symbol = '♘'
            self.image = r"C:\Users\janth\PycharmProjects\ChessImplementation\Piece Images\b_knight_png_256px.png"
        else:
            self.text_symbol = '♞'
            self.image = r"C:\Users\janth\PycharmProjects\ChessImplementation\Piece Images\w_knight_png_256px.png"

    # Takes in position of piece and returns list of valid moves based on current board state
    def get_possible_moves(self, i, j):
        valid_moves = [(i + 1, j + 2), (i - 1, j + 2), (i + 2, j + 1), (i - 2, j + 1), (i + 1, j - 2), (i - 1, j - 2),
                       (i + 2, j - 1), (i - 2, j - 1)]

        for move in valid_moves:
            if move[0] < 0 or move[0] >= 8 or move[1] < 0 or move[1] >= 8:
                valid_moves.remove(move)

        return valid_moves

    def check_move(self, piece_x, piece_y, move_x, move_y, board):
        if board[move_x][move_y] != 0 and board[move_x][move_y].color == self.color:
            return False

        return True
