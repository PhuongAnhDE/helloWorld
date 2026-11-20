n=int(input('n='))
if n<0:
    print('Yeu cau nhap lai')
    exit()
L=[]
for i in range(n): 
    a=int(input())
    L=L+[a]
i=0
j=0
while i<len(L):
    j=j+1
    while j<len(L):
        if L[i]==L[j]:
            del(L[j])
        else:
            j=j+1
    i=i+1
for i in range(len(L)-1):
    print(L[i],end=' ')
            
        