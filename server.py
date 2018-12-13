__author__ = 'Мишин Егор Олегович'

import sys
import json
from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import get_message, send_message
from jim.config import *

import logging
import log.server_log_config
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
            # Добавляем их в список
            # В идеале нам нужно сделать еще проверку, что сообщение нужного формата прежде чем его пересылать!
            # Пока оставим как есть, этим займемся позже
            messages.append(message)
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)

    # Возвращаем словарь сообщений
    return messages



def write_responses(messages, w_clients, all_clients):
    """
    Отправка сообщений тем клиентам, которые их ждут
    :param messages: список сообщений
    :param w_clients: клиенты которые читают
    :param all_clients: все клиенты
    :return:
    """

    for sock in w_clients:
        # Будем отправлять каждое сообщение всем
        for message in messages:
            try:
                # Отправить на тот сокет, который ожидает отправки
                send_message(sock, message)
            except:  # Сокет недоступен, клиент отключился
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)

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
        addr = sys.argv[1]
    except IndexError:
        addr = ''
    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 10000
    except ValueError:
        print('Порт должен быть целым числом')
        sys.exit(0)

    server.bind((addr, port))
    server.listen(15)
    server.settimeout(0.2)
    clients = []
    while True:
        try:
            conn, addr = server.accept()  # Проверка подключений
            # получаем сообщение от клиента
            presence = get_message(conn)
            # формируем ответ
            response = presence_response(presence)
            # отправляем ответ клиенту
            send_message(conn, response)
        except OSError as e:
            pass  # timeout вышел
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            # Добавляем клиента в список
            clients.append(conn)
        finally:
            # Проверить наличие событий ввода-вывода
            wait = 0
            r = []
            w = []
        try:
            r, w, e = select.select(clients, clients, [], wait)
        except:
            pass  # Ничего не делать, если какой-то клиент отключился

        requests = read_requests(r, clients)  # Получаем входные сообщения
        write_responses(requests, w, clients)  # Выполним отправку входящих сообщений

