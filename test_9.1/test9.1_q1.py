n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
x, y = 0, 0
cmax = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > cmax:
            cmax = a[i][j]
            x, y = i, j
print(x, y)