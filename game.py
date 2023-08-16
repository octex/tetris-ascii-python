import time
import os
import random
import models as m


from pynput import keyboard
from datetime import datetime


HIGH_FRAMES = 0.5
LOW_FRAMES = 0.15


class Game:
	def __init__(self, board_len):
		self.board = m.Board(board_len)
		self.new_board_frame = []
		self.is_running = True
		self.global_y = 0
		self.global_x = 6
		self.current_block = self.choose_random_block()
		self.deltaTime = 0
		self.last = datetime.now()
		self.current = None
		self.board.load_board()

	def process_input(self):
		with keyboard.Events() as events:
			event = events.get(self.deltaTime)
			if event:
				if event.key == keyboard.KeyCode.from_char('l') and self.global_x < self.board.board_length: #len block
					self.global_x += 1
				elif event.key == keyboard.KeyCode.from_char('j') and self.global_x > 1:
					self.global_x -= 1
				elif event.key == keyboard.KeyCode.from_char('k'):
					self.current_block.rotate()

	def update(self):
		self.new_board_frame = self.board.board
		self.current = datetime.now()
		self.deltaTime = (self.current - self.last) / 1000
		self.deltaTime = float(str(self.deltaTime).split(':')[2])

		splitted_block = self.current_block.sprite.split('\n')
		delta_y = self.global_y + len(splitted_block)
		self.board.put_current_block(splitted_block, self.global_x, self.global_y)
		self.current_block.update_pos(self.global_x, self.global_y)
		self.current_block.generate_coords()
        
		#TODO: Esta logica funciona para que caigan varios
        # bloques, sin embargo el free_board_length esta bugueao'
		
		if delta_y < self.board.board_length:
			if self.new_board_frame[delta_y][self.global_x] == ' ':
				self.global_y += 1
		elif delta_y >= self.board.board_length:
			if self.new_board_frame[delta_y - 1][self.global_x] == ' ':
				self.global_y += 1
			self.current_block = self.choose_random_block()
			self.global_y = 0
			self.global_x = 6
		self.last = self.current

	def render(self):
		os.system("clear")
		self.board.print_board(new_frame=self.new_board_frame)
		if self.deltaTime < LOW_FRAMES:
			self.deltaTime = LOW_FRAMES
		elif self.deltaTime > HIGH_FRAMES:
			self.deltaTime = HIGH_FRAMES
		print(f"Deltatime: {self.deltaTime}")
		print(f"Last Frame Time: {self.last}")
		print(f"Current Frame Time: {self.current}")
		time.sleep(self.deltaTime)

	def choose_random_block(self):
		block_sprites = random.choice(m.Blocks.ALL)
		new_block = m.Block(x=self.global_x, y=self.global_y,
		      				animations=block_sprites)
		
		return new_block
