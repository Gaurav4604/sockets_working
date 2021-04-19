import socket

HOST = '127.0.0.1'
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for i in range(5):
        s.sendall(bytearray(f'Hello this is msg {i}','utf8'))
        data = s.recv(1024).decode('utf-8')
        print(f'Recieved {data}')
