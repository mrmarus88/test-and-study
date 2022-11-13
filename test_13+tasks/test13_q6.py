#Изучите работу модуля decimal. Напишите  программу Python, 
# чтобы получить квадратный корень и экспоненту данного десятичного числа. 

from decimal import *
x = Decimal('1.44')
print("Square root of ",x, " is :", x.sqrt())
print("exponential of ",x, " is :", x.exp())

