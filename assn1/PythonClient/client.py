from threading import Thread

from PythonClient.constants import DEFAULT_FIRST_NAME, DEFAULT_LAST_NAME, DEFAULT_A_NUMBER, DEFAULT_ALIAS, \
    DEFAULT_SERVER_HOST, DEFAULT_SERVER_PORT, MESSAGE_ID_NEW_GAME
from PythonClient.messages.message_factory import MessageFactory


class Client(Thread):
    def __init__(self):
        super().__init__()

        self.alive = True

        self.COMMAND_MAP = {
            'help': self.help,
            'exit': self.exit,
            'info': self.info,
            'user': self.updateUser,
            'server': self.updateServer,
            'new game': self.newGame
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

    def exit(self):
        self.alive = False

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
        print("-"*30)

    def updateUser(self):
        """Update user information such as first/last name, A#, or alias"""
        self.user['first_name'] = input("Enter First Name: ")
        self.user['last_name'] = input("Enter Last Name: ")
        self.user['a_number'] = input("Enter A Number: ")
        self.user['alias'] = input("Enter Alias: ")

    def updateServer(self):
        """Update server information such as host and port"""
        self.server['host'] = input("Enter server host: ")
        self.server['port'] = input("Enter server port: ")

    def newGame(self):
        """Start a new game"""
        message = MessageFactory.build(MESSAGE_ID_NEW_GAME, self.user['a_number'], self.user['last_name'],
                                       self.user['first_name'], self.user['alias'])

    def sendMessage(self, message):
        """Send a message to the server"""
        pass # TODO
