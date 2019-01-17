from PythonClient.messages.message import Message


class HintMessage(Message):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_id = kwargs['game_id']
        self.game_hint = kwargs['game_hint']
