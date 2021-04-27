import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"

BUFFER_SIZE = 4096 # sending 4096 bytes at every cycle

host = 'localhost'
port = 12345

# client socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

filename = "Churn.csv"
filesize = os.path.getsize(filename)

print("[INFO] connecting to socket")
sock.connect((host, port))

sock.sendall(f"{filename}{SEPARATOR}{filesize}".encode())

