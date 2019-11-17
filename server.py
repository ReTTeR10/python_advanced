__author__ = 'Мишин Егор Олегович'

import sys
import json
from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import get_message, send_message
from jim.config import *

import logging
import log.server_log_config
from log.decorator import Logger
# Получаем серверный логгер по имени, он уже объявлен в server_log_config и настроен
logger = logging.getLogger('server')
log = Logger(logger)


@log
# функция формирования ответа
def presence_response(presence_message):
    if ACTION in presence_message and \
        presence_message[ACTION] == PRESENCE and \
        TIME in presence_message and \
        isinstance(presence_message[TIME], float):
            return {RESPONSE: 200}
    else:
        return {RESPONSE: 400, ERROR: 'Неверный запрос'}


if __name__ == '__main__':
    server = socket(AF_INET, SOCK_STREAM)
    try:
        port = int(sys.argv[1])
    except IndexError:
        addr = ''
    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 7777
    except ValueError:
        print('Порт должен быть целым числом')
        sys.exit()

    server.bind((addr, port))
    server.listen(5)
    while True:
        client, addr = server.accept()
        presence = get_message(client)
        print(presence)
        response = presence_response(presence)
        send_message(client, response)
        client.close()
