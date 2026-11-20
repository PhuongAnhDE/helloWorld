def Lasonguyento(n):
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True
def Sohople(n):
    if n<= 1:
        return True
    return False
def Nhapvadem():
    dem = 0
    print('Nhap day so:')
    while True:
        n= int(input())
        if Sohople(n):
            break
        elif Lasonguyento(n):
            dem=dem+1
    return dem
def inketqua(kq):
    print('Co', kq, 'so nguyen to')
kq=Nhapvadem()
inketqua(kq)