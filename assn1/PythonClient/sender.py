import time
from queue import Queue, Empty
from threading import Thread

from PythonClient.constants import SLEEP_TIME


class Sender(Thread):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.client = kwargs['client']
        self.socket = kwargs['socket']
        self.message_queue = Queue()

    def run(self):
        while self.client.alive:
            try:
                message = self.message_queue.get(block=False)
                self._sendMessage(message)
            except Empty:
                time.sleep(SLEEP_TIME)

    def enqueueMessage(self, message):
        self.message_queue.put(message)

    def _sendMessage(self, message):
        self.socket.send(message.encode())
