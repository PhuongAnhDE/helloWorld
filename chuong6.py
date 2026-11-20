# L=[]
# M=[]
# n=int(input("n="))
# for i in range(n):
#     a=int(input())
#     L.append(a)
# for i in L:
#     if i not in M:
#         M.append(i)
# for i in M:
#     print(i,end=" ")

# d={}
# l=[]
# m=[]
# c=input()
# c=c+' '
# s=input()
# s=s+' '
# st=''
# sa=''
# a=0
# b=0
# for i in range(len(c)):
#     for i in s:
#         if i!=' ':
#             sa=sa+i
#             m.append(sa)
#         else:
#             sa=''
#     for i in c:
#         if i!=' ':
#             st=st+i
#         else:
#             l.append(st)
#             st=''
# for i in range(len(c)):
#     a=l[i]
#     b=int(m[i])
#     d[a]=b
#     a=0
#     b=0
# print(d)

# d={}
# while True:
#     l=[]
#     a=0
#     b=0
#     n=input()
#     if n=='':
#         break
#     l=n.split()
#     a=l[0]
#     b=int(l[1])
#     d[a]=b
# print(d)

d={}
while True:
    l=[]
    a=0
    b=0
    n=input()
    if n=='':
        break
    l=n.split()
    a=l[0]
    b=int(l[1])
    d[a]=b
for i in d:
    if d[i]>=200:
        print(i,end=',')

    
        
    
    
    


        
    
    