#Входные данные
#Вводится число N, а затем N чисел.
#Выходные данные
#Подсчитайте и выведите, сколько среди данных N чисел нулей.

num_zeroes = 0
for i in range(int(input())):
    if int(input()) == 0:
        num_zeroes += 1
print(num_zeroes)