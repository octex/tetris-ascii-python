import curses


class GameState:
    READY = 0
    RUNNING = 1
    CLEARING = 2
    GAMEOVER = 3
    PAUSED = 4


class Constants:
    HIGH_FRAMES = 0.5
    LOW_FRAMES = 0.15
    COLORS = [curses.COLOR_BLACK,
              curses.COLOR_BLUE,
              curses.COLOR_GREEN,
              curses.COLOR_CYAN,
              curses.COLOR_RED,
              curses.COLOR_MAGENTA,
              curses.COLOR_YELLOW,
              curses.COLOR_WHITE]

class Blocks:
    BASE = "#"

    # Source of color palette: https://en.wikipedia.org/wiki/Tetris

    I = (" _\n|_|\n|_|\n|_|\n|_|",
    " _ _ _ _\n|_|_|_|_|") # Cyan

    O = (" _ _\n|_|_|\n|_|_|",) # Yellow
    
    T = ("   _\n _|_|_\n|_|_|_|",
        " _\n|_|_\n|_|_|\n|_|",
        " _ _ _\n|_|_|_|\n  |_|",
        "   _\n _|_|\n|_|_|\n  |_|") # Magenta
    
    S = ("   _ _\n _|_|_|\n|_|_|",
        " _\n|_|_\n|_|_|\n  |_|") # Green

    L = (" _\n|_|\n|_|_\n|_|_|",
        " _ _ _\n|_|_|_|\n|_|",
        " _ _\n|_|_|\n  |_|\n  |_|",
        "     _\n _ _|_|\n|_|_|_|") # Orange

    Z = (" _ _\n|_|_|_\n  |_|_|",
        "   _\n _|_|\n|_|_|\n|_|") # Red

    J = ("   _\n  |_|\n _|_|\n|_|_|",
        " _\n|_|_ _\n|_|_|_|",
        " _ _\n|_|_|\n|_|\n|_|",
        " _ _ _\n|_|_|_|\n    |_|") # Blue

    ALL = [I, O, T, S, L, Z, J]