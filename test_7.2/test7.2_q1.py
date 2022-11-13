n = int(input())
c = 0
while (n > 0):
    num = n % 10
    if (num <= 6):
        c += 1
    n = n // 10
print(c)
    

