from view.game_view import GameView


class GameConsoleView(GameView):
    def __init__(self, board, controller):
        super().__init__(board, controller)

    def display_board(self):
        for j in range(len(self.board.board)):
            for i in range(len(self.board.board)):
                if self.board.board[i][j] == 0:
                    print(" ", end="")
                else:
                    print(self.board.board[i][j].text_symbol, end="")
            print("")

    def display_curr_player(self, player):
        print(f"Player {player.color}'s turn.")

    def request_piece(self, i=None, j=None):
        piece = input("Enter the piece you want to move:")
        return piece

    # i, j -> Previous piece : x, y -> Piece location after move
    def request_move(self, i=None, j=None, x=None, y=None):
        move = input("Enter the location you want to move the piece to:")
        return move

    def display_illegal_move(self):
        print("This move is illegal. Try again.")

    def display_winner(self, winner):
        if winner != 0:
            print(f'Player {winner.color} has won the game! Congratulations!')

    def display_no_legal_moves(self, player):
        if self.model.is_checkmate(player):
            print(f'Player {player.color} has been checkmated!')

    def display_exit(self):
        print("Exiting game")

    def display_score(self, player_white, player_black):
        print("White's Score:", player_white.score)
        print("Captured by White:", end="")
        for white_captured in player_white.captured_pieces:
            print(white_captured.text_symbol, end="")
        print("")
        print("Black's Score:", player_black.score)
        print("Captured by Black:", end="")
        for black_captured in player_black.captured_pieces:
            print(black_captured.text_symbol, end="")
        print("")

    """
        def display_illegal_piece(self):
            print("This is not a valid piece. Try again.")
    """
