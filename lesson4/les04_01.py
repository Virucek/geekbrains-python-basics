"""
Задание 1.
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

def calc_salary(work_hours: int, cost_hour: float, premium: float):
    return (work_hours * cost_hour) + premium

try:
    script_name, work_hours, cost_hour, premium = argv
    print(f'Заработная плата сотрудника: {calc_salary(int(work_hours), float(cost_hour), float(premium))} руб.')
except ValueError as e:
    print(f'При запуске скрипта передайте параметры правильно (числами): выработка в часах, ставка в час, премия')
