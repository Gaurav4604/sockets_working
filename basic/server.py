import socket

HOST = '127.0.0.1'
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'Connected with {addr}')
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            else:
                print(f'Sending acknowledgement for {data}')
                conn.sendall(b'acknowledgement')