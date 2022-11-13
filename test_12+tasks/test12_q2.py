#Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
#Для слова из словаря, записанного в последней строке, определите его синоним.

n = int(input())
d = {}
for i in range(n):
    f, s = input().split()
    d[f] = s
    d[s] = f
print(d[input()])