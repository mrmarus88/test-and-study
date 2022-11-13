#Напишите программу Python, чтобы проверить, 
#что строка содержит только набор символов a-z, A-Z и 0–9).
#Данная задача разобрана в содержании теста.

import re
#функция проверки
def is_allowed_specific_char(string):
    string = re.search(r'[^a-zA-Z0-9.]',string)                         # задание выражения
                                                               # вызов функции поиска в строке заданного выражения
    return not bool(string)

print(is_allowed_specific_char(input()))