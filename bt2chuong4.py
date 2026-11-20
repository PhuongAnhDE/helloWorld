def nhapso():
    n=int(input("n="))
    if n>=1 :
        return n
    else:
        print("")
def tinh(n):
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True
def dem(n,d):
    a=0
    d=2
    while a<n:
        if tinh(d):
            print(d, end=", ")
            a=a+1
        d=d+1
n=nhapso()
da=tinh(n)
dem(n,da)
        
    

        
        
    
        