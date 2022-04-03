from enum import IntEnum

class Player(IntEnum):
    B = 1
    W = 2

player_symbol = {
    Player.B: 'black',
    Player.W: 'white'
}