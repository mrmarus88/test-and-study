#По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.

r = 1
n = int(input())
for i in range(1, n + 1):
    r *= i
print(r)