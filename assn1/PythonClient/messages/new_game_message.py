from PythonClient.messages.message import Message


class NewGameMessage(Message):
    def __init__(self, *args):
        super().__init__()
        self.a_number = args[1]
        self.last_name = args[2]
        self.first_name = args[3]
        self.alias = args[4]

    def encode(self):
        return self._encodeArgs(self.id, self.last_name, self.first_name, self.alias)

    def decode(self):
        pass
