from queue import Queue
from threading import Thread

from PythonClient.constants import DEFAULT_FIRST_NAME, DEFAULT_LAST_NAME, DEFAULT_A_NUMBER, DEFAULT_ALIAS, \
    DEFAULT_SERVER_HOST, DEFAULT_SERVER_PORT, MESSAGE_ID_NEW_GAME, MESSAGE_ID_GUESS, MESSAGE_ID_GET_HINT, \
    MESSAGE_ID_EXIT, MESSAGE_ID_ACK
from PythonClient.messages.message_factory import MessageFactory
from PythonClient.receiver import Receiver
from PythonClient.sender import Sender
from PythonClient.worker import Worker


class Client(Thread):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)

        self.alive = True

        self.COMMAND_MAP = {
            'help': self.help,
            'exit': self.exit,
            'info': self.info,
            'user': self.updateUser,
            'server': self.updateServer,
            'new game': self.newGame,
            'guess': self.guess,
            'get hint': self.getHint
        }

        self.user = {
            'first_name': DEFAULT_FIRST_NAME,
            'last_name': DEFAULT_LAST_NAME,
            'a_number': DEFAULT_A_NUMBER,
            'alias': DEFAULT_ALIAS
        }

        self.server = {
            'host': DEFAULT_SERVER_HOST,
            'port': DEFAULT_SERVER_PORT
        }

        self.game = {
            'id': None,
            'definition': None,
            'guess': None
        }

        self.work_queue = Queue()

        self.sender = Sender(client=self)
        self.receiver = Receiver(client=self)
        self.worker = Worker(client=self)
        self.sender.start()
        self.receiver.start()
        self.worker.start()

        self.help()

    def run(self):
        while self.alive:
            data = input("Enter Command: ").lower()
            try:
                self.COMMAND_MAP[data]()
            except KeyError:
                print("Error: Invalid Command")

    def help(self):
        """Display a help menu for the client"""
        print("-----COMMANDS-----")
        print("help - display this help menu")
        print("exit - end the program")
        print("info - display info about the program")
        print("user - input new information about the user, such as first/last name, A#, or alias")
        print("server - input new information about the server, such as host and port")
        print("new game - initiate a new game with the server")
        print("guess - submit a word as a guess to the server")
        print("get hint - get a hint about a letter")

    def info(self):
        print("-"*30)
        print("User Information")
        print("First Name  : {}".format(self.user['first_name']))
        print("Last Name   : {}".format(self.user['last_name']))
        print("A Number    : {}".format(self.user['a_number']))
        print("Alias       : {}".format(self.user['alias']))
        print("Server Information")
        print("Host        : {}".format(self.server['host']))
        print("Port        : {}".format(self.server['port']))
        print("Game Information")
        print("ID          : {}".format(self.game['id']))
        print("Guess       : {}".format(self.game['guess']))
        print("Definition  : {}".format(self.game['definition']))
        print("-"*30)

    def updateUser(self):
        """Update user information such as first/last name, A#, or alias"""
        if self.game['id'] is not None:
            print("Error: Cannot modify user information while game is in progress")
            return
        self.user['first_name'] = input("Enter First Name: ")
        self.user['last_name'] = input("Enter Last Name: ")
        self.user['a_number'] = input("Enter A Number: ")
        self.user['alias'] = input("Enter Alias: ")

    def updateServer(self):
        """Update server information such as host and port"""
        if self.game['id'] is not None:
            print("Error: Cannot modify server information while game is in progress")
            return
        self.server['host'] = input("Enter server host: ")
        self.server['port'] = input("Enter server port: ")

    def newGame(self):
        message = MessageFactory.build(MESSAGE_ID_NEW_GAME, user_a_number=self.user['a_number'],
                                       user_last_name=self.user['last_name'], user_first_name=self.user['first_name'],
                                       user_alias=self.user['alias'])
        self.sendMessage(message)

    def guess(self):
        if self.game['id'] is None: return
        message = MessageFactory.build(MESSAGE_ID_GUESS, user_id=self.game['id'], game_guess=self.game['guess'])
        self.sendMessage(message)

    def getHint(self):
        if self.game['id'] is None: return
        message = MessageFactory.build(MESSAGE_ID_GET_HINT, game_id=self.game['id'])
        self.sendMessage(message)

    def exit(self):
        if self.game['id'] is None: return
        message = MessageFactory.build(MESSAGE_ID_EXIT, game_id=self.game['id'])
        self.sendMessage(message)

    def sendMessage(self, message):
        """Send a message to the server"""
        self.sender.enqueueMessage(message)

    def enqueueTask(self, task):
        self.work_queue.put(task)
