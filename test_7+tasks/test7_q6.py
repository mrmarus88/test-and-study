#Входные данные
#Вводятся натуральные числа a и b. Гарантируется, что a не превосходит b.
#Выходные данные
#Выведите все числа на отрезке от a до b, являющиеся полными квадратами. Если таких чисел нет, то ничего выводить не нужно.

a = int(input())
b = int(input())
r = ""
for x in range(b+1):
    if a <= x*x <= b:
        r += str(x*x) + " "
print(x*x)


#a = int(input())
#b = int(input())

#print(i**2 for i in range(int(a + a ** 1/2), int(b ** 1/2 +1)))


       #if(sqrt(i * 1.0) == int(sqrt(i)))
            #cout << i << " ";
# 2 - 8
# 2 ** 0.5 != а