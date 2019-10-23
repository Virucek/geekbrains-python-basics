"""
Задание 2.
Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
"""
import os

with open(os.path.join(os.getcwd(), "file_les05_02.txt"), "r", encoding="utf8") as file:
    # Объявляю счетчик количества строк
    line_num = 0
    for line in file:
        # Подсчет слов переводом строки в список и подсчитывая его длину
        words_num = len(line.split())
        line_num += 1
        print(f"В строке {line_num} количество слов: {words_num}")
    print(f"В файле {line_num} строк")
