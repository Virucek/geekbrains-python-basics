"""
Задание 3.
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
(не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
 позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
 Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
 *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
 *****\n*****\n*****.
"""


class OrgCell:

    # В каждом методе есть проверка, что other является объектом класса OrgCell, иначе возбуждается TypeError


    def __init__(self, cells: int):
        if isinstance(cells, int):
            if cells > 0:
                self.cells = cells
            else:
                raise ValueError
        else:
            raise TypeError

    def __add__(self, other):
        if isinstance(other, OrgCell):
            return OrgCell(self.cells + other.cells)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, OrgCell):
            dif = self.cells - other.cells
            if dif > 0:
                return OrgCell(dif)
            else:
                return "Cell difference must be greater than zero"
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, OrgCell):
            return OrgCell(self.cells * other.cells)
        else:
            raise TypeError

    def __truediv__(self, other):
        if isinstance(other, OrgCell):
            return OrgCell(int(self.cells / other.cells))
        else:
            raise TypeError
    # Метод форматирования ячеек. Если деление по модулю cells на columns даст 0, то "хвост" не будет дописываться
    def make_order(self, columns: int):
        return f"{'*' * columns}\n" * int(self.cells / columns) + f"{'*' * (self.cells % columns)}\n"

orgCell = OrgCell(15)
orgCell2 = OrgCell(12)

assert (orgCell + orgCell2).cells == 27
assert (orgCell - orgCell2).cells == 3
assert (orgCell * orgCell2).cells == 180
assert (orgCell / orgCell2).cells == 1

print(orgCell.make_order(5))
print(orgCell2.make_order(5))