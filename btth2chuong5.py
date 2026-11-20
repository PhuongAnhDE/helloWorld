n=int(input('n='))
def Input():
    if n>0:
        return n
    else:
        print('Yeu cau nhap lai')
        exit()
n=Input()
L=[]
for i in range(n): 
    a=int(input())
    L=L+[a]
def Search(L):
    max=L[0]
    min=L[0]
    for i in range(len(L)):
        if L[i]>max:
            max=L[i]
        if L[i]<min:
            min=L[i]
    return max,min
max,min=Search(L)
def Output(max,min):
    print(max,min)
Output(max,min)