import time
from queue import Empty
from threading import Thread

from PythonClient.constants import TASK_SLEEP_TIME


class Worker(Thread):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.client = kwargs['client']

    def run(self):
        while self.client.alive:
            try:
                task = self.client.work_queue.get()
                self.completeTask(task)
            except Empty:
                time.sleep(TASK_SLEEP_TIME)

    def completeTask(self, task):
        pass # TODO
