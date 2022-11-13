s = input()
f = s[:s.find(' ')]
sw = s[s.find(' ') + 1:]
print(sw + ' ' + f)