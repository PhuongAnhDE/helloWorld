import math
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if (a+b>c) and (a+c>b) and (b+c>a) and (a>0) and (b>0) and (c>0) :
    s=float
    s=(a+b+c)/2
    dt=float
    dt=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"Dien tich={dt}")
else:
    print('')
