"""
Задание 6.b
Реализовать два небольших скрипта:
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

from itertools import cycle as iter_cycle
# Некоторый список
my_list = [1, 2, 3, 4, 1, 5, 10, 6]
# Бесконечно выводим элементы списка my_list
for el in iter_cycle(my_list):
    print(f'{el}')
