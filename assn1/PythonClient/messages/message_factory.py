from PythonClient.constants import MESSAGE_ID_NEW_GAME, MESSAGE_ID_GAME_DEF, MESSAGE_ID_GUESS, MESSAGE_ID_ANSWER, \
    MESSAGE_ID_GET_HINT, MESSAGE_ID_EXIT, MESSAGE_ID_ACK, MESSAGE_ID_ERROR, MESSAGE_ID_HEARTBEAT
from PythonClient.messages.new_game_message import NewGameMessage


class MessageFactory:
    MESSAGE_TYPES = {
        MESSAGE_ID_NEW_GAME: NewGameMessage,
        MESSAGE_ID_GAME_DEF: GameDefMessage,
        MESSAGE_ID_GUESS: GuessMessage,
        MESSAGE_ID_ANSWER: AnswerMessage,
        MESSAGE_ID_GET_HINT: GetHintMessage,
        MESSAGE_ID_EXIT: ExitMessage,
        MESSAGE_ID_ACK: AckMessage,
        MESSAGE_ID_ERROR: ErrorMessage,
        MESSAGE_ID_HEARTBEAT: HeartbeatMessage
    }

    @staticmethod
    def build(message_type, *args):
        message = MessageFactory.MESSAGE_TYPES[message_type](args)
        return message
