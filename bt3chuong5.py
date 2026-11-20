x=int(input("x="))
y=int(input("y="))
k=int(input("k="))
n=int(input("n="))
L=[]
for i in range(n): 
    a=int(input(f'L[{i}]='))
    L=L+[a]
def delete(L,x) :
    i=0
    while i<len(L):
        if L[i]==x:
            del(L[i])
        else:
            i=i+1
    return L
L=delete(L,x)
print(L)
    