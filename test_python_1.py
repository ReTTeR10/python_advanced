__author__ = 'Мишин Егор Олегович'

'''
2. * Написать тесты для домашних работ из курса «Python 1».
'''

from python_1 import new_list
import unittest


class test_python_1(unittest.TestCase):
    def test_new_list(self):
        self.assertEqual(new_list(), [1, 4, 16, 0])