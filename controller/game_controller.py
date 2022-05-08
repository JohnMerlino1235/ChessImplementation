from model.game_model import Game
from view.game_view import GameView


class Controller:
    def __init__(self, model: Game):
        self.model = model
        self.view = None

    def set_view(self, view: GameView):
        self.view = view

    def run_game(self):
        game_ended = False

        while not game_ended:
            self.view.display_board()
            self.view.display_curr_player(self.model.curr_player)

            piece_x, piece_y, move_x, move_y = self.get_move()

            if self.model.board[piece_x][piece_y] == 0 \
                    or self.model.board[piece_x][piece_y].color != self.model.curr_player.color:
                self.view.display_illegal_piece

            valid_moves = self.model.board[piece_x][piece_y].get_possible_moves(piece_x, piece_y)

            if (move_x, move_y) not in valid_moves:
                self.view.display_illegal_move()
                piece_x, piece_y, move_x, move_y = self.get_move()

            self.model.make_move(piece_x, piece_y, move_x, move_y)

            if self.model.is_checkmate():
                game_ended = True

            else:
                self.model.change_turn()

        self.view.display_board()
        winner = self.model.get_winner()
        self.view.display_winner(winner)

