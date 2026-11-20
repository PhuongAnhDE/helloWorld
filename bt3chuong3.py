a=float(input("Tieu thu="))
gia=float
vat=float
if 1<=a<=100 :
    gia=a*550
elif 100<a<=150 :
     gia=55000+(a-100)*750
elif 150<a<=200 :
      gia=92500+(a-150)*950
else :
    gia=140000+(a-200)*1350
vat=gia*0.1
print(f"Phai tra={int(gia+vat)}")

    
    