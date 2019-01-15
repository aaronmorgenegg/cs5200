from PythonClient.constants import DEFAULT_FIRST_NAME, DEFAULT_LAST_NAME, DEFAULT_A_NUMBER, DEFAULT_ALIAS, \
    DEFAULT_SERVER_HOST, DEFAULT_SERVER_PORT, MESSAGE_ID_NEW_GAME
from PythonClient.messages.message_factory import MessageFactory


class Client:
    def __init__(self):
        self.COMMAND_MAP = {'user': self.updateUser,
                            'server': self.updateServer,
                            'new game': self.newGame}

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

    def help(self):
        """Display a help menu for the client"""
        print("-----COMMANDS-----")
        print("user - input new information about the user, such as first/last name, A#, or alias")
        print("server - input new information about the server, such as host and port")

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
