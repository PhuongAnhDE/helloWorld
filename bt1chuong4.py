def nhapso():
    while True:
        try:
            n=int(input("n="))
            if 2<=n<=100:
                return n
            else:
                print("")
        except :
                print("")
def tinh(n):
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True
def inra(n,da):
    if da:
        print(f"{n} la SNT")
    else:
        print(f"{n} khong la SNT")
n=nhapso()
da=tinh(n)
inra(n,da)
        