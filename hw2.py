__author__ = 'Мишин Егор Олегович'

'''
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных 
из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров 
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить 
в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и
поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», 
«Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл 
main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение 
данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
'''
import csv, json, yaml, os, re


print('-----1-----')

# files = os.listdir()
# print(files)

# print(file_list)
def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for i in os.listdir():
        if 'info' in i:
            with open(i, encoding='cp1251') as f_n:
                for line in f_n:
                    if 'Изготовитель системы:' in line:
                        # print(line)
                        os_prod_list.append(''.join(re.findall(r'\w+$', line)))
                    if 'Название ОС:' in line:
                        # print(line)
                        os_name_list.append(''.join(re.findall(r'\w+ \w+ \S* \w*', line)))
                    if 'Код продукта:' in line:
                        # print(line)
                        os_code_list.append(''.join(re.findall(r'\S+-\w+', line)))
                    if 'Тип системы:' in line:
                        # print(line)
                        os_type_list.append(''.join(re.findall(r'\w+-\w* \w+', line)))
    # print(os_prod_list)
    # print(os_name_list)
    # print(os_code_list)
    # print(os_type_list)
    for i in range(0, 3):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])
        # print(main_data)



    # main_data.append(os_prod_list)
    # main_data.append(os_name_list)
    # main_data.append(os_code_list)
    # main_data.append(os_type_list)

    # print(main_data)
    return main_data


def write_to_csv(file):
    data = get_data()
    with open(str(file), 'w') as data_file:
        data_file_writer = csv.writer(data_file)
        for row in data:
            data_file_writer.writerow(row)


write_to_csv('data.csv')

with open('data.csv') as f_n:
    print(f_n.read())


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