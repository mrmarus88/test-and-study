#Используя генератор списков. 
#Напишите программу, которая заполняет массив первыми N натуральными числами в обратном порядке (начиная с последнего) и выводит его.

n = int(input())
print(*reversed([i for i in range(1, n+1)]), end = " ")