#Напишите класс с именем Car,  у которого определены следующие атрибуты данных:
#model (модель автомобиля, например "Тойота")
#year (год выпуска автомобиля, например "2000")
#speed (текущая скорость автомобиля, км / ч)
#У класса  Car должен быть определен метод  __init__, который по умолчанию устанавливает модель автомобиля ,  год  и скорость в качестве аргументов.
#Эти значения должны быть присвоены атрибутам объекта модель автомобиля ,  год  и скорость данных. Если скорость не указана, она должна быть по умолчанию равна 0.
#В классе также должны быть следующие методы:
#accelerate -этот метод должен добавлять 5 к атрибуту cкорости данных при каждом вызове.
#brake -этот метод должен вычитать 5 из атрибута данных скорости при каждом вызове. Скорость не должна опускаться ниже 0, поэтому, если brake()вызывается, когда скорость уже равна 0, 
#скорость должна оставаться равной 0.
#honk_horn - этот метод должен распечатать {model} goes 'beep beep', где {model}находится модель объекта.

class Car():
    def __init__(self, model, year, speed=0):
        self.model = model
        self.year = year
        self.speed = speed
    def accelerate(self):
        self.speed += 5 
        return 
    def brake(self):
        if self.speed - 5 >= 0:
            self.speed -= 5 
            return self.speed
        if self.speed == 0:
         return "0"    
    def honk_horn(self):
        print(self.model, "goes 'beep beep'")



my_car = Car("Toyota", 1975)
print(my_car.speed)
	
my_car = Car("Zastava", 2001, 30)
my_car.accelerate()
my_car.accelerate()
my_car.brake()
print(my_car.speed)

my_car = Car("Rust bucket", 1987)
my_car.honk_horn()
        
        