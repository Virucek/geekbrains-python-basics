"""
Задание 6.а
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

from sys import argv
from itertools import count as iter_count

script_name, num = argv
# Выводим сгенерированный числа
for el in iter_count(int(num)):
    print(f'{el}')