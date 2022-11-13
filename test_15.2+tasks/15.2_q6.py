#Напишите программу Python для поиска цифр (0-9) длиной от 1 до 3 в заданной строке.

import re

inp = input()
result = re.finditer(r'([0-9]{1,3})',inp)
print("Number of length 1 to 3")
for i in result:
    print(i.group(0))
