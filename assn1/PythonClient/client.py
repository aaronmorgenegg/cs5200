import socket

from PythonClient.constants import HOST, PORT


class Client:
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect((HOST, PORT))
            # s.sendall(b'Hello, world')
            # data = s.recv(1024)
        # print('Received', repr(data))
