import time
import os
import random
import pdb
import curses
import models as m


from datetime import datetime


class Game:
	def __init__(self, board_length, stdscr):
		self.stdscr = stdscr
		self.stdscr.nodelay(True)
		self.board = m.Board(board_length, stdscr)
		self.new_board_frame = []
		self.is_running = True
		#TODO: Mover el cursor al caracter del medio del bloque
		self.global_y = 0
		self.global_x = 13
		self.current_block = self.choose_random_block()
		self.deltaTime = 0
		self.last = datetime.now()
		self.current = None
		self.rotate = False
		self.move_r = True
		self.move_l = True
		self.score = 0
		self.board.load_board()

	def process_input(self):
		movement = 2
		cha = self.stdscr.getch()
		curses.flushinp()
		if cha == ord('l'):
			if self.move_r:
				self.global_x += movement
		elif cha == ord('j'):
			if self.move_l:
				self.global_x -= movement
		elif cha == ord('k'):
			self.rotate = True
		elif cha == ord('d'):
			self.debug()
		elif cha == ord('q'):
			self.is_running = False

	def update(self):
		self.new_board_frame = self.board.board
		self.current = datetime.now()
		self.deltaTime = (self.current - self.last) / 1000
		self.deltaTime = float(str(self.deltaTime).split(':')[2])

		delta_x = self.global_x + self.current_block.get_x_length()
		delta_y = self.global_y + len(self.current_block.splitted)
		prev_pos = self.current_block.coords
	
		self.board.clear_block_previous_position(prev_pos, self.new_board_frame)

		if self.rotate:
			self.current_block.rotate()
			self.rotate = False

		self.move_r = True
		self.move_l = True

		if not self.global_x >= 1:
			self.global_x = 1
		else:
			for line in self.current_block.splitted:
				y = self.global_y + self.current_block.splitted.index(line)
				x = self.global_x - 1
				left_char = self.new_board_frame[y][x]
				if left_char != '|' and left_char != ' ' and not self.current_block.is_coord_of_block(x, y):
					self.move_l = False

		if delta_x >= self.board.board_length - 2:
			self.move_r = False
		else:
			for line in self.current_block.splitted:
				y = self.global_y + self.current_block.splitted.index(line)
				x = self.global_x + 1
				left_char = self.new_board_frame[y][x]
				if left_char != '|' and left_char != ' ' and not self.current_block.is_coord_of_block(x, y):
					self.move_l = False

		if delta_y < self.board.board_length:
			if m.Board.is_line_clear(self.new_board_frame[delta_y]):
				self.global_y += 1
			else:
				touches = False
				#TODO: Esto esta mal, porque no siempre las colisiones verticales se dan en la parte media de abajo de todo
				middle_bottom = self.current_block.coords[len(self.current_block.coords) - 1][1:-1]
				for coord in middle_bottom:
					if self.new_board_frame[delta_y][coord[0]] != ' ':
						touches = True
				self.global_y += 1
				if touches:
					m.Board.put_current_block(self.current_block.splitted, self.global_x, self.global_y, self.new_board_frame)
					self.board.save_safe_buffer(self.new_board_frame)
					self.current_block = self.choose_random_block()
					self.global_y = 0
					self.global_x = 13
					self.board.get_random_pair()

		elif delta_y >= self.board.board_length:
			m.Board.put_current_block(self.current_block.splitted, self.global_x, self.global_y, self.new_board_frame)
			self.board.save_safe_buffer(self.new_board_frame)
			self.current_block = self.choose_random_block()
			self.global_y = 0
			self.global_x = 13
			self.board.get_random_pair()

		self.current_block.update_pos(self.global_x, self.global_y)
		m.Board.put_current_block(self.current_block.splitted, self.global_x, self.global_y, self.new_board_frame)
		self.last = self.current

	def render(self):
		self.stdscr.clear()
		self.board.print_board(new_frame=self.new_board_frame, current_block=self.current_block)
		if self.deltaTime < m.Constants.LOW_FRAMES:
			self.deltaTime = m.Constants.LOW_FRAMES
		elif self.deltaTime > m.Constants.HIGH_FRAMES:
			self.deltaTime = m.Constants.HIGH_FRAMES
		self.stdscr.addstr(self.board.board_length + 1, 12, f"Score: {self.score}", curses.A_STANDOUT)
		self.stdscr.refresh()
		time.sleep(self.deltaTime)

	def choose_random_block(self):
		block_sprites = random.choice(m.Blocks.ALL)
		new_block = m.Block(x=self.global_x, y=self.global_y,
		      				animations=block_sprites)
		return new_block

	def debug(self):
		import debug_utils as du
		msg = "Game stopped. Entering Debug Mode"
		self.stdscr.addch(self.board.board_length + 2, 0, '\n')
		self.stdscr.addstr(self.board.board_length + 3, 0, f"{'-' * len(msg)}")
		self.stdscr.addstr(self.board.board_length + 4, 0, msg)
		self.stdscr.addstr(self.board.board_length + 5, 0, f"{'-' * len(msg)}")
		self.stdscr.refresh()
		curses.endwin()
		print("------- Debug utils imported as du -------")
		pdb.set_trace()


class Menu:
	def __init__(self, stdscr):
		self.stdscr = stdscr
		self.print_logo()
		self.stdscr.addstr(8, 0, "\t\tPress any key to start...", curses.A_BOLD)
		self.stdscr.refresh()
		self.stdscr.getkey()

	def print_logo(self):
		# logo source: https://patorjk.com/software/taag/#p=display&f=Varsity&t=TETRIS
		f = open('tetris-logo.txt', 'r')
		text = f.read()
		self.stdscr.clear()
		self.stdscr.addstr(0, 0, f"{text}", curses.A_BOLD)
		self.stdscr.refresh()


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
