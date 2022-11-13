n = int(input())
a = 0

for i in range(0,n):
        for x in range(0,n):
            if i == 0 or i == n-1:
                 print("1",end= ' ')
            else: 
                 print("0",end= ' ')
        print()
   