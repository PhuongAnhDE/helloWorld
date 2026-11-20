n=int(input('n='))
if n<0:
    print('')
    exit()
L=[]
for i in range(n): 
    a=int(input())
    L=L+[a]
d=0
for i in range(len(L)):
    if L[i]>0:
        d=d+1
print(f'SND={d}')
t=0
de=0
for i in range(len(L)):
    if L[i]%2==0:
        t=t+L[i]
        de=de+1
if t==0:
    tbc=0
else:
    tbc=t/de
print(f'TBC={tbc}')
    


    
    
    
    