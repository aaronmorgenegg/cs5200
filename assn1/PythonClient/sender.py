import socket
from threading import Thread

from PythonClient.constants import SERVER_HOST, SERVER_PORT


class Sender(Thread):
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect((SERVER_HOST, SERVER_PORT))
            s.sendall(b'Hello, world')
            data = s.recv(1024)
            print('Received', repr(data))
