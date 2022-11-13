x = int(input())
y = int(input())
z = int(input())

if x == y == z: 
    print("3")
elif x == z and x != y:
    print("2")
elif x == y and z != y:
    print("2")
elif x != y != z:
    print("0")
else: 
    print("2")