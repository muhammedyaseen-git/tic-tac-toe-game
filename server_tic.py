import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345

s.bind(('', port))
s.listen(2)
while True:
    c, addr = s.accept()
    print("hi")
    os.system('sleep 2')
    c.send(b'01')
    s.close()
    break
