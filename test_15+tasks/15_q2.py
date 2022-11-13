#Дано текст: This is a simple test message for test
#Задача: Подсчитать количество слов test в строке.

import re

inp = input()
print(len(re.findall(r'test', inp)))