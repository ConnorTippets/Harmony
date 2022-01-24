import socket
import os
import json

with open('names.json', 'r') as f:
    names = json.load(f)
    f.close()
name = names['127.0.0.1']

clear = lambda: os.system("cls")

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        ini = str(input(name + ": "))
        s.sendall(bytes(''+ini+'', "UTF-8"))
        data = s.recv(1024)
