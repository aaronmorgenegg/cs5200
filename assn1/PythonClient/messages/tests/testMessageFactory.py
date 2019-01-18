import unittest

from PythonClient.constants import MESSAGE_ID_ACK, MESSAGE_ID_NEW_GAME, MESSAGE_ID_ERROR, MESSAGE_ID_GUESS, \
    MESSAGE_ID_GAME_DEF
from PythonClient.messages.ack_message import AckMessage
from PythonClient.messages.error_message import ErrorMessage
from PythonClient.messages.game_def_message import GameDefMessage
from PythonClient.messages.message_factory import MessageFactory
from PythonClient.messages.new_game_message import NewGameMessage


class TestMessageFactory(unittest.TestCase):
    def testBuildValidMessage(self):
        """Test MessageFactory.build() method with valid parameters"""
        # Test Ack Message
        message_id = MESSAGE_ID_ACK
        game_id = 5
        expected = AckMessage(message_id, game_id=game_id)
        actual = MessageFactory.build(message_id, game_id=game_id)
        self.assertEqual(expected.id, actual.id)
        self.assertEqual(expected.game_id, actual.game_id)

        # Test New Game Message
        message_id = MESSAGE_ID_NEW_GAME
        user_a_number = "A0000001"
        user_last_name = "Smith"
        user_first_name = "John"
        user_alias = "js"
        expected = NewGameMessage(message_id, user_a_number=user_a_number, user_last_name=user_last_name,
                                  user_first_name=user_first_name, user_alias=user_alias)
        actual = MessageFactory.build(message_id, user_a_number=user_a_number, user_last_name=user_last_name,
                                      user_first_name=user_first_name, user_alias=user_alias)
        self.assertEqual(expected.id, actual.id)
        self.assertEqual(expected.a_number, actual.a_number)
        self.assertEqual(expected.last_name, actual.last_name)
        self.assertEqual(expected.first_name, actual.first_name)
        self.assertEqual(expected.alias, actual.alias)

        # Test Error Message
        message_id = MESSAGE_ID_ERROR
        game_id = 5
        error_text = "Test Error Message"
        expected = ErrorMessage(message_id, game_id=game_id, error_text=error_text)
        actual = MessageFactory.build(message_id, game_id=game_id, error_text=error_text)
        self.assertEqual(expected.id, actual.id)
        self.assertEqual(expected.game_id, actual.game_id)
        self.assertEqual(expected.error_text, actual.error_text)

    def testBuildInvalidMessage(self):
        """Test MessageFactory.build() with invalid parameters"""
        # Test Game Guess with missing arguments
        message_id = MESSAGE_ID_GUESS
        self.assertRaises(KeyError, MessageFactory.build, message_id)

        # Test Game Guess with wrong arguments
        message_id = MESSAGE_ID_GUESS
        game_id=5
        game_hint="test"
        self.assertRaises(KeyError, MessageFactory.build, message_id, game_id=game_id, game_hint=game_hint)

    def testBuildFromBytesValidMessage(self):
        """Test MessageFactory.buildFromBytes() with valid parameters"""
        # Test Game Def with valid bytestring
        bytestring = b'\x00\x02\x00\x05\x00\x0c\x00_\x00_\x00_\x00_\x00_\x00_\x00"\x00A\x00 \x00T\x00e\x00s\x00t\x00 \x00D\x00e\x00f\x00i\x00n\x00i\x00t\x00i\x00o\x00n'

        message_id = MESSAGE_ID_GAME_DEF
        game_id = 5
        game_hint = "______"
        game_definition = "A Test Definition"
        expected = GameDefMessage(message_id, game_id=game_id, game_hint=game_hint, game_definition=game_definition)
        actual = MessageFactory.buildFromBytes(bytestring)
        self.assertEqual(expected.id, actual.id)
        self.assertEqual(expected.game_id, actual.game_id)
        self.assertEqual(expected.game_hint, actual.game_hint)
        self.assertEqual(expected.game_definition, actual.game_definition)
