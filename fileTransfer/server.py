import socket
import os

host = 'localhost'
port = 12345

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((host, port))

sock.listen(5)

conn, addr = sock.accept()

recieved = conn.recv(BUFFER_SIZE).decode()

filename, filesize = recieved.split(SEPARATOR)
filename = os.path.basename(filename)

# filesize = int(filesize)
print(filesize, filename)


with open(filename, 'wb') as f:
    while True:
        bytes_read = conn.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)

conn.close()
sock.close()