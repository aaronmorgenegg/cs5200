

def encodeString(string):
    """Takes a python string and returns the proper encoding:
    2 bytes(length #), 2 bytes(char 1), 2 bytes(char 2)... 2 bytes(char n)
    """
    length = len(string)
    data = length.to_bytes(2, byteorder="big")
    for char in string:
        ord_char = ord(char)
        data += ord_char.to_bytes(2, byteorder="big")
    return data

class Message:
    def __init__(self, *args):
        self.id = args[0]

    def encode(self):
        pass

    def decode(self):
        pass
