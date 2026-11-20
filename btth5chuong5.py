import sys
n=int(input('n='))
    if n<0:
        print('Yeu cau nhap lai')
    sys.exit()
L=[]
for i in range(n): 
    a=int(input())
    L=L+[a]
t=0
for i in range(n):
    if i%2!=0:
        t=t+L[i]
print(f'Tong={t}')
        