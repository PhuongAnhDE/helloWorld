L=[]
for i in range(10):
    a=int(input())
    L=L+[a]
l=[]
l=L.copy()
A=[]
for i in range (0,10,2):
    l[i]=L[i+1]
    A=A+[l[i]]
    l[i+1]=L[i]
    A=A+[l[i+1]]
for i in range(10):
    print(A[i],end=' ')
    
    