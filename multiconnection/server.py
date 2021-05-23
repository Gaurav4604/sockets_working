import socket
from _thread import *
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # telling the socket connection to connect via TCP protocol

HOST = '192.168.1.12'
PORT = 12345
conn_check_list = []
sock.bind((HOST, PORT))


print('[INFO] waiting for connections...')
sock.listen(10) # waiting for connections, this tells how many items can be there in backlog



# function to handle client message
def multi_client(connection):
    count = 0
    connection.send(str.encode("client is now connected"))
    try:
        while True:
            data = connection.recv(1024)
            print("Message from client -> " + data.decode('utf-8'))
            count += 1
            response = "server acknowledgment for message no. " + str(count)

            if data.decode('utf-8') == 'exit': 
                connection.sendall(str.encode("[INFO] Terminating connection to current client..."))
                connection.close()
                conn_check_list.remove(connection)
                print('[INFO] connection terminated')
                break
            else:
                connection.sendall(str.encode(response))
    except Exception as e:
        print(e)


# checker function to see if no connections are made to the server after the initial ones
def time_checker():
    while True:
        time.sleep(1)
        if len(conn_check_list) < 1:
            print("[INFO] server will close after 20 seconds of inactivity")
            time.sleep(20)
            if len(conn_check_list) < 1:
                
                sock.close()
        else:
            continue



def establish_connection():

    while True:
        conn, addr = sock.accept()
        conn_check_list.append(conn)
        print('[INFO] Connection to ' + addr[0] + ' : ' + str(addr[1]) + ' initialized')
        start_new_thread(multi_client, (conn, ))
        start_new_thread(time_checker, ())
        print('[INFO] no of connections -> ' + str(len(conn_check_list)))

if __name__ == '__main__':
    try:
        establish_connection()
    except:
        print('[INFO] server is now closed due to TIMEOUT')