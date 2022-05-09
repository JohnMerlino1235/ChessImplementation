from model.player import player_symbol
from view.game_view import GameView


class GameConsoleView(GameView):
    def __init__(self, board, controller: GameView):
        super().__init__(board, controller)

    def display_board(self):
        for j in range(len(self.board)):
            for i in range(len(self.board)):
                if self.board[i][j] == 0:
                    print(" ", end="")
                else:
                    print(self.board[i][j].text_symbol, end="")
            print("")

    def display_curr_player(self, player):
        print(f"Player {player_symbol[player]}'s turn.")

    # i, j -> Previous piece : x, y -> Piece location after move
    def request_move(self, i=None, j=None, x=None, y=None):
        piece = input("Enter the piece you want to move")
        move = input("Enter the location you want to move the piece to")
        return piece, move
"""
    def display_illegal_piece(self):
        print("This is not a valid piece. Try again.")
"""
    def display_illegal_move(self):
        print("This move is illegal. Try again.")

    def display_winner(self, winner):
        if winner != 0:
            print(f'Player {player_symbol[winner]} has won the game! Congratulations!')

    def display_exit(self):
        print("Exiting game")

    def display_score(self, player_one, player_two):
        print("White's Score:", player_one.score)
        print("Black's Score:", player_two.score)
