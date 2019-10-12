from checkValid import checkValid

def update(arr, playerNo, i):

	if not checkValid(arr, i):
		return False
	
	if playerNo == 0:
		arr[i] = 'O'
	else:
		arr[i] = 'X'
	
	return True
