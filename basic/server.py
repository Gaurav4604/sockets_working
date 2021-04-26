import socket

HOST = '192.168.1.16'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('socket initialized')
    conn, addr = s.accept()
    count = 0
    with conn:
        print(f'Connected with {addr}')
        while True:
            data = conn.recv(1024).decode('utf-8')
            print(data)
            if not data:
                break
            else:
                print(f'Sending acknowledgement for {count}')
                conn.sendall('acknowledgement for data sent'.encode('utf-8'))
                count += 1