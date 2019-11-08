"""
Задание 1.
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
# Класс Дата
class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def date_to_int(cls, date):
        """
        Функция принимает дату, возвращает отдельно число, месяц, год
        :param date: str
        :return: int, int, int
        """
        try:
            # Преобразовываем дату в список, каждый элемент списка преобразовываем в число
            new_date = date.split('-')
            day = int(new_date[0])
            month = int(new_date[1])
            year = int(new_date[2])
            return day, month, year
        except ValueError as e:
            return e

    @staticmethod
    def date_validate(date: str):
        """
        Функция валидирует дату, месяц, год
        :param date: str
        :return: str
        """
        day, month, year = Date.date_to_int(date)
        if day >= 1 and day <= 30 and month >= 1 and month <= 12 and year > 1000 and year < 9999:
            return f'Date is correct'
        else:
            return f'Date is INcorrect'
# Проверка методов
test_date = Date('10-05-2017')
day, month, year = Date.date_to_int(test_date.date)
assert day == 10
assert month == 5
assert year == 2017
assert test_date.date_validate(day, month, year) == "Date is correct"

test_date2 = Date('30-15-2016')
day2, month2, year2 = Date.date_to_int(test_date2.date)
assert day2 == 30
assert month2 == 15
assert year2 == 2016
assert test_date.date_validate(day2, month2, year2) == "Date is INcorrect"