# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from controller.game_controller import Controller
from model.color import Color
from model.game_model import Game
from model.piece_bishop import Bishop
from model.piece_knight import Knight
from model.piece_pawn import Pawn
from model.piece_rook import Rook
from view.console_view import GameConsoleView
from view.game_view import GameView


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chess = Game()
    controller = Controller(chess)
    view = GameConsoleView(chess, controller)
    controller.set_view(view)
    controller.run_game()