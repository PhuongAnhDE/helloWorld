s=int(input("S="))
a=int
a=(s//3600)
b=int
b=(((s%3600)/60)//1)
c=int
c=((((s%3600)/60)%1)*60)
print(f"Thoi gian la {a} gio {int(b)} phut {int(round(c,1))} giay")