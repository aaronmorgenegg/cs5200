from PythonClient.messages.message import Message


class AnswerMessage(Message):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_id = kwargs['game_id']
        self.game_result = kwargs['game_result']
        self.game_hint = kwargs['game_hint']
        self.game_score = kwargs['game_score']
