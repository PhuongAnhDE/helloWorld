n=int(input('n='))
if n<=0:
    print('')
    exit()
L=[]
for i in range(n): 
    a=int(input())
    L=L+[a]
l=[]
l=L
l.reverse()
for i in range(len(l)):
    print(l,end=' ')
print()
l.sort()
for i in range(len(l)):
    print(l,end=' ')