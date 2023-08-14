from game import Game


if __name__ == '__main__':
    game = Game(board_len=20)
    while game.is_running:
        game.process_input()
        game.update()
        game.render()
