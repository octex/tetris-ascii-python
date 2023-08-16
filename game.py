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
				elif event.key == keyboard.KeyCode.from_char('q'):
					self.is_running = False

	def update(self):
		self.new_board_frame = self.board.board
		self.current = datetime.now()
		self.deltaTime = (self.current - self.last) / 1000
		self.deltaTime = float(str(self.deltaTime).split(':')[2])

		splitted_block = self.current_block.sprite.split('\n')
		delta_y = self.global_y + len(splitted_block)
		prev_pos = self.current_block.coords
		m.Board.clear_block_previous_position(prev_pos, self.new_board_frame)

		#TODO: Verificar en base a las coords del bloque y no por caracter individual
		#TODO: Agregar rotacion a la logica de update
		"""
			Para verificar colisiones:
				Me traigo la linea del piso del bloque
					De esa linea, los bordes los descarto.
						Por cada elemento que este en el medio, me fijo que abajo no haya nada
		"""
		if delta_y < self.board.board_length:
			
			# middle_bottom = self.current_block.coords[1:-1]
			# for coord in middle_bottom:
			# 	if self.new_board_frame[delta_y][coord[0]] != ' ':
			# 		pass
			
			if m.Board.is_line_clear(self.new_board_frame[delta_y]):
				self.global_y += 1
			else:
				touches = False
				middle_bottom = self.current_block.coords[len(self.current_block.coords) - 1][1:-1]
				for coord in middle_bottom:
					if self.new_board_frame[delta_y][coord[0]] != ' ':
						touches = True
				self.global_y += 1
				if touches:
					m.Board.put_current_block(splitted_block, self.global_x, self.global_y, self.new_board_frame)
					self.current_block = self.choose_random_block()
					self.global_y = 0
					self.global_x = 6
					splitted_block = self.current_block.sprite.split('\n')

		elif delta_y >= self.board.board_length:
			m.Board.put_current_block(splitted_block, self.global_x, self.global_y, self.new_board_frame)
			self.current_block = self.choose_random_block()
			self.global_y = 0
			self.global_x = 6
			splitted_block = self.current_block.sprite.split('\n')

		m.Board.put_current_block(splitted_block, self.global_x, self.global_y, self.new_board_frame)
		self.current_block.update_pos(self.global_x, self.global_y)
		
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
