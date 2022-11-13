n = int(input())
a = 0

for i in range(0,n):
        for x in range(0,n):
            if x % 2 == 0:
                 print("0",end= ' ')
            else: 
                 print("1",end= ' ')
        print()
   