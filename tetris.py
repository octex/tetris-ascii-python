import time
import os
import random

import keyboard
import models as m

board = []
global_y = 0
global_x = 6
# limit_x = 19
board_length = 20
free_board_length = board_length


def choose_random_block():
    block_sprites = random.choice(m.Blocks.ALL)
    new_block = m.Block(x=global_x, y=global_y, animations=block_sprites)
    return new_block

def clear_free_board():
    for y in range(board_length):
        for x in range(board_length):
            #if not current_block.is_coord_of_block(x, y):
                if board[y][x] != ' ' and board[y][x] != '#':
                    board[y][x] = ' '

current_block = choose_random_block()


def load_board():
    for _y in range(board_length):
        new_line = []
        new_line.append(m.Blocks.BASE)
        for _x in range(board_length - 2):
            new_line.append(' ')
        new_line.append(m.Blocks.BASE)
        board.append(new_line)


def put_current_block(block, x, y):
    base_x = x
    clear_free_board()
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
        print()
    print(' ', end='')
    print(f"{m.Blocks.BASE} "*9)


def process_input():
    global global_x
    if keyboard.is_pressed('l'):
        global_x += 1
    elif keyboard.is_pressed('j'):
        global_x -= 1
    elif keyboard.is_pressed('k'):
        current_block.rotate()

def update():
    global global_y
    global global_x
    global current_block
    global free_board_length
    global board

    splitted_block = current_block.sprite.split('\n')
    delta_y = global_y + len(splitted_block)
    put_current_block(splitted_block, global_x, global_y)
    current_block.update_pos(global_x, global_y)
    current_block.generate_coords()
    #TODO: Esta logica funciona para que caigan varios
    # bloques, sin embargo el free_board_length esta bugueao'
    if delta_y < board_length:
        if board[delta_y][global_x] == ' ':
            global_y += 1
    elif delta_y >= board_length:
        if board[delta_y - 1][global_x] == ' ':
            global_y += 1
        free_board_length -= len(splitted_block)
        current_block = choose_random_block()
        global_y = 0
        global_x = 6
        
    

def render():
    os.system('cls')
    print_board(board)


if __name__ == '__main__':
    load_board()
    while True:
        process_input()
        update()
        render()
        time.sleep(0.35)
