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
        pass