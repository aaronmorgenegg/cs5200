import unittest

from PythonClient.constants import MESSAGE_ID_GUESS, MESSAGE_ID_NEW_GAME
from PythonClient.messages.message_factory import MessageFactory


class TestMessage(unittest.TestCase):
    def testEncode(self):
        # Game Guess message
        expected = b'\x00\x03\x00\x05\x00\x08\x00t\x00e\x00s\x00t'
        message_id = MESSAGE_ID_GUESS
        game_id = 5
        game_guess = "test"
        game_def_message = MessageFactory.build(message_id, game_id=game_id, game_guess=game_guess)
        actual = game_def_message.encode()
        self.assertEqual(expected, actual)

        # New Game message
        expected = b'\x00\x01\x00\x0e\x00A\x000\x000\x000\x000\x000\x001\x00\x06\x00b\x00a\x00r\x00\x06\x00f\x00o\x00o\x00\x04\x00f\x00b'
        message_id = MESSAGE_ID_NEW_GAME
        a_number = "A000001"
        last_name = "bar"
        first_name = "foo"
        alias = "fb"
        new_game_message = MessageFactory.build(message_id, user_last_name=last_name, user_first_name=first_name,
                                                user_alias=alias, user_a_number=a_number)
        actual = new_game_message.encode()
        self.assertEqual(expected, actual)
