from isGameOver import isGameOver
from checkValid import checkValid
from visualize import display
from update import update
import socket

port = 1234

def play():
	
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# An array to represent the tic-tac-toe board,  
	# assume that the board is a 3*3 matrix
	arr = [' ' for i in range(9)]
	
	# Cursor location is represented by row,col 
	row = col = 0
	
	# A set of cursor characters which would
	# be input by the player
	cursorChar = set(('w', 's', 'a', 'd'))
	
	server.bind(('', port))
	server.listen(2)
	# Current Player number
	player = 0
	turn = '1'.encode('utf-8')
	client, addr = server.accept()
	client.send(turn)
	
	# Result to be printed
	res = ["Player 0 won", "Player 1 won", "Draw"]
	
	# A while loop which would simulate
	# the game
	while True:
		
		# This would display the current game
		# status
		display(arr, row * 3 + col)
		
		if player:
			msg = ''
			for i in range(9):
				msg = msg + arr[i]
			msg = msg.encode('utf-8')
			client.send(msg)
			msg = client.recv(1024)
			msg = msg.decode('utf-8')
			msg = int(msg)

			if update(arr, player, msg):	# Update the game board if possible
				player = 1 - player
				pl = isGameOver(arr)
				if pl != -2:
					display(arr, row * 3 + col)
					print(res[pl])
					break			
			
		else :
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
	msg = "over".encode('utf-8')
	client.send(msg)
	server.close()

if __name__ == '__main__':
	
	play()
