#Напишите программу, которая находит все различные цифры в символьной строке.

a = set()
st=input()
for x in st:
      if '0'<=x<='9' and x not in a: a.add(x)
if len(a)>0:
      b=sorted(list(a))
      print(*b,sep='')
else :   print('NO')