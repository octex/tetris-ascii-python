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

    I = (" ▁\n|▁|\n|▁|\n|▁|\n|▁|",
    " ▁ ▁ ▁ ▁\n|▁|▁|▁|▁|") # Cyan

    O = (" ▁ ▁\n|▁|▁|\n|▁|▁|",) # Yellow
    
    T = ("   ▁\n ▁|▁|▁\n|▁|▁|▁|",
        " ▁\n|▁|▁\n|▁|▁|\n|▁|",
        " ▁ ▁ ▁\n|▁|▁|▁|\n  |▁|",
        "   ▁\n ▁|▁|\n|▁|▁|\n  |▁|") # Magenta
    
    S = ("   ▁ ▁\n ▁|▁|▁|\n|▁|▁|",
        " ▁\n|▁|▁\n|▁|▁|\n  |▁|") # Green

    L = (" ▁\n|▁|\n|▁|▁\n|▁|▁|",
        " ▁ ▁ ▁\n|▁|▁|▁|\n|▁|",
        " ▁ ▁\n|▁|▁|\n  |▁|\n  |▁|",
        "     ▁\n ▁ ▁|▁|\n|▁|▁|▁|") # Orange

    Z = (" ▁ ▁\n|▁|▁|▁\n  |▁|▁|",
        "   ▁\n ▁|▁|\n|▁|▁|\n|▁|") # Red

    J = ("   ▁\n  |▁|\n ▁|▁|\n|▁|▁|",
        " ▁\n|▁|▁ ▁\n|▁|▁|▁|",
        " ▁ ▁\n|▁|▁|\n|▁|\n|▁|",
        " ▁ ▁ ▁\n|▁|▁|▁|\n    |▁|") # Blue

    ALL = [I, O, T, S, L, Z, J]
