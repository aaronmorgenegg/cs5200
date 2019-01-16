from PythonClient.messages.message import Message


class NewGameMessage(Message):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.a_number = kwargs['user_a_number']
        self.last_name = kwargs['user_last_name']
        self.first_name = kwargs['user_first_name']
        self.alias = kwargs['user_alias']

    def encode(self):
        return self._encodeArgs(self.id, self.a_number, self.last_name, self.first_name, self.alias)
