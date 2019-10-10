"""
Задание 4.
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль - выручка больше издержек или убыток - издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

revenue = input("Введите значение выручки фирмы ")
costs = input("Введите значение издержек фирмы ")

# Проверка, что были введены числа
if revenue.isdigit() and costs.isdigit():
    # Перевод введенных значений в числа
    revenue, costs = int(revenue), int(costs)
    # Проверка, работает ли форма в прибыль
    if revenue > costs:
        print("Фирма работает в прибыль")
        # Расчет прибыли profit = выручка - издержки
        profit = revenue - costs
        # Расчет рентабельности по формуле (прибыль / выручка * 100%)
        print(f"Рентабельность выручки: {profit / revenue * 100}")
        staff = input("Введите число сотрудников: ")
        # Проверка, что значение количества сотрудников staff является числом и вывод дохода на каждого сотрудника
        if staff.isdigit():
            print(f"Доход на каждого сотрудника: {profit / int(staff)}")
        else:
            print("Введенное значение не число, рассчитать доход на каждого сотрудника невозможно")
    elif revenue < costs:
        print("Фирма работает в убыток")
    else:
        print("Фирма вышла на самоокупаемость, но не принесла прибыли")
else:
    print("Одно или оба введенных значения не число")