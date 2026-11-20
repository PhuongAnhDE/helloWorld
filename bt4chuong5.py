x=int(input("x="))
y=int(input("y="))
k=int(input("k="))
n=int(input("n="))
L=[]
for i in range(n): 
    a=int(input(f'L[{i}]='))
    L=L+[a]
def count(L):
    b=0
    for i in L:
        b=b+1
    return b
b=count(L)
print(b)
        