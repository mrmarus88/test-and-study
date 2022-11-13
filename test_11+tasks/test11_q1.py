#Напишите программу, которая удаляет из строки все повторяющиеся символы.

a = input()
b=set()
s=''
for x in a:
    if  x not in b:
        b.add(x)
        s+=x
print(s)