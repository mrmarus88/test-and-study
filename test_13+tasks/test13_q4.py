#Реализовать программу  для преобразования числа с плавающей запятой в неправильную дробь.

from fractions import Fraction
value = 4.2
print(Fraction(value).limit_denominator())