"""
Задание 3.
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

# РЕШЕНИЕ ЧЕРЕЗ LIST
while True:
    # Ввод месяца
    user_num = input("Введите число от 1 до 12")
    # Объявление списков времен года
    winter = [1, 2, 12]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]
    # Проверка, что введенное значение является числом
    if user_num.isdigit():
        user_num = int(user_num)
        if user_num in winter:
            print("Это Зима!")
        elif user_num in spring:
            print("Это Весна!")
        elif user_num in summer:
            print("Это Лето!")
        elif user_num in autumn:
            print("Это Осень!")
        else:
            print("Вы не ввели число от 1 до 12!")
            continue
        break
    else:
        print("Вы не ввели число от 1 до 12!")

# РЕШЕНИЕ ЧЕРЕЗ DICT
while True:
    # Ввод месяца
    user_num = input("Введите число от 1 до 12")
    # Объявление словаря, содержащего времена года и относящихся к ним месяцев
    seasons = {'winter':[1, 2, 12], 'spring':[3, 4, 5], 'summer':[6, 7, 8], 'autumn':[9, 10, 11]}
    # Проверка, что введенное значение является числом
    if user_num.isdigit():
        user_num = int(user_num)
        if user_num in seasons['winter']:
            print("Это Зима!")
        elif user_num in seasons['spring']:
            print("Это Весна!")
        elif user_num in seasons['summer']:
            print("Это Лето!")
        elif user_num in seasons['autumn']:
            print("Это Осень!")
        else:
            print("Вы не ввели число от 1 до 12!")
            continue
        break
    else:
        print("Вы не ввели число от 1 до 12!")