#Напишите программу, которая сортирует натуральные числа в массиве 
#по убыванию суммы цифр десятичной записи числа.
#При равенстве сумм цифр числа должны сохранить исходный порядок.
#Использовать lambda-функции.

a = input().split()
print(*sorted(a, key = lambda x: (int(x) %10 + int(x) //10), reverse = True))


