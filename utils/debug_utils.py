import os
import time


from datetime import datetime


def print_game_frame(frame, save_to_file=False):
    print('-------------------------------------------')
    print('                 Debug frame')
    print('-------------------------------------------')
    for line in frame:
        for char in line:
            print(char, end='')
        print('')

    if save_to_file:
        fn = f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}-DEBUG-FRAME.txt"
        f = open(fn, 'w')
        for line in frame:
            for char in line:
                f.write(char)
            f.write('\n')
        print(f"Frame saved at: {fn}")


def rotate(animations):
    # This is just a fun thing I wanted to try
    c_index = 0
    while c_index <= (len(animations) - 1):
        os.system('clear')
        print(animations[c_index])
        c_index += 1
        if c_index > (len(animations) - 1):
            c_index = 0
        time.sleep(0.2)
