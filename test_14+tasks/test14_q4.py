#Даны четыре действительных числа: x1, y1, x2, y2.
# Напишите функцию distance(x1, y1, x2, y2), вычисляющую
# расстояние между точкой (x1,y1)и (x2,y2). 
# Считайте четыре действительных числа и выведите результат работы этой функции.

import math
def distance(x1, y1, x2, y2):
    return(math.sqrt(((x2-x1)**2) + ((y2 -y1)**2)))

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print(distance(x1, y1, x2, y2))