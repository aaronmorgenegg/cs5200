import logging
import socket
import time
from threading import Thread

from PythonClient.constants import MESSAGE_ID_HEARTBEAT, MESSAGE_ID_ACK, SLEEP_TIME
from PythonClient.messages.message_factory import MessageFactory


class Receiver(Thread):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.client = kwargs['client']
        self.socket = kwargs['socket']

    def run(self):
        while self.client.alive:
            try:
                buf = self.socket.recv(1024)
                if len(buf) > 0:
                    logging.info("Receiver received bytes: {}".format(buf))
                    response = self._decodeBuffer(buf)
                    if response is not None:
                        self.client.enqueueTask(response)
            except socket.error:
                time.sleep(SLEEP_TIME)

    def setSocket(self, socket):
        self.socket = socket

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
        logging.info("Receiver responding to heartbeat.")
        if self.client.game['id'] is None: return
        message = MessageFactory.build(MESSAGE_ID_ACK, game_id=self.client.game['id'])
        logging.info("Receiver sending bytes: {}".format(message.encode()))
        self.socket.send(message.encode())
