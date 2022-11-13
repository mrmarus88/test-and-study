#Напишите класс Python с именем Rectangle, состоящий из длины и ширины, и метода,
#который будет вычислять площадь прямоугольника.

class Rectangle():
    def __init__(self, l, w):
         self.length = l
         self.width = w

    def rectangle_area(self):
        return self.length*self.width

a=int(input()) # введите а
b=int(input()) # Тут должен быть ваш код, вам нужно ввести b
newRectangle = Rectangle(a, b)
print(newRectangle.rectangle_area())