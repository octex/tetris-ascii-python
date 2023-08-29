import curses


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
