import os
import random
import keyboard
import models as m


class Game:
	def __init__(self, board_len):
		self.board = []
		self.board_length = board_len
		self.free_board_length = board_len
		self.is_running = True
		self.global_y = 0
		self.global_x = 6
		self.current_block = self.choose_random_block()
		self.load_board()

	def process_input(self):
		if keyboard.is_pressed('l'):
			self.global_x += 1
		elif keyboard.is_pressed('j'):
			self.global_x -= 1
		elif keyboard.is_pressed('k'):
			self.current_block.rotate()

	def update(self):
		splitted_block = self.current_block.sprite.split('\n')
		delta_y = self.global_y + len(splitted_block)
		self.put_current_block(splitted_block, self.global_x, self.global_y)
		self.current_block.update_pos(self.global_x, self.global_y)
		self.current_block.generate_coords()
        #TODO: Esta logica funciona para que caigan varios
        # bloques, sin embargo el free_board_length esta bugueao'
		if delta_y < self.board_length:
			if self.board[delta_y][self.global_x] == ' ':
				self.global_y += 1
		elif delta_y >= self.board_length:
			if self.board[delta_y - 1][self.global_x] == ' ':
				self.global_y += 1
			self.free_board_length -= len(splitted_block)
			self.current_block = self.choose_random_block()
			self.global_y = 0
			self.global_x = 6

	def render(self):
		os.system('clear')
		self.print_board()

	def put_current_block(self, block, x, y):
		base_x = x
		self.clear_free_board()
		for line in block:
			for char in line:
				self.board[y][x] = char
				x += 1
			x = base_x
			y += 1

	def load_board(self):
		for _y in range(self.board_length):
			new_line = []
			new_line.append(m.Blocks.BASE)
			for _x in range(self.board_length - 2):
				new_line.append(' ')
			new_line.append(m.Blocks.BASE)
			self.board.append(new_line)

	def clear_free_board(self):
		for y in range(self.board_length):
			for x in range(self.board_length):
				#if not current_block.is_coord_of_block(x, y):
					if self.board[y][x] != ' ' and self.board[y][x] != '#':
						self.board[y][x] = ' '

	def print_board(self):
		for y in range(self.board_length):
			for x in range(self.board_length):
				print(self.board[y][x], end='')
			print()
		print(' ', end='')
		print(f"{m.Blocks.BASE} "*9)

	def choose_random_block(self):
		block_sprites = random.choice(m.Blocks.ALL)
		new_block = m.Block(x=self.global_x, y=self.global_y,
		      				animations=block_sprites)
		return new_block