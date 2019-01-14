import socket
from threading import Thread

from PythonClient.constants import DEFAULT_SERVER_HOST, DEFAULT_SERVER_PORT


class Receiver(Thread):
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect((DEFAULT_SERVER_HOST, DEFAULT_SERVER_PORT))
            while True:
                s.recv(1024)
