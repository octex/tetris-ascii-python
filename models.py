import curses
import random


from datetime import datetime


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
    def __init__(self, board_length, stdscr):
        self.stdscr = stdscr
        self.board = []
        self.board_length = board_length
        self.get_random_pair()
        self.safe_buffer = []
        self.condition_counter = 0

    def save_safe_buffer(self, buffer):
        self.safe_buffer = []
        for line in buffer:
            new_line = ""
            for char in line:
                new_line += char
            self.safe_buffer.append(new_line)

    def get_random_pair(self):
        curses.init_pair(1, random.choice(Constants.COLORS), curses.COLOR_BLACK)

    def print_board(self, new_frame=None, current_block=None):
        if new_frame:
            self.board = new_frame
        for y in range(self.board_length):
            for x in range(self.board_length):
                if current_block:
                    if self.board[y][x] != '#' and self.board[y][x] != ' ' and current_block.is_coord_of_block(x, y): # and block.is_coord_of_block(x, y)
                        # self.get_random_pair()
                        self.stdscr.addch(y, x, self.board[y][x], curses.color_pair(1) | curses.A_BOLD)
                    else:
                        self.stdscr.addch(y, x, self.board[y][x])
                else:
                    self.stdscr.addch(y, x, self.board[y][x])
        self.stdscr.addstr(self.board_length, 1, f"{Blocks.BASE}" * (self.board_length - 2))
    
    def load_board(self):
        for _y in range(self.board_length):
            new_line = []
            new_line.append(Blocks.BASE)
            for _x in range(self.board_length - 2):
                new_line.append(' ')
            new_line.append(Blocks.BASE)
            self.board.append(new_line)

    def clear_block_previous_position(self, coords, frame):
        for p_coord in coords:
            for x, y in p_coord:
                if self.safe_buffer:
                    if self.safe_buffer[y][x] == ' ':
                        frame[y][x] = ' '
                    elif self.safe_buffer[y][x] != ' ':
                        frame[y][x] = self.safe_buffer[y][x]
                        self.condition_counter += 1
                else:
                    frame[y][x] = ' '

    @staticmethod
    def put_current_block(block, x, y, frame=None):
        base_x = x
        for line in block:
            for char in line:
                if char != ' ':
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
