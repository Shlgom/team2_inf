from random import randint
from math import log, ceil


def is_valid():
    while True:
        num = input('Введите целое число'
                    ' от 0 до 100 включительно: ')

        if num.isdigit() and (float(num) % int(num) == 0.0) and \
                (-1 < int(num) < 101):
            return int(num)