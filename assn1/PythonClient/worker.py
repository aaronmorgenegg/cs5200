import time
from queue import Empty
from threading import Thread

from PythonClient.constants import SLEEP_TIME, MESSAGE_ID_ANSWER, MESSAGE_ID_ERROR, MESSAGE_ID_GAME_DEF, MESSAGE_ID_ACK


class Worker(Thread):

    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.client = kwargs['client']

        self.TASK_MAP = {
            MESSAGE_ID_ANSWER: self._completeAnswerTask,
            MESSAGE_ID_ERROR: self._completeErrorTask,
            MESSAGE_ID_GAME_DEF: self._completeGameDefTask,
            MESSAGE_ID_ACK: self._completeAckTask
        }

    def run(self):
        while self.client.alive:
            try:
                task = self.client.work_queue.get(block=False)
                self._completeTask(task)
            except Empty:
                time.sleep(SLEEP_TIME)

    def _completeTask(self, task):
        self.TASK_MAP[task.id](task)

    def _completeAnswerTask(self, task):
        if task.result == 1:
            print("Correct. Score: {}".format(task.score))
        elif task.result == 0:
            print("Incorrect.")
        self.client.game['guess'] = task.hint

    def _completeErrorTask(self, task):
        print(task.error_text)

    def _completeGameDefTask(self, task):
        self.client.game['id'] = task.game_id
        self.client.game['guess'] = task.game_hint
        self.client.game['definition'] = task.game_definition

    def _completeAckTask(self, task):
        self.client.alive = False
