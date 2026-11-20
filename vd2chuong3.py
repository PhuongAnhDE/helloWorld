a=float(input("nhap diem mon toan:"))
b=float(input("nhap diem mon van:"))
c=float(input("nhap diem mon anh:"))
d=(a+b+c)/3
if d>=9:
        print("Dau NV1")
elif 8<=d<=9:
         print("Dau NV2")
elif 7<=d<=8:
          print("Dau NV3")
elif 6<=d<=7:
         print("Dau NV4")
elif d<6:
         print("Thi rot")
else :
        if a==0 or b==0 or c==0:
            print("thi rot")
        
        
