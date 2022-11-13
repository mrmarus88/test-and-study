n = int(input())
a = 0

for i in range(0,n):
        for x in range(0,n):
            if x < n * 0.5 and i < n * 0.5:
                print("1",end= ' ')
            else: 
                print("0",end= ' ')
        print()