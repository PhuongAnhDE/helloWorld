def nhap():
        m1=int(input("M1 = "))
        m2=int(input("M2 = "))
        s=int(input("S = "))
        return m1,m2,s
m1=0
m2=0
s=0
def tinh(m1,m2,s):
    if m1==0 and m2==0 and s==0:
        t=s*m1
        pt=t*1.1
    elif 0<=s<=100 :
        t=s*m1
        pt=t*1.1
    else:
        t=100*m1+(s-100)*m2
        pt=t*1.1
    return pt
while True:
    print("CONG VIEC")
    print("----------------------------------")
    print("So 1: Nhap M1, M2 va S")
    print("So 2: Tinh so tien phai tra")
    print("So 0: Thoat")
    print("----------------------------------")
    c=input("Moi ban chon cong viec: ")
    if c=="1" :
        m1,m2,s=nhap()
    elif c=="2":
        if m1==0 and m2==0 and s==0:
            pt=tinh(m1,m2,s)
            print("So dien nang tieu thu la:",s,"chu")
            print("so tiem phai tra la:",pt)
        else:
            pt=tinh(m1,m2,s)
            print("So dien nang tieu thu la:",s,"chu")
            print("so tien phai tra la:",pt)
    elif c=="0":
        break
    
    
        
    
    
    
    
    