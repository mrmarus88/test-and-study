#Напишите функцию, вычисляющую значение a**n.

import math

def s(a, n):
    s = math.pow(a,n)
    return s 
t = input().split()
print(s(int(t[0]),int(t[1])))


#print(math.pow(int(input()),int(input())))