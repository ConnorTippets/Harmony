import socket
import os
import json
clear = lambda: os.system("cls")
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
ready = False
while not ready:
    with open('names.json', 'r') as f:
        names = json.load(f)
        f.close()
    if not names == {}:
        ready = True
    else:
        continue

x = False
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            if not x:
                print(names.get(addr[0]) + " has connected.")
                x = True
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(names.get(addr[0])+" sent '"+data.decode() + "'")
                conn.sendall(data)
