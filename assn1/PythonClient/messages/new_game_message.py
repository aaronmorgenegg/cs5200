from PythonClient.messages.message import Message, encodeString


class NewGameMessage(Message):
    def __init__(self, *args):
        super().__init__()
        self.a_number = args[1]
        self.last_name = args[2]
        self.first_name = args[3]
        self.alias = args[4]

    def encode(self):
        data = self.id.to_bytes(2, byteorder="big")
        data += encodeString(self.last_name)
        data += encodeString(self.first_name)
        data += encodeString(self.alias)

        return data

    def decode(self):
        pass
