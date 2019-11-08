"""
Задание 4.
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Задание 5.
Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
подходящую структуру, например словарь.

Задание 6.
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""

#TODO - рефакторинг

class ValidateError(Exception):
    def __init__(self, message):
        self.message = message

# Класс склада оргтехники
class OfficeEquipWarehouse:
    def __init__(self):
        """
        Основная структура, в которой хранятся данные по оргтехнике вида:
        {
            "Принтер":[{
                "модель":"модель",
                "тип":"лазерный",
                "количество":{
                    "склад": 15,
                    "Бухгалтерия": 10
                }
            },
            {
                "модель":"модель2",
                "тип":"струйный",
                "количество":{
                    "склад": 25,
                    "Бухгалтерия": 30
                }
            }],
            "Сканер":[{...
        """
        self.office_equip_dict = {}

    def add_to_warehouse(self, *args):
        """
        Функция по добавлению записи об оргтехнике на склад (в словарь office_equip_dict).
        Если запись с такой же моделью и типом / скоростью копирования / разрешением сканирования уже имеется в словаре,
        то добавляется только количество на складе
        :param args: OfficeEquip
        :return:
        """
        for equip in args:
            # Проверка, что переданный аргумент относится к классу OfficeEquip
            if isinstance(equip, OfficeEquip):
                # Сборка словаря из аргументов объекта
                original_vars = vars(equip)
                # Создание копии словаря original_vars, т.к. в дальнейшем придется удалять элементы из неё
                temp_copy_vars = original_vars.copy()
                # Флаг того, что запись с такими данными отсутствует в словаре
                copy_flag = False
                # Удаляем имя оргтехники (Принтер, Сканер, Ксерокс) из словаря
                name = temp_copy_vars.pop('name')
                # Удаляем количество оргтехники из словаря объекта
                number = temp_copy_vars.pop('number')
                # Проверяем, что тип оргтехники присутствует в результирующем словаре. Если нет - добавить ключ и запись по нему
                if name in self.office_equip_dict.keys():
                    #Обходим каждую запись по этому типу для проверки
                    for dict_rec in self.office_equip_dict[name]:
                        #Создаем копию словаря каждой записи
                        temp_dict = dict_rec.copy()
                        #Удаляем из временной копии словаря количество
                        temp_dict.pop('number')
                        # Сравниваем временные копии без name и number
                        if temp_copy_vars == temp_dict:
                            # Если запись с такими данными уже присутствует, количество таких объектов на складе возрастает
                            dict_rec['number']['склад'] += number
                            # Переключаем флаг
                            copy_flag = not copy_flag
                            break
                    # Если флаг показывае, что отсутствует запись, то добавляем её
                    if not copy_flag:
                        temp_copy_vars.update({"number": {"склад": number}})
                        self.office_equip_dict[name].append(temp_copy_vars)
                else:
                    temp_copy_vars.update({"number": {"склад": number}})
                    self.office_equip_dict.update({name:[temp_copy_vars]})

    def add_to_unit(self, unit, *args):
        """
        Функция отвечает за передачу техники в определенное подразделение компании со склада
        :param unit: str
        :param args: tuple (OfficeEquip, int)
        :return:
        """
        for equip in args:
            # Проверка, что переданный аргумент относится к классу OfficeEquip
            if isinstance(equip[0], OfficeEquip):
                # Сборка словаря из аргументов объекта
                equip_vars = vars(equip[0])
                # Сохраняем количество, которое необходимо передать в number
                number = equip[1]
                # Создание копии словаря equip_vars, т.к. в дальнейшем придется удалять элементы из неё
                temp_equip_vars = equip_vars.copy()
                temp_equip_vars.pop('number')
                temp_equip_vars.pop('name')
                # Проверяем, что тип оргтехники присутствует в результирующем словаре. Если нет - запись пропускается
                if equip_vars['name'] in self.office_equip_dict:
                    #Обходим каждую запись по этому типу для проверки
                    for dict_rec in self.office_equip_dict[equip_vars['name']]:
                        # Создаем копию словаря каждой записи
                        temp_dict_rec = dict_rec.copy()
                        temp_dict_rec.pop('number')
                        # Сравниваем временные копии без name и number
                        if temp_equip_vars == temp_dict_rec:
                            # Если подразделения нет в словаре данного типа в "Количество" данного типа оргтехники, то добавляем туда ключ
                            if not unit in dict_rec['number']:
                                dict_rec['number'].update({unit: 0})
                            try:
                                # Если на складе меньше количество объектов, чем указано для переноса, то возбуждаем исключение ValidateError
                                if not (dict_rec['number']['склад'] - number > 0):
                                    raise ValidateError(f"Недостаточно экземпляров {equip_vars['name']} с характеристиками {temp_equip_vars} на складе для передачи в подразделение!")
                                # Если ошибок нет, добавляем количество объектов к количеству в поздраделении, а со склада отнимаем
                                dict_rec['number'][unit] += number
                                dict_rec['number']['склад'] -= number
                            except ValidateError as e:
                                print(e)
                            break
                else:
                    continue

    def get_all_equip(self):
        """
        Вернуть результиющий словарь оргтехники
        :return: dict
        """
        return self.office_equip_dict

# Базовый класс Оргтехники
class OfficeEquip:
 #   template_construct = {
 #       'Модель': ('model', str),
 #       'Количество': ('number', int),
 #   }

    def __init__(self, number, model):
        """
        Параметры, общие для всех типов оргтехники
        :param number: int
        :param model: str
        """
        self.number = number
        self.model = model
    # Функция-декоратор для проверки ожидаемых типов
    def typecheck(types):
        def __f(f):
            def _f(*args):
                for a, t in zip(args, types):
                    if not isinstance(a, t):
                        raise ValidateError(f"Expected {t} got {a}")
                return f(*args)

            return _f

        return __f
# Класс Принтер, наследуемый от базового класса. type - тип принтера (лазерный, струйный и т.д.)
class Printer(OfficeEquip):
#    template_construct = OfficeEquip.template_construct
 #   template_construct.update({'Тип принтера': ('type', str)})

    @OfficeEquip.typecheck(types=[OfficeEquip, int, str, str])
    def __init__(self, number, model, type):
        super().__init__(number, model)
        self.name = 'Принтер'
        self.type = type

# Класс Сканер, наследуемый от базового класса. scan_res - разрешение сканирования (в dpi)
class Scanner(OfficeEquip):
#    template_construct = OfficeEquip.template_construct
#    template_construct.update({'Разрешение сканирования(dpi)':('scan_res', str)})

    @OfficeEquip.typecheck(types=[OfficeEquip, int, str, str])
    def __init__(self, number, model, scan_res):
        self.name = 'Сканер'
        super().__init__(number, model)
        self.scan_res = scan_res

# Класс Ксерокс, наследуемый от базового класса. Скорость копирования
class Xerox(OfficeEquip):
#    template_construct = OfficeEquip.template_construct
#    template_construct.update({'Скорость копирования': ('copy_speed', int)})

    @OfficeEquip.typecheck(types=[OfficeEquip, int, str, int])
    def __init__(self, number, model, copy_speed):
        self.name = 'Ксерокс'
        super().__init__(number, model)
        self.copy_speed = copy_speed
 # Проверка методов
printer = Printer(5, "HP", "lazer")
printer2 = Printer(7, "HP", "lazer")
printer3 = Printer(5, "XEROX", "струйный")
printer4 = Printer(8, "XEROX", "струйный")
printer5 = Printer(9, "HP", "lazer")
scanner = Scanner(5, "XEROX", '1440 * 1440')
xerox = Xerox(15, "CANON", 26)
xerox2 = Xerox(7, "HP", 26)
xerox3 = Xerox(25, "CANON", 17)
warehouse = OfficeEquipWarehouse()
warehouse.add_to_warehouse(printer, printer2, printer3, printer4, printer5, scanner, xerox, xerox2, xerox3)
units = [
    "Бухгалтерия",
    "Отдел внедрения",
    "RnD"
]
print(warehouse.get_all_equip())
warehouse.add_to_unit(units[0], (printer, 3), (printer3, 5), (scanner, 2), (xerox, 6), (xerox, 50))
print(warehouse.get_all_equip())
# Реализация (и проверка) контроля пользовательских вводов
warehouse2 = OfficeEquipWarehouse()
while True:
    user_choice = input(
        "Выберите тип орг.техники для добавления: \n0 - Принтер\n1 - Сканер\n2 - Ксерокс\nВведите 'stop', чтобы остановить ввод")
    if not user_choice.lower() == 'stop':
        try:
            user_choice = int(user_choice)
        except ValueError:
            print("Неверное значение данных!")
            continue
        try:
            if not user_choice:
                model, number, type = input(
                    'Введите модель (строка), количество (число), тип (строка) принтера через запятую:').split(", ")
                warehouse2.add_to_warehouse(Printer(int(number), model, type))
            elif user_choice == 1:
                model, number, scan_res = input(
                    'Введите модель (строка), количество (число), разрешение (строка) принтера через запятую:').split(", ")
                warehouse2.add_to_warehouse(Scanner(int(number), model, scan_res))
            elif user_choice == 2:
                model, number, copy_speed = input(
                    'Введите модель (строка), количество (число), скорость копирования (число) принтера через запятую:').split(", ")
                warehouse2.add_to_warehouse(Xerox(int(number), model, int(copy_speed)))
            else:
                print("Неверное значение введено! Не 0, 1, 2")
                break
        except ValueError as e:
            print('Введено неверное значение!')
        except ValidateError as e:
            print(e)
            continue
    else:
        print(warehouse2.get_all_equip())
        break
