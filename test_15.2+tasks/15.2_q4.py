#Напишите программу Python, которая соответствует строке,
#за которой следует a, за которым следует один или несколько b.
#Если данное условие выполняется, то выведите Found a match!, иначе Not matched!


import re

text = input()
if  re.search(r'ab+?',text) != None:
    print("Found a match!")
else:
    print("Not matched!")