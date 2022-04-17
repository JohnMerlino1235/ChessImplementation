from model.player import player_symbol
from view.game_view import GameView

class GameConsoleView(GameView):
    def __init__(self, board, controller: GameView):
        super().__init__(board, controller)

    def display_board(self):

    def display_curr_player(self, player):
        print(f"Player {player_symbol[player]}'s turn.")

    def request_move(self, i = None, j = None, piece = None):
        move = input("Enter your move (")

    def display_illegal_move(self):

    def display_no_legal_moves(self, player):

    def display_winner(self, winner):
        if winner != 0:
            print (f'Player {player_symbol[winner]} has won the game! Congratulations!')




    def display_exit(self):
        print("Exiting game")
