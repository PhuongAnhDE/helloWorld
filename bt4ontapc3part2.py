while True:
    a = float(input("a="))
    b = int(input("b="))
    c = input("Toan tu:")
    d=float
    if c=="+":
        d=a+b
    elif c=="-":
        d=a-b
    elif c=="*":
        d=a*b
    elif c=="/":
        if b==0:
            print("")
            break
        else:
            d=a/b
            continue
    else:
        print("")
        continue
    t=input("Tiep tuc:")
    if t== "t" or t=="T":
        if d-int(d)!=0 :
            print(f"{a}{c}{b}={d}")
        else:
            print(f"{a}{c}{b}={round(d)}")
        break
   