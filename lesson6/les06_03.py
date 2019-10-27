"""
Задание 3.
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"profit": profit, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_full_profit).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""
# Описываем базовый класс Worker
class Worker:

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        # Составляем защищенный атрибус Доход (income) из переданных атрибутов ОКлад (profit) и премия (bonus)
        self._income = {"profit": float(profit), "bonus": float(bonus)}
# Описываем класс Position, унаследованный от класса Worker
class Position(Worker):
    # Объявление метода, который возвращает полное имя сотрудника (name + surname)
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    # Объявление метода, который возвращает доход сотрудника с учетом премии (profit + bonus)
    def get_full_profit(self):
        return self._income["profit"] + self._income["bonus"]
# Прогон тестов
test_employer = Position("Иван", "Иванов", "инженер", 50000, 15000)
assert test_employer.get_full_name() == "Иван Иванов"
assert test_employer.get_full_profit() == 65000.0

test_employer2 = Position("Тест", "Тестович", "подопытный", 30000.5, 25000.9)
assert test_employer2.name == "Тест"
assert test_employer2.position == "подопытный"

