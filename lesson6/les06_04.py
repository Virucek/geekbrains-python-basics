"""
Задание 4.
Опишите несколько классов: TownCar, SportCar, WorkCar, PoliceCar.
У каждого класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также несколько методов: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
"""
# Создаем базовый класс Car, имеющий атрибуты speed, color, name и методы go, stop, turn(direction)
class Car:
    def __init__(self, speed: int, color: str, name: str):
        self.speed = int(speed)
        self.color = color
        self.name = name
    # Метод, сообщающий, что машина поехала
    def go(self):
        print("Машина поехала")
    # Метод, сообщающий, что машина остановилась
    def stop(self):
        print("Машина остановилась")
    # Метод, сообщающий, куда машина повернула
    def turn(self, direction):
        print(f"Машина повернула в сторону {direction}")
# Описание класса TownCar - наследника Car, определяем у него атрибут is_police со значением False
class TownCar(Car):
    is_police = False
# Описание класса SportCar - наследника Car, определяем у него атрибут is_police со значением False
class SportCar(Car):
    is_police = False
# Описание класса WorkCar - наследника Car, определяем у него атрибут is_police со значением False
class WorkCar(Car):
    is_police = False
# Описание класса PoliceCar - наследника Car, определяем у него атрибут is_police со значением True
class PoliceCar(Car):
    is_police = True
# Прогон тестов
test_town_car = TownCar(100, "Красный", "Шевроле")
test_sport_car = SportCar(370, "Синий", "Ауди")
test_work_car = WorkCar(100, "Белый", "Камаз")
test_police_car = PoliceCar(200, "Сине-белый", "Ауди")

test_town_car.go()
test_sport_car.stop()
test_work_car.turn("Север")
assert test_police_car.is_police == True
assert test_town_car.is_police == False
assert test_work_car.speed == 100
assert test_sport_car.name == "Ауди"