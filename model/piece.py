from enum import IntEnum


class Piece(IntEnum):
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
