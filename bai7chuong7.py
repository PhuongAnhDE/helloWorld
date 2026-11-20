n=int(input())
S=[]
M=[]
D={}
i=0
for i in range(n):
    x=input()
    S.append(x)
for i in range(n):
    y=int(input())
    M.append(y)
for i in range(n):
    D[S[i]]=M[i]
tdk={}
for M in D:
    if D[M]<150:
        tdk[M]=D[M]
print(tdk)