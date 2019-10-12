'''
A function which checks whether the TIC_TAC_TOE game is in a win or draw or continue state.
i/p : State of the tic-tac-toe board (A list of 9 entries)
o/p:
if a WIN , the winning player symbol is returned (X OR O)
elif a DRAW, 0 is returned
else  CONTINUE state, -1 is returned

            BOARD
    |   0   |   1   |   2   |
    |   3   |   4   |   5   |
    |   6   |   7   |   8   |

    Input Symbols are X and O or " " for empty
'''

def isGameOver(board):
    # row match for X or O
    pos = 0;
    while(pos<=6):
        if(board[pos]=='X' and board[pos+1]=='X' and board[pos+2]=='X'):
            return 'X'
        if(board[pos]=='O' and board[pos+1]=='O' and board[pos+2]=='O'):
            return 'O'
        pos+=3
    # col match for X or O
    pos=0
    while(pos<=2):
        if(board[pos]=='X' and board[pos+3]=='X' and board[pos+6]=='X'):
            return 'X'
        if(board[pos]=='O' and board[pos+3]=='O' and board[pos+6]=='O'):
            return 'O'
        pos+=1
    #first diagnonal match for O or X
    pos=0
    if(board[pos]=='X' and board[pos+4]=='X' and board[pos+8]=='X'):
            return 'X'
    if(board[pos]=='O' and board[pos+4]=='O' and board[pos+8]=='O'):
            return 'O'
    # second diagonal match for X or O
    pos = 6
    if(board[pos]=='X' and board[pos-2]=='X' and board[pos-4]=='X'):
            return 'X'
    if(board[pos]=='O' and board[pos-2]=='O' and board[pos-4]=='O'):
            return 'O'
    #now to check whether if it is a draw or conitune state
    pos=0
    while(pos<=8):
        if board[pos]==" ":
            return -1
        pos=pos+1
    # now all are occupied hence a DRAW
    return 0


def main():
    arr = ['X','X','O','O','0','O',' ','O','X']
    returnValue = isGameOver(arr)
    print(returnValue)
    return

main()