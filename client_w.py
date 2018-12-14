from socket import socket, AF_INET, SOCK_STREAM
from client import create_presence, translate_message, read_messages, write_messages
from jim.utils import send_message, get_message
from jim.config import *

client = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
addr = 'localhost'
port = 7777
mode = 'w'
# Соединиться с сервером
client.connect((addr, port))
# Создаем сообщение
presence = create_presence()
# Отсылаем сообщение
send_message(client, presence)
# Получаем ответ
response = get_message(client)
# Проверяем ответ
response = translate_message(response)
if response['response'] == OK:
    # в зависимости от режима мы будем или слушать или отправлять сообщения
    if mode == 'r':
        read_messages(client)
    elif mode == 'w':
        write_messages(client)
    else:
        raise Exception('Не верный режим чтения/записи')