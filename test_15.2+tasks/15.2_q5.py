#Напишите программу Python, которая определит начинается ли строка  с цифры 5.

import re

inp = input()
if  re.search(r'^5',inp) != None:
    print("True")
else:
    print("False")