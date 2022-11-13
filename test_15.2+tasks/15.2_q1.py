#Напишите программу на Python, которая соответствует слову, содержащему "z". 
#Если данное условие выполняется, то выведите Found a match!, иначе Not matched!

import re

inp = input()
if  re.search(r'[z]',inp) != None:
    print("Found a match!")
else:
    print("Not matched!")