__author__ = 'Мишин Егор Олегович'

'''
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип 
и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление 
в формат Unicode и также проверить тип и содержимое переменных.
'''
print('-----1-----\n')

word_1 = 'разработка'
word_2 = 'сокет'
word_3 = 'декоратор'

print(f'{word_1} - {type(word_1)}, \n{word_2} - {type(word_2)}, \n{word_3} - {type(word_3)}')

word_1_unicode = '\u0440\u0430\u0437\u0440\u0430\u0431\u043E\u0442\u043A\u0430'
word_2_unicode = '\u0441\u043E\u043A\u0435\u0442'
word_3_unicode = '\u0434\u0435\u043A\u043E\u0440\u0430\u0442\u043E\u0440'

print(f'\n Проверка в Unicode:\n'
      f'{word_1_unicode} - {type(word_1_unicode)}, \n{word_2_unicode} - {type(word_2_unicode)},'
      f' \n{word_3_unicode} - {type(word_3_unicode)}\n')

'''

Вывод из print:

разработка - <class 'str'>, 
сокет - <class 'str'>, 
декоратор - <class 'str'>

 Проверка в Unicode:
разработка - <class 'str'>, 
сокет - <class 'str'>, 
декоратор - <class 'str'>
'''


'''
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность 
кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
'''

print('-----2-----\n')

word_1_byte = b'class'
word_2_byte = b'function'
word_3_byte = b'method'

print(f'{word_1_byte}, {type(word_1_byte)}, {len(word_1_byte)}')
print(f'{word_2_byte}, {type(word_2_byte)}, {len(word_2_byte)}')
print(f'{word_3_byte}, {type(word_3_byte)}, {len(word_3_byte)}')
print('\n')
'''

Вывод из print:

b'class', <class 'bytes'>, 5
b'function', <class 'bytes'>, 8
b'method', <class 'bytes'>, 6
'''


'''
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
'''
print('-----3-----\n')

word_1_byte = b'attribute'
# word_2_byte = b'класс'
# word_3_byte = b'функция'
word_4_byte = b'type'

print(f'{word_1_byte}, {type(word_1_byte)},'
    # f'\n{word_2_byte}, {type(word_2_byte)},'
    #  f'\n{word_3_byte}, {type(word_3_byte)},'
      f'\n{word_4_byte}, {type(word_4_byte)},')

'''
Вывод из print:

b'attribute', <class 'bytes'>,

  File "D:/Projects/pyhton_2/1й урок/hw1.py", line 70
    word_2_byte = b'класс'
                 ^
SyntaxError: bytes can only contain ASCII literal characters.

  File "D:/Projects/pyhton_2/1й урок/hw1.py", line 71
    word_3_byte = b'функция'
                 ^
SyntaxError: bytes can only contain ASCII literal characters.

b'type', <class 'bytes'>,

'''


'''
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
в байтовое и выполнить обратное преобразование (используя методы encode и decode).
'''
print('-----4-----\n')

word_1 = 'разработка'
word_2 = 'администрирование'
word_3 = 'protocol'
word_4 = 'standard'

print('\nstring to byte:')

word_1_to_byte = word_1.encode('utf-8')
word_2_to_byte = word_2.encode('utf-8')
word_3_to_byte = word_3.encode('utf-8')
word_4_to_byte = word_4.encode('utf-8')

print(f'\nword_1_to_byte = {word_1_to_byte},'
      f'\nword_2_to_byte = {word_2_to_byte},'
      f'\nword_3_to_byte = {word_3_to_byte},'
      f'\nword_4_to_byte = {word_4_to_byte}')

'''
Вывод из print:

word_1_to_byte = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
word_2_to_byte = b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5',
word_3_to_byte = b'protocol',
word_4_to_byte = b'standard'
'''

print('\nbyte to string:')

word_1_to_string = word_1_to_byte.decode('utf-8')
word_2_to_string = word_2_to_byte.decode('utf-8')
word_3_to_string = word_3_to_byte.decode('utf-8')
word_4_to_string = word_4_to_byte.decode('utf-8')

print(f'\nword_1_to_string = {word_1_to_string},'
      f'\nword_2_to_string = {word_2_to_string},'
      f'\nword_3_to_string = {word_3_to_string},'
      f'\nword_4_to_string = {word_4_to_string}')

'''
Вывод из print:

word_1_to_string = разработка,
word_2_to_string = администрирование,
word_3_to_string = protocol,
word_4_to_string = standard
'''

'''
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового
в строковый тип на кириллице.
'''
print('-----5-----\n')

import subprocess

args = ['ping', 'yandex.ru']
args2 = ['ping', 'youtube.com']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
subproc_ping2 = subprocess.Popen(args2, stdout=subprocess.PIPE)

for line in subproc_ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))

for line in subproc_ping2.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))

print('\n')


'''
Вывод из print:

Обмен пакетами с yandex.ru [77.88.55.77] с 32 байтами данных:

Ответ от 77.88.55.77: число байт=32 время=40мс TTL=51

Ответ от 77.88.55.77: число байт=32 время=47мс TTL=51

Ответ от 77.88.55.77: число байт=32 время=40мс TTL=51

Ответ от 77.88.55.77: число байт=32 время=48мс TTL=51



Статистика Ping для 77.88.55.77:

    Пакетов: отправлено = 4, получено = 4, потеряно = 0

    (0% потерь)

Приблизительное время приема-передачи в мс:

    Минимальное = 40мсек, Максимальное = 48 мсек, Среднее = 43 мсек



Обмен пакетами с youtube.com [173.194.122.136] с 32 байтами данных:

Ответ от 173.194.122.136: число байт=32 время=40мс TTL=112

Ответ от 173.194.122.136: число байт=32 время=48мс TTL=112

Ответ от 173.194.122.136: число байт=32 время=40мс TTL=112

Ответ от 173.194.122.136: число байт=32 время=49мс TTL=112



Статистика Ping для 173.194.122.136:

    Пакетов: отправлено = 4, получено = 4, потеряно = 0

    (0% потерь)

Приблизительное время приема-передачи в мс:

    Минимальное = 40мсек, Максимальное = 49 мсек, Среднее = 44 мсек

'''



'''
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
«сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате 
Unicode и вывести его содержимое.
'''

print('-----6-----\n')

f_n = open('test_file.txt', 'r')
print(f_n)
f_n.close()

'''
Вывод из print:

<_io.TextIOWrapper name='test_file.txt' mode='r' encoding='cp1251'>

Делаем вывод что кодировка файла - ср1251

'''

with open('test_file.txt', encoding='utf-8') as f_n:
    for line in f_n:
        print(line, end='')

'''
Вывод из print:

сетевое программирование
сокет
декоратор
'''