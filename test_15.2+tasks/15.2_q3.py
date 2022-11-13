#Напишите программу Python, которая соответствует строке с буквой a,
#за которой следует ровно две или три 'b'. 
#Если данное условие выполняется, то выведите Found a match!, иначе Not matched!

import re

text = input()
if  re.search(r'ab.b',text) != None:
    print("Found a match!")
else:
    print("Not matched!")