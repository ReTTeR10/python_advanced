__author__ = 'Мишин Егор Олегович'

from socket import socket, AF_INET, SOCK_STREAM
import sys
from jim.utils import get_message, send_message
from jim.config import *
import time
from errors import UsernameTooLongError, ResponseCodeLenError, MandatoryKeyError, ResponseCodeError

import logging
import log.client_log_config
from log.decorator import Logger
# Получаем по имени клиентский логгер, он уже нестроен в client_log_config
logger = logging.getLogger('client')
log = Logger(logger)


# функция формирования сообщения
@log
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

@log
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


def read_messages(client):
    """
    Клиент читает входящие сообщения в бесконечном цикле
    :param client: сокет клиента
    """
    while True:
        # читаем сообщение
        print('Читаю')
        message = get_message(client)
        print(message)
        # там должно быть сообщение всем
        print(message[MESSAGE])


def create_message(message_to, text, account_name='Guest'):
    return {ACTION: MSG, TIME: time.time(), TO: message_to, FROM: account_name, MESSAGE: text}


def write_messages(client):
    """Клиент пишет сообщение в бесконечном цикле"""
    while True:
        # Вводим сообщение с клавиатуры
        text = input(':)>')
        # Создаем jim сообщение
        message = create_message('#all', text)
        # отправляем на сервер
        send_message(client, message)


if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
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
        sys.exit(0)
    try:
        mode = sys.argv[3]
    except IndexError:
        mode = 'r'
    client.connect((addr, port))
    presence = create_presence()
    send_message(client, presence)
    response = get_message(client)
    response = translate_message(response)
    if response['response'] == OK:
        if mode == 'r':
            read_messages(client)
        elif mode == 'w':
            write_messages(client)
        else:
            raise Exception('Не верный режим чтения/записи')
