#Напишите программу, которая сортирует элементы массива по возрастанию последней цифры десятичной записи чисел.
#Используя lambda- функции.


a = input().split()
print(*sorted(a, key = lambda n: n[-1]))

