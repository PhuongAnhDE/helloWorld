import math
def nhapso():
    print("Nhap 3 so nguyen:")
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    return a,b,c
def giaipt(a,b,c):
    d= b*b-4*a*c
    if d<0:
        m="vn"
        return m,None,None
    elif d==0:
        x1=-b/(2*a)
        m="nk"
        f=x1
        return m,f,None
    else:
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
        m="2n"
        f=x1
        g=x2
        return m,f,g
def inkq(m,f,g):
    if m=="vn":
        print("Phuong trinh vo nghiem")
    if m=="nk":
        print("Phuong trinh co nghiem kep")
        print(f"x1=x2={f}")
    if m=="2n":
        print("Phuong trinh co hai nghiem")
        print(f"x1={f}")
        print(f"x2={g}")
a,b,c=nhapso()
if a==0 and b!=0 and c!=0:
    print("Phuong trinh co nghiem")
    print(f'x={-c/b}')
elif a==0 and b==0 and c!=0:
    print("Phuong trinh vo nghiem") 
elif a==0 and b==0 and c==0:
    print("Phuong trinh vo nghiem")
else:
    m,f,g=giaipt(a,b,c)
    inkq(m,f,g)


