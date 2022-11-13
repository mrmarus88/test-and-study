#Напишите программу на Python для вычисления площади правильного многоугольника. Обратите внимание на подключение математического пакета Math. 

from math import tan, pi
n_sides = int(input())
s_length = float(input())
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print("The area of the polygon is: ",p_area)