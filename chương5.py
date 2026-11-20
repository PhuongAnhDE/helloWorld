# L=["An", "Binh", "Nam"]
# while True:
#     a=input()
#     if a in L:
#         print("Da ton tai")
#     else:
#         L.append(a)
#         print(L)
#         break
# N=[]
# for i in range(10):
#     a=int(input())
#     N.append(a)
# x=int(input("x="))
# b=5
# for i in range(10):
#     if N[i]==b :
#         N[i]=x
#     print(N[i],end=",")
# print()
# while x in N:
#     N.remove(x)
# for i in range(len(N)):
#     print(N[i],end=',')
# numbers=[1,2,3]
# numbers.extend('python')
# print(numbers)
names = ["An", "Nam", 'Binh', 'Ngoc']
names.remove('An')
del(names[0])
x=names.pop(-2)
print(x)
print(names)