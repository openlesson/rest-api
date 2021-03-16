from socket import socket, AF_INET, SOCK_STREAM
from config import *


with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Wait for connection...')
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(BUFFER)
            print("Receive", data.decode('utf-8'))
            if not data:
                break
            conn.sendall(data)
