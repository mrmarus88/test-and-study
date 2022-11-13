s=input()
s1=""
i=0
for c in s:
    if c == 'a':
        c = 'b'
        i += 1
    if c == 'A':
        c = 'B'
        i += 1
    s1 += c
print(s1)
print(i)