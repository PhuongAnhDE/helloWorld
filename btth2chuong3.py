m1=int(input("M1="))
m2=int(input("M2="))
m3=int(input("M3="))
s=int(input("S="))
gia=int
if 1<=s<=100 :
    gia=s*m1
elif 100< s <= 150 :
    gia=100*m1+(s-100)*m2
else:
      gia=100*m1+50*m2+(s-150)*m3
print(f"Phai tra={gia}")
