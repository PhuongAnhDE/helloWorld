# def Lasomayman(n):
#     tong=0
#     d=0
#     t=n
#     while t>0 :
#         
#         s=t%10
#         tong=tong+s
#         d=d+1
#         t=t//10
#     if tong%6==0 and tong%8==0:
#         return True
#     return False
# def Sohople(n):
#     if n<= 1:
#         return True
#     return False
# def tieptuc(n):
#     N=input()
#     if n=="T":
#         return False
#     return True
# def Nhapvadem():
#     dem = 0
#     print()
#     while True:
#         n=str(input())
#         if Sohople(n):
#             break
#         elif Lasomayman(n):
#             dem=dem+1
#     return dem
# def inketqua(kq):
#     if tieptuc():
#         print(f'So luong so may ma la;{kq}')
# kq=Nhapvadem()
# inketqua(kq)
#
dem=0
while True:
    n=input()
    if n=="T":
        break
    else:
        S=0
        for i in range (len(n)):
            S=S+int(n[i])
        if S%6==0 and S%8==0:
            dem=dem+1
print("So hoan hao la:",dem,'so')
            