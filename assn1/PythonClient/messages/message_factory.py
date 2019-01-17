import logging

from PythonClient.constants import MESSAGE_ID_NEW_GAME, MESSAGE_ID_GAME_DEF, MESSAGE_ID_GUESS, MESSAGE_ID_ANSWER, \
    MESSAGE_ID_GET_HINT, MESSAGE_ID_EXIT, MESSAGE_ID_ACK, MESSAGE_ID_ERROR, MESSAGE_ID_HEARTBEAT, MESSAGE_ID_HINT
from PythonClient.messages.ack_message import AckMessage
from PythonClient.messages.answer_message import AnswerMessage
from PythonClient.messages.error_message import ErrorMessage
from PythonClient.messages.exit_message import ExitMessage
from PythonClient.messages.game_def_message import GameDefMessage
from PythonClient.messages.get_hint_message import GetHintMessage
from PythonClient.messages.guess_message import GuessMessage
from PythonClient.messages.heartbeat_message import HeartbeatMessage
from PythonClient.messages.hint_message import HintMessage
from PythonClient.messages.new_game_message import NewGameMessage


class MessageFactory:
    MESSAGE_TYPES = {
        MESSAGE_ID_NEW_GAME: NewGameMessage,
        MESSAGE_ID_GAME_DEF: GameDefMessage,
        MESSAGE_ID_GUESS: GuessMessage,
        MESSAGE_ID_ANSWER: AnswerMessage,
        MESSAGE_ID_GET_HINT: GetHintMessage,
        MESSAGE_ID_HINT: HintMessage,
        MESSAGE_ID_EXIT: ExitMessage,
        MESSAGE_ID_ACK: AckMessage,
        MESSAGE_ID_ERROR: ErrorMessage,
        MESSAGE_ID_HEARTBEAT: HeartbeatMessage
    }

    ARG_ORDER = {
        MESSAGE_ID_NEW_GAME: ["string", "string", "string", "string"],
        MESSAGE_ID_GAME_DEF: ["int", "string", "string"],
        MESSAGE_ID_GUESS: ["int", "string"],
        MESSAGE_ID_ANSWER: ["int", "bool", "int", "string"],
        MESSAGE_ID_GET_HINT: ["int"],
        MESSAGE_ID_HINT: ["int", "string"],
        MESSAGE_ID_EXIT: ["int"],
        MESSAGE_ID_ACK: ["int"],
        MESSAGE_ID_ERROR: ["int", "string"],
        MESSAGE_ID_HEARTBEAT: ["int"]
    }

    @staticmethod
    def build(*args, **kwargs):
        logging.debug("Message Factory building message with id: {}".format(args[0]))
        message = MessageFactory.MESSAGE_TYPES[args[0]](*args, **kwargs)
        return message

    @staticmethod
    def buildFromBytes(bytestring):
        """Build a message from a byte string"""
        logging.info("Message Factory building message from bytes: {}".format(bytestring))
        args = MessageFactory._decodeBytes(bytestring)
        if args[0] == MESSAGE_ID_HEARTBEAT:
            return MessageFactory.build(args[0], game_id=args[1])
        elif args[0] == MESSAGE_ID_GAME_DEF:
            return MessageFactory.build(args[0], game_id=args[1], game_hint=args[2], game_definition=args[3])
        elif args[0] == MESSAGE_ID_ERROR:
            return MessageFactory.build(args[0], game_id=args[1], error_text=args[2])
        elif args[0] == MESSAGE_ID_ANSWER:
            return MessageFactory.build(args[0], game_id=args[1], game_result=args[2], game_score=args[3], game_hint=args[4])
        elif args[0] == MESSAGE_ID_GET_HINT:
            return MessageFactory.build(args[0], game_id=args[1])
        elif args[0] == MESSAGE_ID_ACK:
            return MessageFactory.build(args[0], game_id=args[1])
        elif args[0] == MESSAGE_ID_EXIT:
            return MessageFactory.build(args[0], game_id=args[1])
        elif args[0] == MESSAGE_ID_GUESS:
            return MessageFactory.build(args[0], game_id=args[1], game_guess=args[2])
        elif args[0] == MESSAGE_ID_HINT:
            return MessageFactory.build(args[0], game_id=args[1], game_hint=args[2])
        else:
            print("Error: No message handling")
            logging.error("Message Factory no message handling for message with id: {}".format(args[0]))

    @staticmethod
    def _decodeBytes(bytestring):
        byte_list = list(bytestring)
        message_id = MessageFactory._decodeInt(byte_list)
        arg_order = MessageFactory.ARG_ORDER[message_id]
        args = [message_id]
        for arg in arg_order:
            if arg == "bool": args.append(MessageFactory._decodeBool(byte_list))
            elif arg == "int": args.append(MessageFactory._decodeInt(byte_list))
            elif arg == "string": args.append(MessageFactory._decodeString(byte_list))
        return args

    @staticmethod
    def _decodeBool(byte_list):
        bytestring = "{}".format(byte_list.pop(0))
        return bool(int(bytestring))

    @staticmethod
    def _decodeInt(byte_list):
        bytestring = "{}{}".format(byte_list.pop(0), byte_list.pop(0))
        return int(bytestring)

    @staticmethod
    def _decodeChar(byte_list):
        return chr(MessageFactory._decodeInt(byte_list))

    @staticmethod
    def _decodeString(byte_list):
        length = MessageFactory._decodeInt(byte_list)//2
        string = ""
        for i in range(length):
            string += MessageFactory._decodeChar(byte_list)
        return string
