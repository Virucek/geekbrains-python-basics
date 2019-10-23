"""
Задание 1.
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
import os
# Объявляем имя файла
file_name = "new_file_les05_01.txt"

file = open(os.path.join(os.getcwd(), file_name), "w", encoding="utf8")
while True:
    user_string = input(f"Введите данные для записи в файл {file_name}")
    # Удаляем табуляцию и пробелы и проверяем строку user_string (строку "    " тоже будем считать пустой)
    if not user_string.strip():
        break
    # Записываем данные в файл
    print(user_string, file=file)
file.close()