#В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

a = [int(s) for s in input().split()]
min = 0
max = 0
for i in range(1, len(a)):
    if a[i] > a[max]:
        max = i
    if a[i] < a[min]:
        min = i
a[min], a[max] = a[max], a[min]
print(' '.join([str(i) for i in a]))