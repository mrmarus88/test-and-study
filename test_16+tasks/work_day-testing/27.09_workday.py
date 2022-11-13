# переменное количество аргументов
def print_args(arg0, *n_tuple):
   """
   Функция распечатает переменное количество аргументов
   """
   print("аргументы:", arg0, end=" ")
   for var in n_tuple:
       print(var, end=" ")
   print("")
print_args(10)
print_args(10, 20, 30)
print_args(10, 20, 30, 40, 50)

def f_example1(*args, **kwargs):
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
        
def f_example2(name, *, age):
    print(name)
    print(age)
# убедитесь, что f_example2("Валерия", 35) выдаст ошибку
f_example2("Валерия", age=35)

def f_example3(x, y, z):
    print('координаты: ', x, y, z)
# длина ряда должна совпадать
list3 = [1, 2, 3]
f_example3(*list3)
string3 = "456"
f_example3(*string3)
# длина ряда и ключи должны совпадать
dict3 = {'x': 7, 'y': 8, 'z': 9}
f_example3(**dict3)

numbers = (i for i in range(7))
*start, end = numbers
print(start, type(start))
print(end, type(end))

tuple_ = (1, 2, 3)
set_ = {4, 5, 6}
list_ = [*tuple_, *set_]
print(list_)
print((*list_, *tuple_))
print({*list_, *tuple_})

dict_a = {1: 1, '2': 2, '3': 3}
dict_b = {4: 4, '5': 5, '6': 6}
dict_c = {**dict_a, **dict_b}
print(dict_c)

dict_a = {'1': 1, '2': 2, '3': 3}
dict_b = {'4': 4, '2': 5, '6': 6}
dict_c = {**dict_a, **dict_b}
print(dict_c)

arr = [1, 2, 3, 4, 5]

def create_arr(n):
    arr = list(range(1, n+1))
    print(arr)

def display_arr():
    global arr
    print(arr)

def transform_arr(n):
    global arr
    if n > len(arr):
        arr = list(range(1, n+1))
    print(arr)

def display_transform_arr(m, n):
    arr = list(range(1, n+1))
    def transform_arr():
        nonlocal arr, m, n
        if m > n:
            arr = list(range(n, m+1))
        return arr
    arr = transform_arr()
    
# для создания группы функций
def power_n(n):
    return lambda x: x ** n
power2, power3, power4 = (power_n(i) for i in (2,3,4))
power2(7), power3(5), power4(2)



from functools import reduce
lst = list(range(1,11))
lst_sum = reduce(lambda x, y: x + y, lst)
print(lst_sum)
lst_prod = reduce(lambda x, y: x * y, lst)
print(lst_prod)

import random
r_list = [random.randint(1,99) for i in range(5)]
r_tuple = tuple(random.randint(1,99) for i in range(5))
print(r_list, r_tuple)

# формирует новый список из итерируемого объекта
print(sorted(r_list), sorted(r_tuple))

print(sorted(r_list, reverse=True), sorted(r_tuple, reverse=True))

# с функцией ключа сортировки
string = "Have you already set your goals for the New Year"
print(sorted(string.split(), key=len))

# по умолчанию - сортировка по первой буквы на основе Unicode
print([(ord(s[0]), s[0]) for s in sorted('New Year')])

# игнорирование различий между маленькими и большими буквами
print(sorted(string.split(), key=str.lower))

# по умолчанию - по длине, если символы одинаковые
print(sorted(['hhhhh', 'hh', 'h', 'hhhh', 'hhhhhh', 'hhh']))

# по умолчанию - по первому различию, если начало одинаковое
print(sorted(['hhhd', 'hhhf', 'hhha', 'hhhe', 'hhhb', 'hhhc']))

# сортирует по возрасту
pet_tuples = [
('Mimi', 'cat', 5),('Lu', 'dog', 10),('Bash', 'dog', 7)]
print(sorted(pet_tuples, key=lambda pet: pet[2]))

# применима только к объектам одного вида
similar_values = [False, 0, 1, 1 <= 0, True, '0' == '1']
print(sorted(similar_values))

# возвращает список ключей словаря
dict1 = {1: '1', 3: '15', 2: '4'}
print(sorted(dict1))