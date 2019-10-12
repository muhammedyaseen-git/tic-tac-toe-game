# from IPython.display import clear_output
from os import system

''' 
X -> Red
O -> Green
_ -> White Background


'''

def display(board, cursor):

	# ANSI escape codes for colors
	RED = '\033[31m'
	GREEN = '\033[32m'
	RESET = '\033[0m'
	WHITE = '\033[47m'
	s = ''
	for i in range(0, len(board)):

		# white background for cursor highlight
		if cursor == i:
			s = s + WHITE
		if board[i] == 'X':
			s = s + RED + ' X ' + RESET
		elif board[i] == 'O':
			s = s + GREEN + ' O ' + RESET
		else:
			s = s + '   ' + RESET

		# 
		row = i // 3
		col = i % 3

		if col < 2:
			s = s + '|'
		# last column
		else:
			s = s + '\n'
			# last row
			if row < 2:
				s = s + '-----------\n'
	
	
	# clear_output()
	system('clear')
	print(s)
	return
		

# board = ['X', 'O', 'X', 'X', ' ', 'X', 'X', 'O', 'X']
# display(board, 8)
