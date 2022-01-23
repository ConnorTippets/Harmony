import socket
import os

clear = lambda: os.system("cls")
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

x = False
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            if not x:
                print('Connected by', addr)
                x = True
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(addr[0]+" sent "+data.decode())
                conn.sendall(data)
