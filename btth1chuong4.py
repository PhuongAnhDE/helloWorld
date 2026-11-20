def nhap():
    n=int(input("n="))
    while n>=0:
        return n
    if n<0:
        print("loi")
def giaithua(n):
    i=1
    gt=1
    while i<=n:
        gt=gt*i
        i=i+1
    return gt
def inkq(n,gt):
    if n>0:
        print(f"{n}!={gt}",sep="")
    elif n==0:
        print(f"{n}!=1",sep="")
n=nhap()
if n<0:
    print("")
kq=giaithua(n)
inkq(n,kq)
    