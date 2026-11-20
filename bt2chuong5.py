x=int(input("x="))
y=int(input("y="))
k=int(input("k="))
n=int(input("n="))
L=[]
for i in range(n): 
    a=int(input(f'L[{i}]='))
    L=L+[a]
def search(L,x):
    for i in range(len(L)):
        if L[i]==x:
            return i
a=search(L,x)
if a is None :
    print("None")
else:
    print(a)
print(L)
