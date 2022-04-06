import numpy as np
from model.player import Player


class Game:
    def __init__(self):
        # set board -> 0 if no piece, 1 if Black Piece, 2 if White Piece
        self.board = np.zeros((8, 8), d_type=np.int)
        # board with pieces -> object types
        self.pieces = 0
        self.curr_player = Player.W
