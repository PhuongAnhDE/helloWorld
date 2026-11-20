while True:
    n=int(input("n="))
    if n=="":
        break
    tong=0
    d=0
    t=n
    while t>0 :
        s=t%10
        tong=tong+s
        d=d+1
        t=t//10
    tbc=tong/d
    print(round(tbc,2))