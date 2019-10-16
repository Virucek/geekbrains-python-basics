"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_func(num1, num2):
    """
    Функция возвращает результат деления num1 на num2, если num2 не равен 0
    :param num1: int
    :param num2: int
    :return: int
    """
    return num1 / num2 if num2 != 0 else 'Ошибка. На 0 деление вне закона'


while True:
    try:
        num1 = int(input('Введите делимое'))
        num2 = int(input('Введите делитель'))
    except ValueError as e:
        print(f'{e}\n Одно из чисел введено неверно')
        continue
    print(f'{num1} / {num2} = {my_func(num1, num2)}')
    break
