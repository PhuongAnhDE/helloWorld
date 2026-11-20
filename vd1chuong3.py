a=str(input("Nhập tên:"))
b=int(input("Nhập tuổi:"))
c=str(input("Nhập giới tính:"))
if b<18:
    print(a,c,str(b)+" tuoi", "la tre em", sep=", ")
elif 18<=b<=40 :
     print(a,c,str(b)+" tuoi", "nguoi truong thanh", sep=", ")
elif 40<b<=60 :
     print(a,c,str(b)+" tuoi", "nguoi trung nien", sep=", ")
else :
    print(a,c,str(b)+" tuoi", "nguoi gia", sep=", ")

     
        