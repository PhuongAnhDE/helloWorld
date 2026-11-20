n=int(input('n='))
def Input():
    if n>0:
        return n
    else:
        print('')
        exit()
n=Input()
L=[]
for i in range(n): 
    a=int(input())
    L=L+[a]
x=int(input('x='))
def FirstAndLast(L):
    l=[]
    for i in range(n+1):
        if L[0] :
            l=l+[L[0]]
            if l[-1]:
                l=l+[L[-1]]
        return l
def Search(L,x):
    a=''
    if x in L :
        a="True"
    else:
        a="False"
    return a
l=FirstAndLast(L)
a=Search(L,x)
print(l)
print(a)
    