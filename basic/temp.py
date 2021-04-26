import socket

HOST = '192.168.1.16'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for i in range(5):
        a = input("enter your data: ")
        s.sendall(bytearray(f'{a}','utf8'))
        data = s.recv(1024).decode('utf-8')
        print(f'Recieved {data}')
