__author__ = 'Мишин Егор Олегович'

from socket import socket, AF_INET, SOCK_STREAM
import sys
from jim.utils import get_message, send_message
from jim.config import *
import time
from errors import UsernameTooLongError, ResponseCodeLenError, MandatoryKeyError, ResponseCodeError
import threading
import logging
# import log.client_log_config
from log.decorator import Logger


logger = logging.getLogger('client')
log = Logger(logger)



@log
def create_presence(account_name="Guest"):      # функция формирования сообщения
    if not isinstance(account_name, str):   # Генерируем ошибку передан неверный тип
        raise TypeError

    if len(account_name) > 25:      # Если длина имени пользователя больше 25 символов
        raise UsernameTooLongError(account_name)  # генерируем нашу ошибку имя пользователя слишком длинное

    message = {              # формируем словарь сообщения, если все хорошо
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
        raise TypeError         # Нет ключа response

    if RESPONSE not in response:        # Ошибка нужен обязательный ключ
        raise MandatoryKeyError(RESPONSE)

    code = response[RESPONSE]   # получаем код ответа, если все хорошо
    # длина кода не 3 символа
    if len(str(code)) != 3:          # Ошибка неверная длина кода ошибки
        raise ResponseCodeLenError(code)

    if code not in RESPONSE_CODES:         # неправильные коды символов
        raise ResponseCodeError(code)     # ошибка неверный код ответа

    return response


def read_messages(client, account_name):
    """
    Клиент читает входящие сообщения в бесконечном цикле
    :param client: сокет клиента
    """
    while True:
        message = get_message(client)        # читаем сообщение
        # print(message)
        print(message['message'])


def create_message(message_to, text, account_name='Guest'):
    return {ACTION: MSG, TIME: time.time(), TO: message_to, FROM: account_name, MESSAGE: text}


# def write_messages(client):
#     """Клиент пишет сообщение в бесконечном цикле"""
#     while True:
#         # Вводим сообщение с клавиатуры
#         text = input(':)>')
#         # Создаем jim сообщение
#         message = create_message('#all', text)
#         # отправляем на сервер
#         send_message(client, message)


if __name__ == '__main__':
    # Создать TCP-сокет клиента
    client = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    # Пытаемся получить параметры скрипта
    # Получаем аргументы скрипта
    #------------ip-адрес-----------#
    # если ip-адрес указан в параметрах -p <addr>
    try:
        addr = sys.argv[1]
    # если ip-адрес не указан в параметрах
    except IndexError:
        addr = 'localhost'
    #--------------порт-------------#
    # если порт указан в параметрах
    try:
        port = int(sys.argv[2])
    # если порт не указан в параметрах
    except IndexError:
        port = 7777
    # если порт - не целое число
    except ValueError:
        print('Порт должен быть целым числом')
        sys.exit(0)
    try:
        mode = sys.argv[3]
    except IndexError:
        mode = 'r'
    try:
        account_name = sys.argv[4]
        print(account_name)
    except IndexError:
        print('Укажите получателя')
        #sys.exit(0)
    #print(sys.argv)
    # ДАННЫЕ ПОЛУЧИЛИ -> СОЕДИНЯЕМСЯ С СЕРВЕРОМ
    # Соединиться с сервером
    client.connect((addr, port))
    # Сформировать сообщение серверу
    #account_name = 'Console0'
    presence = create_presence(account_name)
    # Отправить сообщение серверу
    send_message(client, presence)
    # Получить ответ сервера
    response = get_message(client)
    # Разобрать ответ сервера
    response = translate_message(response)
    #print(response)
    if response['response'] == OK:
        t = threading.Thread(target=read_messages, args=(client, account_name))
        t.start()

        while True:
            message_str = input('-->')
            if message_str.startswith('message'):
                params = message_str.split()
                try:
                    to = params[1]
                    text = params[2]
                except IndexError:
                    print('Не задан получатель или текст сообщения')
                else:
                    message = create_message(to, text, account_name)
                    send_message(client, message)

            elif message_str == 'help':
                print('message <получатель> <текст> - отправить сообщение, '
                      'Список получателей: Console[0-9]')
            elif message_str == 'exit':
                break
            else:
                print('Неверная команда, для справки введите help')

        client.disconnect()