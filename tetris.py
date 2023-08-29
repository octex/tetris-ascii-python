from models.game import Game
from models.menu import Menu
from curses import wrapper


def main(stdscr):
    menu = Menu(stdscr=stdscr)
    game = Game(board_length=31, stdscr=stdscr)
    while game.is_running:
        game.process_input()
        game.update()
        game.render()


if __name__ == '__main__':
    wrapper(main)
