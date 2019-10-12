"""
Задание 3.
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

num = input("Введите целое положительное число: ")
i = 0
# Проверка, введено ли именно число
if num.isdigit():
    # Перевод введенной строки в число
    num = int(num)
    # Объявление переменной для хранения максимального числа
    max = 0
    """
    Т.к. по заданию требуется использовать именно арифметические операции, то:
    остаток от деления числа на 10 записывается в переменную и сравнивается с максимальным значением.
    Само число делится без остатка на 10, тем самым уменьшается его разрядность, пока деление на 10 не даст 0 (значит, число на 10 больше делиться не может)
    """
    while num // 10 > 0:
        n = num % 10
        if n > max:
            max = n
        num = num // 10
    # Т.к. от num осталась одна цифра, её проверить необходимо отдельно
    if num > max:
        max = num
    print(f"Самая большая цифра в числе: {max}")
else:
    print("Введите число в следующий раз")