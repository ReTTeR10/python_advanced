__author__ = 'Мишин Егор Олегович'

import time
#import json
#from pytest import raises
#import socket
import unittest
from client import create_presence, translate_message
from errors import UsernameTooLongError, ResponseCodeLenError, MandatoryKeyError, ResponseCodeError

# тестируем функцию формирования сообщения от клиента
class TestClientCreatePresence(unittest.TestCase):
    # action формируется корректно
    def test_create_presence_non(self):
        self.assertEqual(create_presence()['action'], "presence")
    # проверяем, что имя клиента записывается корректно, если мы его передаем
    def test_create_presence_param(self):
        self.assertEqual(create_presence('test_user_name')["user"]["account_name"], 'test_user_name')
    # берем разницу во времени
    def test_create_presence_time(self):
        self.assert_(abs(create_presence()['time'] - time.time()) < 0.1)
    # неверный тип аккаунта - число
    def test_create_presence_acc_int(self):
        with self.assertRaises(TypeError):
            create_presence(200)
    # неверный тип аккаунта - None
    def test_create_presence_acc_none(self):
        with self.assertRaises(TypeError):
            create_presence(None)
    # слишком длинное
    def test_create_presence_acc_toolong(self):
        with self.assertRaises(UsernameTooLongError):
            create_presence('11111111111111111111111111')

# тестируем функцию разбора ответа сервера
class TestClientTranslateMessage(unittest.TestCase):
    # неправильный тип
    def test_translate_message_inc_type(self):
        with self.assertRaises(TypeError):
            translate_message(100)
    # нету ключа response
    def test_translate_message_not_resp(self):
        with self.assertRaises(MandatoryKeyError):
            translate_message({'one': 'two'})
    # неверная длина кода ответа
    def test_translate_message_incor_resp_len(self):
        with self.assertRaises(ResponseCodeLenError):
            translate_message({'response': '5'})
    # неверный код ответа
    def test_translate_message_incor_resp(self):
        with self.assertRaises(ResponseCodeError):
            translate_message({'response': 700})
    # все правильно
    def test_translate_message_cor_resp(self):
        self.assertEqual(translate_message({'response': 200}), {'response': 200})

if __name__ == "__main__":
    unittest.main()







"""
# МОДУЛЬНЫЕ ТЕСТЫ
def test_create_presence():
    # без параметров
    message = create_presence()
    assert message['action'] == "presence"
    # берем разницу во времени
    assert abs(message['time'] - time.time()) < 0.1
    assert message["user"]["account_name"] == 'Guest'
    # с именем
    message = create_presence('test_user_name')
    assert message["user"]["account_name"] == 'test_user_name'
    # неверный тип
    with raises(TypeError):
        create_presence(200)
    with raises(TypeError):
        create_presence(None)
    # Имя пользователя слишком длинное
    with raises(UsernameToLongError):
        create_presence('11111111111111111111111111')


def test_translate_message():
    # неправильный тип
    with raises(TypeError):
        translate_message(100)
    # нету ключа response
    with raises(MandatoryKeyError):
        translate_message({'one': 'two'})
    # неверная длина кода ответа
    with raises(ResponseCodeLenError):
        translate_message({'response': '5'})
    # неверный код ответа
    with raises(ResponseCodeError):
        translate_message({'response': 700})
    # все правильно
    assert translate_message({'response': 200}) == {'response': 200}

"""



