#Дано текст например: This is a simple test message for test
#Задача: 
# 1)Определить, заканчивается ли строка на слово test, 
# 2)начинается ли на test. 
# 3)Определить является ли строка просто строкой test.

import re

inp = input()
print(re.search(r'test^',inp) != None)
print(re.search(r'test$',inp) != None)               
print(re.search(r'test',inp) != None)          
print(re.search(r'^test$',inp) != None)

