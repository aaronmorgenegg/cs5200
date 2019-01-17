
DEFAULT_SERVER_HOST = '127.0.0.1'  # The server's hostname or IP address
DEFAULT_SERVER_PORT = 12001        # The port used by the server

DEFAULT_A_NUMBER    = 'A00000001'
DEFAULT_FIRST_NAME  = 'John'
DEFAULT_LAST_NAME   = 'Smith'
DEFAULT_ALIAS       = 'js'

# Message ID's
MESSAGE_ID_NEW_GAME  = 1
MESSAGE_ID_GAME_DEF  = 2
MESSAGE_ID_GUESS     = 3
MESSAGE_ID_ANSWER    = 4
MESSAGE_ID_GET_HINT  = 5
MESSAGE_ID_HINT      = 6
MESSAGE_ID_EXIT      = 7
MESSAGE_ID_ACK       = 8
MESSAGE_ID_ERROR     = 9
MESSAGE_ID_HEARTBEAT = 10

SLEEP_TIME = .05 # in seconds, sleep time after checking empty queues for workers/senders/receivers

LOG_LEVEL = 10 # [10,20,30,40,50] [debug, info, warning, error, critical]
LOG_FILE = "PythonClient.log"
