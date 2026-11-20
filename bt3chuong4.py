def nhapso():
    x=float(input('x='))
    y=float(input('y='))
    return x,y
def toantu():
    ch=input('Phep toan:')
    return ch
def tinh(x,y,ch):
    if ch == "+" :
        print(f"{x}{ch}{y}={x+y}")
    elif ch == "-" :
        print(f"{x}{ch}{y}={x-y}")
    elif ch == "*" :
       print(f"{x}{ch}{y}={x*y}")
    elif ch == "/" :
        if y==0:
            print('Khong hop le')
        else:
            print(f"{x}{ch}{y}={x/y}")
    else:
        print('Khong hop le')
def tieptuc():
    t=input("Tiep tuc:") 
    return t
t=""
while t!="t" and t!="T":
    x,y=nhapso()
    ch=toantu()
    tinh(x,y,ch)
    t=tieptuc()

    
    


    