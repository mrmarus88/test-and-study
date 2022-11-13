#Напишите программу Python, чтобы найти последовательности одной буквы верхнего регистра,
# за которой следуют буквы нижнего регистра. 
# Если данное условие выполняется, то выведите Found a match!, иначе Not matched!

import re

inp = input()
if re.search(r'^[A-Z]+[a-z]', inp):
    print('Found a match!')
else:
    print('Not matched!')