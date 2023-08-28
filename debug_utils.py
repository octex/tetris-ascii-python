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
