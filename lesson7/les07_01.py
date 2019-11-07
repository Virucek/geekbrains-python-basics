"""
Задание 1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""

class Matrix:

    def __init__(self, *lines):
        self.matrix = lines

    def __str__(self):
        matrix = ''
        for line in self.matrix:
            matrix += ' '.join(map(str, line)) + '\n'
        return matrix

    def __add__(self, other):
        # Объявляем новый результирующий список списков
        new_matrix = []
        # Перебираем списки (строки) из 1 и 2 матриц
        for i, j in zip(self.matrix, other.matrix):
            # Объявляем пустую строку новой матриц
            new_line = []
            # Перебираем каждый элемент из строк 1 и 2 матрицы
            for el_self, el_other in zip(i, j):
                # В строку для новой матрицы добавляем сумму элементов
                new_line.append(el_self + el_other)
            #В новую матрицу добавляем строку с полученными результатами
            new_matrix.append(new_line)
        #Возвращаем объект класса Matrix с полученными параметрами
        return Matrix(*(line for line in new_matrix))

matrix = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(matrix)
matrix2 = Matrix([1, 2, 3], [3, 4, 7], [1, 3, 8])
print(matrix + matrix2)