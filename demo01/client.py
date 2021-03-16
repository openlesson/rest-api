from socket import socket, AF_INET, SOCK_STREAM
from config import *

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, World')
    data = s.recv(BUFFER)
    print("Response from server", data.decode('utf-8'))