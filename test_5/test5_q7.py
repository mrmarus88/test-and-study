a = int(input())
b = int(input())
c = int(input())
d = int(input())

x = d - b

if x < 0 : x = d + 100 - b 
else: x = d - b 

r = c - a

print("Ваша сдача составляет ", r,"руб. " , x , "коп.")