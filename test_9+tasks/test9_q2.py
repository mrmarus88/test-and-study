#Напишите программу, которая заполняет массив и определяет количество положительных трёхзначных чисел в этом массиве, которые не делятся на 5.

a = [int(s) for s in input().split()]
print(sum(1 for i in a if (i % 5 != 0 and len(str(i)) == 3)))
