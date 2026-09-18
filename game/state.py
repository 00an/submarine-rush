from enum import Enum


class GameState(Enum):
    MAIN = "main"
    BOATS = "boats"
    CONTROLS = "controls"
    CREDITS = "credits"
    SETTINGS = "settings"