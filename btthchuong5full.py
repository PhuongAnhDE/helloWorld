# cau1
# L=[]
# def Input():
#     n=int(input('n='))
#     if n<=0:
#         print()
#         exit()
#     for i in range(n):
#         a=int(input())
#         L.append(a)
#     x=int(input('x='))
#     return L,x
# def firstandlast(L):
#     l=[]
#     for i in range(len(L)):
#         if i==0:
#             l=l+[L[0]]
#         elif i==len(L)-1:
#             l=l+[L[-1]]
#     return l
# def search(L,x):
#     if x in L:
#         print("True")
#     else:
#         print('Flase')
# L,x=Input()
# l=firstandlast(L)
# print(l)
# search(L,x)
# cau2
# L=[]
# def Input():
#     n=int(input('n='))
#     if n<=0:
#         print()
#         exit()
#     for i in range(n):
#         a=int(input())
#         L.append(a)
#     return L
# def search(L):
#     max=L[0]
#     min=L[0]
#     for i in range(len(L)):
#         if L[i]>max:
#             max=L[i]
#         elif L[i]<min:
#             min=L[i]
#     return min,max
# def output(max,min):
#     print(max,min)
# L=Input()
# min,max=search(L)
# output(max,min)
# L=[]
# def Input():
#     n=int(input('n='))
#     if n<=0:
#         print()
#         exit()
#     for i in range(n):
#         a=int(input())
#         L.append(a)
#     return L
# def maxmin(L):
#     print(max(L),min(L))
# L=Input()
# maxmin(L)
# cau3
# L=[]
# d=0
# b=0
# tbc=0
# n=int(input('n='))
# if n<=0:
#     print()
#     exit()
# for i in range(n):
#     a=int(input())
#     L.append(a)
# for i in range(n):
#     if L[i]>0:
#         d=d+1
#     if L[i]%2==0 :
#         tbc=tbc+L[i]
#         b=b+1
# print(f'SND={d}')
# if tbc>0 and b>0:
#     print(f'TBC={tbc/b}')
# else:
#     print(f'TBC=0')
# cau4
# A=[]
# B=[]
# n=int(input('n='))
# if n<=0:
#     print()
#     exit()
# for i in range(n):
#     a=int(input())
#     A.append(a)
# A.reverse()
# B=A.copy()
# B.sort()
# print(A)
# print(B)
# cau5
# A=[]
# t=0
# n=int(input('n='))
# if n<=0:
#     print()
#     exit()
# for i in range(n):
#     a=int(input())
#     A.append(a)
# for i in range(n-1):
#     if i%2!=0:
#       t=t+A[i]  
# print(f'Tong={t}')
# cau6
# A=[]
# B=[]
# for i in range(10):
#     a=int(input())
#     A.append(a)
# B=A.copy()
# for i in range(0,10,2):
#     B[i]=A[i+1]
#     B[i+1]=A[i]
# for i in range(10):
#     print(B[i],end=' ')
# cau7
M=[]
n=int(input('n='))
for i in range(n):
    a=int(input())
    M.append(a)
i=0
while i<len(M):
    j=i+1
    while j<len(M):
        if M[i]==M[j]:
            del(M[j])
        else:
            j=j+1
    i=i+1
for a in range(len(M)):
    print(M[a],end=' ')