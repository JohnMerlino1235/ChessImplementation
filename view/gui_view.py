import random
import time
import tkinter as tk
import tkinter.messagebox
from tkinter import messagebox

# from controller.game_controller import Controller
from model.color import Color
from model.game_model import Game
from model.player import Player
from PIL import Image, ImageTk

from view.game_view import GameView


class GUIView(tk.Tk):
    def __init__(self, game_controller: Controller, model: Game):
        self.game_controller = game_controller
        tk.Tk.__init__(self)
        self.model = model
        self.title("Chess")
        self.container = tk.Frame(self, width=(75 * 8), height=(75 * 9))
        self.container.pack(side="top", fill="both", expand=True)
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage, MainPage, PlayPage):
            page_name = F.__name__
            if F == PlayPage:
                frame = F(parent=self.container, controller=self, board=self.model)
                self.frames[page_name] = frame
                frame.grid(row=0, column=0, sticky="nsew")
            else:
                frame = F(parent=self.container, controller=self)
                self.frames[page_name] = frame
                frame.grid(row=0, column=0, sticky="nsew")

        self.change_page("LoginPage")

    def change_page(self, page_name, player=None, turn=None, model=None):
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "PlayPage":
            frame.start_game(player, turn, model)
            frame.display_board()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        username_label = tk.Label(self, text="Username:")
        username_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        username_entry = tk.Entry(self)
        username_entry.grid(row=0, column=1, sticky=tk.E, padx=5, pady=5)
        password_label = tk.Label(self, text="Password:")
        password_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        password_entry = tk.Entry(self)
        password_entry.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)
        login_button = tk.Button(
            self,
            text="Login",
            width=10,
            command=lambda: [
                self.login_verify(username_entry.get(), password_entry.get())
            ],
        )
        login_button.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

        guest_button = tk.Button(
            self, text="Play as Guest", width=10, command=lambda: self.guest_play()
        )
        guest_button.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

        register_button = tk.Button(
            self,
            text="Sign Up",
            width=20,
            command=lambda: controller.change_page("RegisterPage"),
        )
        register_button.grid(row=2, column=3, sticky=tk.W, padx=5, pady=5)

    def guest_play(self):
        self.controller.game_controller.model.player_white = Player(
            "Guest", Color.WHITE
        )
        self.controller.change_page("MainPage")


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        label = tk.Label(self, text="Main Page")
        label.pack(side="top", pady=10)
        play_button = tk.Button(
            self, text="Play Game", command=lambda: controller.change_page("PlayPage")
        )
        settings_button = tk.Button(
            self,
            text="Settings",
            command=lambda: controller.change_page("SettingsPage"),
        )
        leaderboard_button = tk.Button(
            self,
            text="View Leaderboard",
            command=lambda: controller.change_page("LeaderboardPage"),
        )
        login_page_button = tk.Button(
            self, text="Sign out", command=lambda: self.sign_out()
        )
        exit_button = tk.Button(self, text="Exit", command=lambda: self.close())
        play_button.pack(pady=5)
        settings_button.pack(pady=5)
        leaderboard_button.pack(pady=5)
        login_page_button.pack(pady=5)
        exit_button.pack(pady=5)


class PlayPage(tk.Frame, GameView):
    def __init__(self, parent, controller, board=None):
        tk.Frame.__init__(self, parent)
        GameView.__init__(self, board, controller.game_controller)
        self.parent = parent
        self.controller = controller
        self.board = board
        self.board_size = board.shape[0]
        self.buttons = [
            [0 for x in range(self.board_size)] for y in range(self.board_size)
        ]
        exit_button = tk.Button(
            self, text="Exit Game", command=lambda: self.display_exit()
        )
        self.invalid_move_label = tk.Label(
            self, text="Invalid move.\nTry again.", fg="red"
        )
        for i in range(self.board_size):
            self.rowconfigure(i, minsize=60)
            self.columnconfigure(i, minsize=60)
        self.set_buttons()
        self.curr_player = tk.Label(self, text=f"Current Player:")
        self.curr_player.grid(row=self.board_size + 1, column=self.board_size + 1)
        exit_button.grid(row=self.board_size + 1, column=0, sticky="nsew")

    def display_board(self):
        player_white = self.controller.game_controller.model.player_white
        player_black = self.controller.game_controller.model.player_black
        self.invalid_move_label.grid_forget()
        for j in range(self.board_size):
            for i in range(self.board_size):
                if self.board[i][j] != 0:
                    photo = Image.open(self.board[i][j].image)
                    resized_photo = photo.resize((45, 45))
                    photo2 = ImageTk.PhotoImage(resized_photo)
                    self.buttons[i][j].configure(image=photo2)
                    self.buttons[i][j].configure(self.request_move(i, j, None, None))
        self.update()

        """
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == player_one.num and self.buttons[i][j].cget(
                        'bg') != self.controller.game_controller.model.get_player(self.board[i][j]).color.value:
                    self.buttons[i][j].configure(bg=player_one.color.value)
                    self.buttons[i][j].configure(command=None)
                elif self.board[i][j] == player_two.num and self.buttons[i][j].cget(
                        'bg') != self.controller.game_controller.model.get_player(self.board[i][j]).color.value:
                    self.buttons[i][j].configure(bg=player_two.color.value)
                    self.buttons[i][j].configure(command=None)
                    """

    def display_curr_player(self, player):
        pass

    def display_exit(self):
        pass

    def display_illegal_move(self):
        pass

    def display_no_legal_moves(self, player):
        pass

    def display_winner(self, winner):
        pass

    def start_game(self, player, turn, board=None):
        if board:
            self.board = board
        self.controller.game_controller.reset_game(player, self.board_size, board, turn)
        self.board = self.controller.game_controller.model.board
        self.display_board()
        self.display_curr_player(self.controller.game_controller.model.curr_player)

    def request_move(self, i=None, j=None, x=None, y=None):
        pass

    def set_buttons(self):
        for j in range(self.board_size):
            for i in range(self.board_size):
                if i % 2 == 0:
                    if j % 2 == 0:
                        background = "white smoke"
                    else:
                        background = "green"
                else:
                    if j % 2 == 0:
                        background = "green"
                    else:
                        background = "white smoke"
                button = 0
                self.buttons.append(button)
                self.buttons[i][j] = tk.Button(
                    self,
                    image=None,
                    bg=background,
                    command=lambda i=i, j=j: self.request_move(i, j, None, None),
                )
                self.buttons[i][j].grid(row=j, column=i, sticky="nsew")


if __name__ == "__main__":
    game = Game()
    # controller = Controller(game)
    game_view = GUIView(controller, game.board)
    controller.set_view(game_view.frames["PlayPage"])

    game_view.mainloop()
