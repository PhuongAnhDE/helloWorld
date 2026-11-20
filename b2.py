n=int(input("Nhap so gio: "))

for i in range(n):
    if n>0:
        lp=0
        if 0<n<=2:
            lp=2*5000
        elif 3<=n<=10:
            lp=10000+(n-2)*3000
        else:
            lp=10000+24000+(n-10)*2000
    else:
        exit
print("Le phi:",lp)

