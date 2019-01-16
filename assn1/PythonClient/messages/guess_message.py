from PythonClient.messages.message import Message


class GuessMessage(Message):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_id = kwargs['game_id']
        self.game_guess = kwargs['game_guess']

    def encode(self):
        return self._encodeArgs(self.id, self.game_id, self.game_guess)
