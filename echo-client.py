import socket
import os

clear = lambda: os.system("cls")

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        ini = str(input(""))
        s.sendall(bytes(''+ini+'', "UTF-8"))
        data = s.recv(1024)
