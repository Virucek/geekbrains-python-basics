"""
Задание 2.
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""

class Road:
    # Определяем конструктор, принимающий и определяющий атрибуты длина (length) и ширина (width)
    def __init__(self, length, width):
        self._length = length
        self._width = width
    # Определяем метод расчета массы асфальта (масса асфальта на 1 кв.м. и число см. толщины полотна - константы)
    def calc_weight(self):
        return self._length * self._width * 25 * 5 / 1000

a = Road(20, 5000)
weight = a.calc_weight()
print(f"{a._length} м * {a._width} м * 25 кг * 5 см = {weight} т")

assert a.calc_weight() == 12500
