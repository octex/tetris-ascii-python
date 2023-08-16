

class Blocks:
    BASE = "#"

    I = (" _\n|_|\n|_|\n|_|\n|_|",
    " _ _ _ _\n|_|_|_|_|")

    O = (" _ _\n|_|_|\n|_|_|",)
    
    T = ("   _\n _|_|_\n|_|_|_|",
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
    
    def update_pos(self, x, y):
        self.x = x
        self.y = y

    def generate_coords(self):
        coords = []
        sprite_splitted = self.sprite.split('\n')
        t_x = self.x
        t_y = self.y
        base_x = t_x
        for line in sprite_splitted:
            new_coords = []
            for char in line:
                if char != ' ':
                    coord = (t_x, t_y)
                    new_coords.append(coord)
                t_x += 1
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

    def get_coords(self):
        return self.coords

class Board:
    def __init__(self, board_length):
        self.board = []
        self.board_length = board_length

    def print_board(self, new_frame=None):
        if new_frame:
            self.board = new_frame
        for y in range(self.board_length):
            for x in range(self.board_length):
                print(self.board[y][x], end='')
            print()
        print(' ', end='')
        print(f"{Blocks.BASE} "*9)
    
    def load_board(self):
        for _y in range(self.board_length):
            new_line = []
            new_line.append(Blocks.BASE)
            for _x in range(self.board_length - 2):
                new_line.append(' ')
            new_line.append(Blocks.BASE)
            self.board.append(new_line)

    def clear_free_board(self):
        for y in range(self.board_length):
            for x in range(self.board_length):
                #if not current_block.is_coord_of_block(x, y):
                    if self.board[y][x] != ' ' and self.board[y][x] != '#':
                        self.board[y][x] = ' '

    def put_current_block(self, block, x, y):
        base_x = x
        self.clear_free_board()
        for line in block:
            for char in line:
                self.board[y][x] = char
                x += 1
            x = base_x
            y += 1
