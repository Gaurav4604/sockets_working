import threading
import socket
from _thread import *
import time

class Server(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.bind((host, port))
        self.server_sock.listen(10)
        self.conn_check_list = []
    
    def multi_client_handler(self, connection):
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
                    self.conn_check_list.remove(connection)
                    print('[INFO] connection terminated')
                    break
                else:
                    connection.sendall(str.encode(response))
        except Exception as e:
            print(e)      

    def time_checker(self):
        while True:
            time.sleep(1)
            if len(self.conn_check_list) < 1:
                print("[INFO] server will close after 20 seconds of inactivity")
                time.sleep(20)
                if len(self.conn_check_list) < 1:
                    
                    self.server_sock.close()
            else:
                continue

    def establish_conn(self):
        while True:
            conn, addr = self.server_sock.accept()
            self.conn_check_list.append(conn)
            print('[INFO] Connection to ' + addr[0] + ' : ' + str(addr[1]) + ' initialized')
            start_new_thread(self.multi_client_handler,  (conn, ))
            start_new_thread(self.time_checker, ())
            print('[INFO] no of connections -> ' + str(len(self.conn_check_list)))

    def run(self):
        try:    
            self.establish_conn()
        except:
            print('[INFO] server is now closed due to TIMEOUT')



s = Server('192.168.1.12', 12345)
s.run()