

class Blocks:
    BASE = "#"

    I = (" _\n|_|\n|_|\n|_|\n|_|",
    " _ _ _ _\n|_|_|_|_|")

    O = (" _ _\n|_|_|\n|_|_|",)
    
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
        self.coords = self.generate_coords()

    def rotate(self):
        if self.current_index == len(self.animations) - 1:
            self.current_index = 0
        else:
            self.current_index += 1
        self.sprite = self.animations[self.current_index]
        self.coords = self.generate_coords()
    def generate_coords(self):
        coords = []
        sprite_splitted = self.sprite.replace(' ', '').split('\n')
        t_x = self.x
        t_y = self.y
        base_x = t_x
        for line in sprite_splitted:
            new_coords = []
            for char in line:
                coord = (t_x, t_y)
                t_x += 1
                new_coords.append(coord)
            coords.append(new_coords)
            t_y += 1
            t_x = base_x
        return coords
    def is_coord_of_block(self, x, y):
        for coord in self.coords:
            for _coord in coord:
                if _coord[0] == x and _coord[1] == y:
                    return True
        return False