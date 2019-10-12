from isGameOver import isGameOver
from checkValid import checkValid
from visualize import display
from update import update

def play():
	
	# An array to represent the tic-tac-toe board,  
	# assume that the board is a 3*3 matrix
	arr = [' ' for i in range(9)]
	
	# Cursor location is represented by row,col 
	row = col = 0
	
	# A set of cursor characters which would
	# be input by the player
	cursorChar = set(('w', 's', 'a', 'd'))
	
	# Current Player number
	player = 0
	
	# Result to be printed
	res = ["Player 0 won", "Player 1 won", "Draw"]
	
	# A while loop which would simulate
	# the game
	while True:
		
		# This would display the current game
		# status
		display(arr, row * 3 + col)
		
		# Get input from the player
		c = input()
		
		# If the input is a cursor character, do as follows
		if c in cursorChar:
			
			if c == 'w' and row != 0:		# If the cursor moves up, then reduce row value
				row -= 1
			elif c == 's' and row != 2:		# If the cursor moves down, then increase row value
				row += 1
			elif c == 'a' and col != 0:		# If the cursor moves left, then reduce col value
				col -= 1
			elif c == 'd' and col != 2:		# If the cursor moves right, then increase col value
				col += 1

		elif c == ' ':						# If the input is an enter character, then do as follows
			
			if update(arr, player, row * 3 + col):	# Update the game board if possible
				
				player = 1 - player			# Change the player
				
				pl = isGameOver(arr)		# Get game status
				
				if pl != -2:				# If the game is over, do as follows
					display(arr, row * 3 + col)
					print(res[pl])			# print the results
					break					# End the game

if __name__ == '__main__':
	
	play()
