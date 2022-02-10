import time
import os
import random


board = []
global_y = 1
global_x = 1
board_length = 20


class Blocks:
    BASE = "#"
    I = " _\n| |\n| |\n| |\n|_|"
    O = " ___\n|   |\n|___|"
    T = "   _\n _| |_\n|_____|"
    S = " _\n| |_\n|_  |\n  |_|"
    L = " _\n| |\n| |_\n|___|"
    Z = "   _\n _| |\n|  _|\n|_|"
    J = "   _\n  | |\n _| |\n|___|"
    ALL = [I, O, T, S, L, Z, J]


def choose_random_block():
    return random.choice(Blocks.ALL)


current_block = choose_random_block()


def load_board(board):
    for y in range(board_length):
        new_line = []
        new_line.append(Blocks.BASE)
        for x in range(board_length - 2):
            new_line.append(' ')
        new_line.append(Blocks.BASE)
        board.append(new_line)
    

def put_current_block(block, x, y):
    base_x = x
    for line in block:
        for char in line:
            board[y][x] = char
            x += 1
        x = base_x
        y += 1


def print_board(board):
    for y in range(board_length):
        for x in range(board_length):
            print(board[y][x], end='')
            previous_pos = board[y - 1][x - 1]
            if previous_pos != ' ' and previous_pos != '#':
                board[y - 1][x - 1] = " "
        print()
    print(' ', end='')
    print(f"{Blocks.BASE} "*9)


def process_input():
    pass

def update():
    global global_y
    put_current_block(current_block.split('\n'), global_x, global_y)
    global_y += 1
    

def render():
    os.system('cls')
    print_board(board)


if __name__ == '__main__':
    load_board(board)
    while True:
        process_input()
        update()
        render()
        time.sleep(1)
