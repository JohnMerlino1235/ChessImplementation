# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from model.color import Color
from model.piece_bishop import Bishop
from model.piece_knight import Knight
from model.piece_pawn import Pawn
from model.piece_rook import Rook


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    white_pawn = Pawn(Color.WHITE)
    print(white_pawn.get_possible_moves(1, 6))
    print(white_pawn.score)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
