__author__ = 'Мишин Егор Олегович'
import json, yaml
'''
2. Задание на закрепление знаний по модулю json. 
Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение 
данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — 
товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date). 
Функция должна предусматривать запись данных в виде словаря в файл orders.json. 
При записи данных указать величину отступа в 4 пробельных символа;

Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
'''
print('\n-----2-----')


def write_order_to_json(item, quantity, price, buyer, date):  # описываем функцию

    with open('orders.json', 'r') as json_file_read:          # загружаем текущую информацию из файла
        json_data = json.load(json_file_read)

    with open('orders.json', 'w') as json_file:               # далее добавляем к старой информации новую
        json_file_target = json_data[0]['orders']
        orders_info = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
        json_file_target.append(orders_info)
        json.dump(json_data, json_file, indent=4)


# Тут можно было сделать простой счетчик чтобы можно было добавлять несколько товаров...
item = input('Наименование товара: ')
quantity = input('Количество товара: ')
price = input('Стоимость товара: ')
buyer = input('Покупатель товара: ')
date = input('Дата: ')

write_order_to_json(item, quantity, price, buyer, date)

with open('orders.json') as f_n:
    print(f_n.read())                  # Выводим новое содержимое







'''
3. Задание на закрепление знаний по модулю yaml. 
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, 
второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, 
отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. 
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить возможность 
работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
'''

print('\n-----3-----')

dict_to_yaml = {
    "key1": ['hello', 'I', 'am', 'test', 'list'],
    "key2": 255,
    "key3": {
        "symbol_1": "€",
        "symbol_2": "©",
        "symbol_3": "༖",

    }
}

with open('test.yaml', 'w') as f_n:
    yaml.dump(dict_to_yaml, f_n, default_flow_style=False)

with open('test.yaml') as f_n:
    print(f_n.read())