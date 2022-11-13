#Напишите программу Python, которая соответствует строке,
# в которой есть a, за которым следуют три 'b'. 
# Если данное условие выполняется, то выведите Found a match!, иначе Not matched!

import re

inp = input()
if re.search(r'^[a]+[b]{3,3}', inp):
    print('Found a match!')
else:
    print('Not matched!')