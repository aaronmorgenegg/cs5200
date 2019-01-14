import socket
from threading import Thread

from PythonClient.constants import SERVER_HOST, SERVER_PORT


class Receiver(Thread):
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect((SERVER_HOST, SERVER_PORT))
            while True:
                s.recv(1024)
