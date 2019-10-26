# client solver
# 1 -> win
# 0 -> draw
# -1 -> lose
# board -> string[0 - 8] to store the state of the board
# dp[2][board] -> stores the (optimal value, action pair), dp[0][board] -> player 1, dp[1][board] -> player 2

import socket

dp = [{}, {}]
port = 123
server = '127.0.0.1'

def isGameOver(board):
    X = 'XXX'
    O = 'OOO'
    pos = 0
    lst = []
    # row
    while pos <= 6:
        s = board[pos] + board[pos + 1] + board[pos + 2]
        lst.append(s)
        pos += 3

    pos = 0
    # column
    while pos <= 2:
        s = board[pos] + board[pos + 3] + board[pos + 6]
        lst.append(s)
        pos += 1

    # Diagonals
    s = board[0] + board[4] + board[8]
    lst.append(s)
    s = board[2] + board[4] + board[6]
    lst.append(s)

    if X in lst:
        return 1
    if O in lst:
        return 0
    return -1

def solve(board, turn):
    if board in dp[turn]:
        return dp[turn][board][0]
    over = isGameOver(board)
    if over == turn:
        dp[turn][board] = (1, -1)
        return 1
    if over != -1:
        dp[turn][board] = (-1, -1)
        return -1
    tup = ()
    ch = 'O'
    if turn:
        ch = 'X'
    for act in range(9):
        if board[act] != ' ':
            continue
        val = solve(board[: act] + ch + board[act + 1 :], 1 - turn)
        if val != 0:
            val = -val
        tup = tup + ((val, act),)
    if len(tup):
        dp[turn][board] = max(tup)
    else:
        dp[turn][board] = (0, -1)
    return dp[turn][board][0]

def decision(arr, turn):
    ch = 'O'
    tup = ()
    if turn:
        ch = 'X'
    for act in range(9):
        if arr[act] != ' ':
            continue
        val = solve(arr[: act] + ch + arr[act + 1 :], 1 - turn)
        if val != 0:
            val = -val
        tup = tup + ((val, act),)
    dp[turn][arr] = max(tup)
    return dp[turn][arr][1]

def main():
    
    board = 9 * ' '
    for turn in range(2):
        tup = ()
        ch = '0'
        if turn:
            ch = 'X'
        for act in range(9):
            if board[act] != ' ':
                continue
            val = solve(board[: act] + ch + board[act + 1 :], 1 - turn)
            if val != 0:
                val = -val
            tup = tup + ((val, act),)
        dp[turn][board] = max(tup)
        
    ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser.connect((server, port))
    msg = ser.recv(1024)
    msg = msg.decode('utf-8')
    turn = int(msg)
    while True:
        msg = ser.recv(1024)
        msg = msg.decode('utf-8')
        if msg != "over" :
            act = decision(msg, turn)
            act = str(act)
            act = act.encode('utf-8')
            ser.send(act)
        else:
            break
    ser.close()


if __name__ == "__main__":
    main()
