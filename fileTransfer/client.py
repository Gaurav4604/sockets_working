import socket
import os
import time

SEPARATOR = "<SEPARATOR>"

BUFFER_SIZE = 4096 # sending 4096 bytes at every cycle

host = 'localhost'
port = 12345

# client socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

filename = "../Churn.txt"
filesize = os.path.getsize(filename)
print(filesize)
print("[INFO] connecting to socket")
sock.connect((host, port))

sock.sendall(f"{filename}{SEPARATOR}{filesize}".encode())

time.sleep(0.15)

with open(filename, 'rb') as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        else:
            sock.sendall(bytes_read)

sock.close()