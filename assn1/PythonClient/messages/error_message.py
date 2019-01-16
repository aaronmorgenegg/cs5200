from PythonClient.messages.message import Message


class ErrorMessage(Message):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_id = kwargs['game_id']
        self.error_text = kwargs['error_text']
