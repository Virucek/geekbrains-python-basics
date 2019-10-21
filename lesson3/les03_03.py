"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(var1, var2, var3):
    """
    Сумма двух максимальных аргументов (сравниваются парами и максимальныеы из пар суммируются)
    :param var1: int
    :param var2: int
    :param var3: int
    :return: int
    """
    return max(var1, var2) + max(var1, var3)


while True:
    try:
        var1 = int(input('Введите первое число'))
        var2 = int(input('Введите второе число'))
        var3 = int(input('Введите третье число'))
    except ValueError as e:
        print(f'{e}\nОдно из введенных значений не является числом. Попробуйте ещё раз')
        continue
    print(f'{my_func(var1, var2, var3)}')
    break
