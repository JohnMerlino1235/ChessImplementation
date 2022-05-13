from enum import IntEnum


class Player:
    def __init__(self, username, color):
        self.username = username
        self.color = color
        # self.elo = update_elo_from_db
        self.score = 0
        self.captured_pieces = []

    def update_captured(self, piece):
        self.score += piece.score
        self.captured_piece.append(piece.text_symbol)

    def receive_move(self, i, j):
        return i, j
