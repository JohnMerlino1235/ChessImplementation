# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from model.color import Color
from model.game_model import Game
from model.piece_bishop import Bishop
from model.piece_knight import Knight
from model.piece_pawn import Pawn
from model.piece_rook import Rook


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    board = Game()
    print(" 0 1 2 3 4 5 6 7 ")
    for x in range(8):
        print(x, end="")
    print("")
    for j in range(8):
        print(j, end="")
        for i in range(8):
            if board.board[i][j] != 0:
                print(board.board[i][j].text_symbol, end="")
            else:
                print(" ", end="")
        print("")
