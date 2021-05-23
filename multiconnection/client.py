import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '192.168.1.12'
PORT = 12345

print('[INFO] waiting for server response')

sock.connect((HOST, PORT))

res = sock.recv(1024)
print('Server Response -> ' + res.decode('utf-8'))
while True:
    message = input('input your message: ')
    sock.send(str.encode(message))
    res = sock.recv(1024).decode('utf-8')
    print(res)
    if message == 'exit':
        break
        
sock.close()