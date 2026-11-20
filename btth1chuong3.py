import math
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
dt=float
p=float
p=(a+b+c)/2
dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
if (a+b)>c and (a+c)>b and (b+c)>a :
    print(f'Dien tich={round(dt,3)}')
else:
    print('Khong hop le')
    


