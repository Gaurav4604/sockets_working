import socket

HOST = '172.20.10.13'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for i in range(5):
        s.sendall(f'Hello this is msg {i}'.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print(f'Recieved {data}')