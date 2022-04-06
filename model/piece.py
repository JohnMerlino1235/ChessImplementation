class Piece:
    def __init__(self, color, piece_set):
        # color of piece

        self.color = color
        self.piece_set = piece_set.append(self)
        self.text_rep = None
        self.image_rep = None

    captured = False

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


class Pawn(Piece):
    """
    Object Representing a Pawn

    - If not moved at all, can move forward one or two spaces
    - If previously moved, can move forward one space
    - If going to capture, can capture forward-left, forward-right
    """
    black_text = '♙'
    # black_image =

    white_text = '♟'
    # white_image =


class Knight(Piece):
    """
    Object Representing a Knight

    - Can move 2 spaces forward / backward and 1 space left / right
    - Can move 1 space forward / backward and 2 spaces left / right
    """

    black_text = '♘'
    # black_image =

    white_text = '♞'
    # white_image =


class Bishop(Piece):
    """
    Object Representing a Bishop

    - Can move up to 8 spaces diagonally
    """

    black_text = '♗'
    # black_image =

    white_text = '♝'
    # white_image =


class Rook(Piece):
    """
    Object Representing a Rook

    - Can move up to 8 spaces horizontally or vertically
    """

    black_text = '♖'
    # black_iamge =

    white_text = '♜'
    # white_image =


class Queen(Piece):
    """
    Object Representing a Queen

    - Can move up to 8 spaces diagonally
    - Can move up to 8 spaces horizontally or vertically
    """

    black_text = '♕'
    # black_image =

    white_text = '♛'
    # white_image =


class King(Piece):
    """
    Object Representing a King

    - Can move 1 space to any surrounding spaces
    """

    black_text = '♔'
    # black_image =

    white_text = '♚'
    # white_image =

    """
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
