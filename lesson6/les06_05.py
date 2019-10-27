"""
Задание 5.
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
# Описание базового класса Stationery
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Эта канцелярская принадлежность - {self.title}")
# Описание класса Pen, наследованного от Stationery
class Pen(Stationery):
    def draw(self):
        print(f"Эта ручка - {self.title}")
# Описание класса Pencil, наследованного от Stationery
class Pencil(Stationery):
    def draw(self):
        print(f"Этот карандаш -  {self.title}")
# Описание класса Handle, наследованного от Stationery
class Handle(Stationery):
    def draw(self):
        print(f"Этот маркер - {self.title}")

test_1 = Stationery("Ножницы")
test_1.draw()

test_2 = Pen("Перьевая")
test_2.draw()

test_3 = Pencil("мягкий")
test_3.draw()

test_4 = Handle("Черный")
test_4.draw()