from socket import socket, AF_INET, SOCK_STREAM
import sys
from jim.utils import get_message, send_message
from jim.config import *
import time


def create_presence(account_name="Guest"):
    if not isinstance(account_name, str):
        raise TypeError
    if len(account_name) > 25:
        raise UsernameTooLongError(account_name)
    message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }

    return message


def translate_message(response):
    if not isinstance(response, dict):
        raise TypeError
    if RESPONSE not in response:
        raise MandatoryKeyError(RESPONSE)
    code = response[RESPONSE]

    if len(str(code)) != 3:
        raise ResponseCodeLenError(code)

    if code not in RESPONSE_CODES:
        raise ResposeCodeError(code)

    return response

if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)
    try:
        addr = sys.argv[1]
    except IndexError:
        addr = 'localhost'
    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 7777
    except ValueError:
        print('Порт должен быть целым числом')
        sys.exit()

    client.connect((addr, port))
    presence = create_presence()
    send_message(client, presence)
    response = get_message(client)
    response = translate_message(response)
    print(response)
