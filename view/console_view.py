from model.player import player_symbol
from view.game_view import GameView

class GameConsoleView(GameView):
    def __init__(self, board, controller: GameView):
        super().__init__(board, controller)

    def display_board(self):
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if self.board[x][y] == 0:
                    print("_")
                else:
                    print(self.board[x][y].symbol)


    def display_curr_player(self, player):
        print(f"Player {player_symbol[player]}'s turn.")

    # i, j -> Previous piece : x, y -> Piece location after move
    def request_move(self, i = None, j = None, x = None, y = None):
        move = input("Enter your move (")

    def display_illegal_move(self):

    def display_no_legal_moves(self, player):

    def display_winner(self, winner):
        if winner != 0:
            print (f'Player {player_symbol[winner]} has won the game! Congratulations!')




    def display_exit(self):
        print("Exiting game")
