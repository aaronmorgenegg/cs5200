from PythonClient.messages.message import Message


class AckMessage(Message):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.game_id = kwargs['game_id']

    def encode(self):
        return self._encodeArgs(self.id, self.game_id)

    def decode(self):
        pass
