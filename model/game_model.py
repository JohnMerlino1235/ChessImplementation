import numpy as np

from model.color import Color
from model.piece_bishop import Bishop
from model.piece_king import King
from model.piece_knight import Knight
from model.piece_pawn import Pawn
from model.piece_queen import Queen
from model.piece_rook import Rook
from model.player import Player


class Game:
    def __init__(self):
        # set board -> 0 if no piece, 1 if Black Piece, 2 if White Piece
        self.board = np.zeros((8, 8), dtype = object)
        self.create_board()
        self.curr_player = Player.W

    def create_board(self):
        self.board[0][0] = Rook(Color.BLACK)
        self.board[7][0] = Rook(Color.BLACK)
        self.board[0][7] = Rook(Color.WHITE)
        self.board[7][7] = Rook(Color.WHITE)
        self.board[1][0] = Knight(Color.BLACK)
        self.board[6][0] = Knight(Color.BLACK)
        self.board[1][7] = Knight(Color.WHITE)
        self.board[6][7] = Knight(Color.WHITE)
        self.board[2][0] = Bishop(Color.BLACK)
        self.board[5][0] = Bishop(Color.BLACK)
        self.board[2][7] = Bishop(Color.WHITE)
        self.board[5][7] = Bishop(Color.WHITE)
        self.board[3][0] = Queen(Color.BLACK)
        self.board[3][7] = Queen(Color.WHITE)
        self.board[4][0] = King(Color.BLACK)
        self.board[4][7] = King(Color.WHITE)

        for i in range(8):
            self.board[i][1] = Pawn(Color.BLACK)
            self.board[i][6] = Pawn(Color.WHITE)
