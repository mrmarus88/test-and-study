#Напишите программу, которая выводит все цифры, встречающиеся в символьной строке больше одного раза.

a = input()
l = list ("0123456789")
c = ""
for x in l:
    if a.count(str(x))>1:
     c += str(x)
     if len(c)>0:
      print(*c)
     else: print("NO")