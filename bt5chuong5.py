x=int(input("x="))
y=int(input("y="))
k=int(input("k="))
n=int(input("n="))
L=[]
for i in range(n): 
    a=int(input(f'L[{i}]='))
    L=L+[a]
def replace(L,x,y):
    l=[]
    for i in range(len(L)):
        if L[i]==x:
            L[i]=y
            l=l+[L[i]]
            
        else:
            l=L
    return L
L=replace(L,x,y)
print(L)

