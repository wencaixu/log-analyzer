import socket
import time

SERVER = ""
PORT = 8888

for k in range(10000):
    sock = socket.socket()
    sock.connect((SERVER, PORT))
    message = "123"
    print(message)
    sock.sendall(bytes(message, encoding="utf8"))
    sock.close()
    time.sleep(1)
