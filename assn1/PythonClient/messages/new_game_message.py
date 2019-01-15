from PythonClient.messages.message import Message


class NewGameMessage(Message):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.a_number = kwargs['a_number']
        self.last_name = kwargs['last_name']
        self.first_name = kwargs['first_name']
        self.alias = kwargs['alias']

    def encode(self):
        return self._encodeArgs(self.id, self.a_number, self.last_name, self.first_name, self.alias)

    def decode(self):
        pass
