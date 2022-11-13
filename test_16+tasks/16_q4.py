#Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar 
#У каждого класса должны быть следующие аттрибуты: speed, color, name, is_police - Булево значение. 
#А так же несколько методов: go, stop, turn(direction) - которые должны сообщать, о том что машина поехала, остановилась, повернула(куда)
#Подумайте как выделить общие признаки классов в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name, is_polise):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_polise = bool(is_polise)
    def go(self):
        print('машина модель {} поехала'.format(self.name))
    def stop(self):
        print('машина модель {} остановилась'.format(self.name))
    def turn(self, direction):
        print('машина модель {} повернула {}'.format(self.name, direction))

class TownCar(Car):
    pass
class SportCar(Car):
    pass
class WorkCar(Car):
    pass
class PoliceCar(Car):
    pass

