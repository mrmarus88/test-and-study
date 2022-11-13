n = int(input())
a = []
for i in range(n):
  r = input().split()
  for j in range(n): 
      r[j] = int(r[j])
  a.append(r)
m = 0
for i in range(1, n):
  k = 0
  for j in range(i):
    if (a[i][j] == a[j][i]):
        k = k+1
  if k == i: m = m+1
if (m == n-1): print('yes')
else: print('no')