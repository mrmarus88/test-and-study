#Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.

a = input()
b = input()

i = a <= b
print(*[i for i in range(int(a),int(b)+1)])