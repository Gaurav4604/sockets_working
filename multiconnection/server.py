import socket
from _thread import *

sock = socket.socket()

HOST = '192.168.1.16'
PORT = 8888

sock.bind((HOST, PORT))

threads = 0

print('[INFO] waiting for connections...')
sock.listen(10)