import socket
from threading import Thread

from PythonClient.constants import MESSAGE_ID_HEARTBEAT, MESSAGE_ID_ACK
from PythonClient.messages.message_factory import MessageFactory


class Receiver(Thread):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, *args, **kwargs)
        self.client = kwargs['client']
        self.socket = None

    def run(self):
        self.reconnectSocket()
        while self.client.alive:
            buf = self.socket.recv(1024)
            if len(buf) > 0:
                print(buf)
                response = self._decodeBuffer(buf)
                if response is not None:
                    self.client.enqueueTask(response)

    def reconnectSocket(self):
        if self.socket is not None: self.socket.close()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.connect((self.client.server['host'], self.client.server['port']))

    def _decodeBuffer(self, buf):
        try:
            message = MessageFactory.buildFromBytes(buf)
            if message.id == MESSAGE_ID_HEARTBEAT:
                self._ackHeartbeat()
                message = None
        except KeyError:
            message = None
        return message

    def _ackHeartbeat(self):
        if self.client.game['id'] is None: return
        message = MessageFactory.build(MESSAGE_ID_ACK, game_id=self.client.game['id'])
        self.socket.send(message.encode())
