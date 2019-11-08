"""
Задание 7.
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
# Класс "Комплексное число". Передаются параметры: действительная часть числа и мнимая
class ComplexNumber:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __str__(self):
        return f'{self.real} + {self.image} * i'

    def __add__(self, other):
        return f'{(self.real + other.real)} + {(self.image + other.image)}*i'

    def __mul__(self, other):
        return f'{(self.real * other.real - self.image * other.image)} + {(self.image * other.real + self.real * other.image)}*i'
# Проверка работы методов
complex = ComplexNumber(2, 3)
complex2 = ComplexNumber(4, 5)

assert complex + complex2 == '6 + 8*i'
assert complex * complex2 == '-7 + 22*i'