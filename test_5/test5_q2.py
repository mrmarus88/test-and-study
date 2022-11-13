a = float(input())
b = float(input())
c = float(input())

sum = round(a + b + c,0)
pro = round(a * b * c,0)
ari = (a+b+c)/3

print(int(a) , "+" , int(b) , "+" , int(c) , "=", ("{:.0f}".format(sum)),sep="")
print(int(a) , "*" , int(b) , "*" , int(c) , "=", ("{:.0f}".format(pro)),sep="")
print("(", int(a) , "+" , int(b) , "+" , int(c) , ")/3=", ("{:.3f}".format(ari)),sep="")