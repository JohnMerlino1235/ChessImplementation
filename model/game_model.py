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
        # set board -> 0 if no piece, Piece Object if Piece
        self.board = np.zeros((8, 8), dtype=object)
        self.create_board()
        self.player_white = Player("White", Color.WHITE)
        self.player_black = Player("Black", Color.BLACK)
        self.curr_player = self.player_white

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

    def is_legal_move(self, piece_x, piece_y, move_x, move_y):
        if self.board[piece_x][piece_y] == 0:
            return False
        if self.board[piece_x][piece_y].color != self.curr_player.color:
            return False

        valid_moves = self.board[piece_x][piece_y].get_possible_moves(piece_x, piece_y)

        if not valid_moves:
            return False

        if (move_x, move_y) not in valid_moves:
            return False

        return self.board[piece_x][piece_y].check_move(piece_x, piece_y, move_x, move_y, self.board)

    def make_move(self, piece_x, piece_y, move_x, move_y):
        if self.board[move_x][move_y] != 0:
            captured_piece = self.board[move_x][move_y]
            # Update score
            self.curr_player.update_captured(captured_piece)
            # add captured piece to current player's captured piece array
            # self.curr_player.captured_pieces(captured_piece)
        self.board[move_x][move_y] = self.board[piece_x][piece_y]
        self.board[piece_x][piece_y] = 0

    def change_turn(self):
        if self.curr_player == self.player_white:
            self.curr_player = self.player_black
        else:
            self.curr_player = self.player_white

"""
    def is_checkmate(self, player):
        if self.is_attacked(piece_x, piece_y):
            return self.board[piece_x][piece_y].get_possible_moves(piece_x, piece_y)
"""




