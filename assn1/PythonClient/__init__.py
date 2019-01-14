import socket
from threading import Thread

from PythonClient.constants import DEFAULT_SERVER_HOST, DEFAULT_SERVER_PORT


class Sender(Thread):
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect((DEFAULT_SERVER_HOST, DEFAULT_SERVER_PORT))
            s.sendall(b'Hello, world')
            data = s.recv(1024)
            print('Received', repr(data))
