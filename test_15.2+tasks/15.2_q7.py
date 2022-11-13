#Напишите программу Python для поиска последовательностей строчных букв, 
#соединенных знаком подчеркивания. Если данное условие выполняется, 
#то выведите Found a match!, иначе Not matched!

import re

inp = input()
if re.search(r'^[a-z]+_[a-z]+$', inp):
    print('Found a match!')
else:
    print('Not matched!')

