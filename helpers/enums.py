import enum


class StateOfGame(enum.Enum):
    EXIT = 1
    START_WINDOW = 2
    INPUT = 3
    REGISTRATION = 4
    MENU = 5
    ROOM = 6
    PLAYER_CHOOSE = 7
    CHOOSING_HERO = 8
    TREE_PLAYER = 9
    TREE_PLAYER1 = 10
    INPUT_ROOM = 11
    CREATE_ROOM = 12
    GAME_ROOM = 13
