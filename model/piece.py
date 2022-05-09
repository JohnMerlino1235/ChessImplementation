from abc import ABC, abstractmethod
from model.color import Color



class Piece(ABC):
    def __init__(self, color: Color, score: int):
        # color of piece
        super().__init__()
        self.color = color
        self.score = score
        self.text_symbol = None
        self.image = None
        self.update_rep()


    @abstractmethod
    def update_rep(self):
        pass

    @abstractmethod
    def get_possible_moves(self, i, j):
        pass

    @abstractmethod
    def check_move(self, piece_x, piece_y, move_x, move_y, board):

    """
    # global values represent rows and columns on a board

    global row1, row2, row3, row4, row5, row6, row7, row8
    global col1, col2, col3, col4, col5, col6, col7, col8

    row1 = range(0, 8)
    row2 = range(8, 16)
    row3 = range(16, 24)
    row4 = range(24, 32)
    row5 = range(32, 40)
    row6 = range(40, 48)
    row7 = range(48, 56)
    row8 = range(56, 64)

    col1 = range(0, 57, +8)
    col2 = range(1, 58, +8)
    col3 = range(2, 59, +8)
    col4 = range(3, 60, +8)
    col5 = range(4, 61, +8)
    col6 = range(5, 62, +8)
    col7 = range(6, 63, +8)
    col8 = range(7, 64, +8)
class Queen(Piece):

    Object Representing a Queen

    - Can move up to 8 spaces diagonally
    - Can move up to 8 spaces horizontally or vertically


    black_text = '♕'
    # black_image =

    white_text = '♛'
    # white_image =


class King(Piece):
    
    Object Representing a King

    - Can move 1 space to any surrounding spaces
    

    black_text = '♔'
    # black_image =

    white_text = '♚'
    # white_image =

    
    WPawn, BPawn = 1
    WKnight, BKnight, WBishop, BBishop = 3
    WRook, BRook = 5
    WQueen, BQueen = 10
    WKing, BKing = 100


piece_symbol = {
    Piece.WPawn: '♟',
    Piece.BPawn: '♙',
    Piece.WKnight: '♞',
    Piece.BKnight: '♘',
    Piece.WBishop: '♝',
    Piece.BBishop: '♗',
    Piece.WRook: '♜',
    Piece.BRook: '♖',
    Piece.WQueen: '♛',
    Piece.BQueen: '♕',
    Piece.WKing: '♚',
    Piece.BKing: '♔'
}
"""
