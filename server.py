__author__ = 'Мишин Егор Олегович'

import sys
# import json
from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import get_message, send_message
from jim.config import *
import select

import logging
# import log.server_log_config
from log.decorator import Logger
logger = logging.getLogger('server')
log = Logger(logger)

def read_requests(r_clients, all_clients):
    """
    Чтение сообщений, которые будут посылать клиенты
    :param r_clients: клиенты которые могут отправлять сообщения
    :param all_clients: все клиенты
    :return:
    """
    # Список входящих сообщений
    messages = []

    for sock in r_clients:
        try:
            # Получаем входящие сообщения
            message = get_message(sock)
            print(message)
            # Добавляем их в список
            # В идеале нам нужно сделать еще проверку, что сообщение нужного формата прежде чем его пересылать!
            # Пока оставим как есть, этим займемся позже
            messages.append((message, sock))
        except:
            print(f'Клиент {sock.fileno()} {sock.getpeername()} отключился')
            all_clients.remove(sock)

    # Возвращаем словарь сообщений
    return messages



def write_responses(messages):
    """
    Отправка сообщений тем клиентам, которые их ждут
    :param messages: список сообщений
    # :param w_clients: клиенты которые читают
    # :param all_clients: все клиенты
    :return:
    """
    for message, sender in messages:
        if message['action'] == MSG:
                # получаем кому отправить сообщение
                to = message['to']
                sock = names[to]
                msg = message['message']
                send_message(sock, message)

@log
# функция формирования ответа
def presence_response(presence_message):
    if ACTION in presence_message and \
                    presence_message[ACTION] == PRESENCE and \
                    TIME in presence_message and \
            isinstance(presence_message[TIME], float):
        # Если всё хорошо шлем ОК
        return {RESPONSE: 200}
    else:
        # Шлем код ошибки
        return {RESPONSE: 400, ERROR: 'Неверный запрос'}


if __name__ == '__main__':
    server = socket(AF_INET, SOCK_STREAM)
    try:
        addr = sys.argv[1]
    except IndexError:
        addr = ''
    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 7777
    except ValueError:
        print('Порт должен быть целым числом')
        sys.exit(0)

    server.bind((addr, port))
    server.listen(15)
    server.settimeout(0.2)
    clients = []
    names = {}
    while True:
        try:
            conn, addr = server.accept()  # Проверка подключений
            # получаем сообщение от клиента
            presence = get_message(conn)

            # print(presence)
            client_name = presence['user']['account_name']
            # формируем ответ
            response = presence_response(presence)
            # отправляем ответ клиенту
            send_message(conn, response)
        except OSError as e:
            pass  # timeout вышел
        else:
            print(f"Получен запрос на соединение от {str(addr)}")
            names[client_name] = conn

            clients.append(conn)
        finally:
            # Проверить наличие событий ввода-вывода
            wait = 0
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass  # Eсли какой-то клиент отключился - ничего не делать,

            requests = read_requests(r, clients)  # Получаем входящие сообщения
            write_responses(requests)  # Выполним отправку входящих сообщений

