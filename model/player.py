from enum import IntEnum


class Player:
    def __init__(self, username, color):
        self.username = username
        self.color = color
        # self.elo = update_elo_from_db
        self.score = 0

    def update_score(self, change):
        self.score += change
