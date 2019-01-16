


class Message:
    def __init__(self, *args, **kwargs):
        self.id = args[0]

    def encode(self):
        pass

    def _encodeArgs(self, *args):
        data = b''
        for arg in args:
            if isinstance(arg, int):
                data += self._encodeInt(arg)
            elif isinstance(arg, str):
                data += self._encodeString(arg)

        return data

    def _encodeInt(self, int):
        return int.to_bytes(2, byteorder="big")

    def _encodeString(self, string):
        """Takes a python string and returns the proper encoding:
        2 bytes(length #), 2 bytes(char 1), 2 bytes(char 2)... 2 bytes(char n)
        """
        length = len(string)
        data = length.to_bytes(2, byteorder="big")
        for char in string:
            ord_char = ord(char)
            data += ord_char.to_bytes(2, byteorder="big")
        return data
