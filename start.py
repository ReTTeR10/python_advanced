__author__ = 'Мишин Егор Олегович'
# Служебный скрипт запуска/останова нескольких клиентских приложений

from subprocess import Popen, CREATE_NEW_CONSOLE
import time

# список запущенных процессов
p_list = []

while True:
    answer = input("Запустить сервер и клиентов (y) / Выйти (q)")

    if answer == 'y':
        # запускаем сервер
        # Запускаем серверный скрипт и добавляем его в список процессов
        p_list.append(Popen('python -i server.py',
                            creationflags=CREATE_NEW_CONSOLE))
        print('Сервер запущен')
        time.sleep(1)

        # запускаем клиентов
        CONSOLE_COUNT = 2

        for i in range(CONSOLE_COUNT):
            # Запускаем клиентский скрипт и добавляем его в список процессов
            client_name = f'Console{i}'
            p_list.append(Popen(f'python -i client.py localhost 7777 r {client_name}',
                            creationflags=CREATE_NEW_CONSOLE))
        print('Клиенты запущены')

    elif answer == 'q':
        print(f'Открыто процессов {len(p_list)}')

        for p in p_list:
            print('Закрываю {p}')
            p.kill()
        p_list.clear()
        print('Выхожу')

        break
