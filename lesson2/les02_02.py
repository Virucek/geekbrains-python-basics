"""
Задание 2.
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

# Ввод списка элементов

user_list = input("Введите список элементов через пробел")

# Преобразование введенных элементов в список
user_list = user_list.split()

# Если количество элементов четное, то четные и нечетные элементы просто меняются местами
if len(user_list) % 2 == 0:
    # Вводим переменную для хранения списка четных элементов (временный список - temp_list)
    temp_list = user_list[::2]
    # Четным элементам изначального списка присваиваем значения нечетных
    user_list[::2] = user_list[1::2]
    # Нечетным элементам изначального списка присваиваем значения четных (из temp_list)
    user_list[1::2] = temp_list
else:
    """
    Если количество элементов нечетное, то последний элемент в списке обрезается и записывается в переменную,
    четные и нечетные элементы меняются местами, а последний элемент отдельно добавляется в список
    """
    a = user_list.pop(-1)
    temp_list = user_list[::2]
    user_list[::2] = user_list[1::2]
    user_list[1::2] = temp_list
    user_list.append(a)
print(user_list)