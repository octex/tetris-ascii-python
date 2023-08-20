

class Constants:
    HIGH_FRAMES = 0.5
    LOW_FRAMES = 0.15
    
    class BColors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

class Blocks:
    BASE = "#"

    I = (" _\n|_|\n|_|\n|_|\n|_|",
    " _ _ _ _\n|_|_|_|_|")

    O = (" _ _\n|_|_|\n|_|_|",)
    
    T = ("   _\n _|_|_\n|_|_|_|",
        " _\n|_|_\n|_|_|\n|_|",
        " _ _ _\n|_|_|_|\n  |_|",
        "   _\n _|_|\n|_|_|\n  |_|")
    
    S = ("   _ _\n _|_|_|\n|_|_|",
        " _\n|_|_\n|_|_|\n  |_|")

    L = (" _\n|_|\n|_|_\n|_|_|",
        " _ _ _\n|_|_|_|\n|_|",
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
        self.generate_splitted()
        self.generate_coords()

    def rotate(self):
        if self.current_index == len(self.animations) - 1:
            self.current_index = 0
        else:
            self.current_index += 1
        self.sprite = self.animations[self.current_index]
        self.generate_splitted()
        self.generate_coords()
    
    def update_pos(self, x, y):
        self.x = x
        self.y = y
        self.generate_coords()

    def generate_coords(self):
        self.coords = []
        t_x = self.x
        t_y = self.y
        base_x = t_x
        for line in self.splitted:
            new_coords = []
            for char in line:
                if char != ' ':
                    coord = (t_x, t_y)
                    new_coords.append(coord)
                t_x += 1
            self.coords.append(new_coords)
            t_y += 1
            t_x = base_x
        # return coords

    def is_coord_of_block(self, x, y):
        for coord in self.coords:
            for _coord in coord:
                if _coord[0] == x and _coord[1] == y:
                    return True
        return False

    def get_x_length(self):
        exes = []
        for line in self.coords:
            for coord in line:
                exes.append(coord[0])
        exes.sort()
        exes = set(exes)
        return len(exes)

    def generate_splitted(self):
        self.splitted = self.sprite.split('\n')

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
            print("\t", end='')
            for x in range(self.board_length):
                print(f"{self.board[y][x]}", end='')
            print()
        print('\t ', end='')
        print(f"{Blocks.BASE}" * (self.board_length - 2), end='')
        print(' ')
    
    def load_board(self):
        for _y in range(self.board_length):
            new_line = []
            new_line.append(Blocks.BASE)
            for _x in range(self.board_length - 2):
                new_line.append(' ')
            new_line.append(Blocks.BASE)
            self.board.append(new_line)

    @staticmethod
    def clear_block_previous_position(prev_block_coords, frame, block):
        for p_coord in prev_block_coords:
            for x, y in p_coord:
                # if block.splitted[y - block.y][x - block.x] != '  ':
                frame[y][x] = ' '

    @staticmethod
    def put_current_block(block, x, y, frame=None):
        base_x = x
        for line in block:
            for char in line:
                frame[y][x] = char
                x += 1
            x = base_x
            y += 1

    @staticmethod
    def is_line_clear(line):
        for char in line:
            if char != ' ' and char != Blocks.BASE:
                return False
        return True
