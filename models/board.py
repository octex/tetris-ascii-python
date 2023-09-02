import curses
import random


from utils.constants import Constants as c
from utils.constants import Blocks


class Board:
    def __init__(self, board_length, stdscr):
        self.stdscr = stdscr
        self.board = []
        self.board_length = board_length
        self.get_random_pair()
        self.safe_buffer = []
        self.numeric_buffer = []

    def get_completed_lines(self):
        y_indexes = []
        for line in self.numeric_buffer:
            current_y_index = self.numeric_buffer.index(line)
            is_completed = True
            for pos in line:
                if pos == 0:
                    is_completed = False
                    break
            if is_completed:
                y_indexes.append(current_y_index)
        return y_indexes

    def save_numeric_buffer(self, buffer):
        self.numeric_buffer.clear()
        for line in buffer:
            new_line = []
            for char in line:
                if char == '#':
                    new_line.append(-1)
                elif char == ' ':
                    new_line.append(0)
                else:
                    new_line.append(1)
            self.numeric_buffer.append(new_line)


    def save_safe_buffer(self, buffer):
        self.safe_buffer.clear()
        for line in buffer:
            new_line = ""
            for char in line:
                new_line += char
            self.safe_buffer.append(new_line)
        self.save_numeric_buffer(self.safe_buffer)

    def clear_line(self, y_index, buffer=None):
        if buffer:
            t_buffer = buffer
        else:
            t_buffer = self.board
        for line in t_buffer:
            if t_buffer.index(line) == y_index:
                for char in line:
                    if char != '#':
                        line[line.index(char)] = ' '
                self.clear_trash_chars(t_buffer, y_index - 1)

    def rebuild_board(self, buffer):
        t_buffer = buffer.copy()
        for i in range(len(t_buffer)):
            if self.is_line_clear(t_buffer[i]):
                t_line = buffer[i].copy()
                buffer[i].clear()
                buffer.remove([])
                buffer.insert(0, t_line)

    def clear_trash_chars(self, buffer=None, start_index=0):
        if buffer:
            t_buffer = buffer
        else:
            t_buffer = self.board
        for i in range(len(t_buffer[start_index])):
            if t_buffer[start_index][i] == '_':
                index_l = i - 1
                index_r = i + 1
                condition = (t_buffer[start_index][index_l] != '|' or \
                             t_buffer[start_index][index_r] != '|') or \
                                t_buffer[start_index - 1][i] == ' '
                if condition:
                    t_buffer[start_index][i] = ' '

    def get_random_pair(self):
        curses.init_pair(1, random.choice(c.COLORS), curses.COLOR_BLACK)

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
