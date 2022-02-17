

class Blocks:
    BASE = "#"

    I = (" _\n|_|\n|_|\n|_|\n|_|",
    " _ _ _ _\n|_|_|_|_|")

    O = (" _ _\n|_|_|\n|_|_|")
    
    T = ("   _\n _|_|_\n|_|_|_|\n",
        " _\n|_|_\n|_|_|\n|_|",
        " _ _ _\n|_|_|_|\n  |_|",
        "   _\n _|_|\n|_|_|\n  |_|")
    
    S = ("   _ _\n _|_|_|\n|_|_|\n",
        " _\n|_|_\n|_|_|\n  |_|")

    L = (" _\n|_|\n|_|_\n|_|_|",
        " _ _ _\n|_|_|_|\n|_|\n",
        " _ _\n|_|_|\n  |_|\n  |_|",
        "     _\n _ _|_|\n|_|_|_|")

    Z = (" _ _\n|_|_|_\n  |_|_|",
        "   _\n _|_|\n|_|_|\n|_|")

    J = ("   _\n  |_|\n _|_|\n|_|_|",
        " _\n|_|_ _\n|_|_|_|",
        " _ _\n|_|_|\n|_|\n|_|",
        " _ _ _\n|_|_|_|\n    |_|")

    ALL = [I, O, T, S, L, Z, J]


class Block:
    def __init__(self, x, y, animations):
        self.x = x
        self.y = y
        self.animations = animations
        self.current_index = 0
        self.sprite = self.animations[self.current_index]

    def get_idle(self):
        return self.idle

    def rotate(self):
        if self.current_index == len(self.animations):
            self.current_index = 0
        else:
            self.current_index += 1
        self.sprite = self.animations[self.current_index]
