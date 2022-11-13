#Реализовать программу Python для сложения, вычитания, умножения и деления двух дробей.

import fractions
f1 = fractions.Fraction(2, 3)
f2 = fractions.Fraction(3, 7)
print('{} + {} = {}'.format(f1, f2, f1 + f2))
print('{} - {} = {}'.format(f1, f2, f1 - f2))
print('{} * {} = {}'.format(f1, f2, f1 * f2))
print('{} / {} = {}'.format(f1, f2, f1 / f2))