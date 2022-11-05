import math 

a=float(input()) 
b=float(input()) 
c=float(input()) 

if math.sqrt(a**2+b**2)==c:
    print("Yes")
elif math.sqrt(c**2+b**2)==a:
    print("Yes")
elif math.sqrt(a**2+c**2)==b:
    print("Yes")
else:
    print("No")