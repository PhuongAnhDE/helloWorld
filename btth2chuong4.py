def nhapso():
    n=int(input("n="))
    while n<2:
        print("")
        break
    return n
def inkq(n):
    sc=0 
    d=2      
    while sc<(n-1)/2:
        if d%2==0:
            print(d,end=" ")
            sc=sc+1
        d=d+1
    print("")
def tieptuc():
    k=input("Tiep tuc khong?") 
    return k
k=""
while k!="K" and k!="k":
    n=nhapso()
    inkq(n)
    k=tieptuc()

    
    
    