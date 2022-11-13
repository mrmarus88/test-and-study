#Напишите программу Python для преобразования полярных координат в прямоугольные координаты .

import cmath
cn = complex(3,4)
# получение значений полярных координат
print("Polar Coordinates: ",cmath.polar(cn))
cn1 = cmath.rect(2, cmath.pi)
print("Polar to rectangular: ",cn1)