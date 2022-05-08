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

    def play_turn(self, piece_x, piece_y, move_x, move_y):

    def get_move(self):
        move = [0]
        valid = False
        while len(move) != 2 and not valid:
            move = self.model.curr_player.receive_move()
            if move == "exit":
                return [(-1, -1), (-1, -1)]
            try:
                piece = move[0].split(',')
                piece_x = int(piece[0])
                piece_y = int(piece[1])
                move = move[1].split(',')
                move_x = int(move[0])
                move_y = int(move[1])
                valid = True
            except (ValueError, IndexError) as e:
                self.view.display_illegal_move
                move = [0]
                continue

        return piece_x, piece_y, move_x, move_y

    def update_board(self):
        self.view.display_board()

        if not self.model.is_checkmate():
            self.view.display_curr_player(self.model.curr_player)
        else:
            self.game_over()

    def game_over(self):
        self.view.display_board()
        # self.model.update_elo(self.model.get_winner())
        self.view.display_winner(self.model.get_winner())

