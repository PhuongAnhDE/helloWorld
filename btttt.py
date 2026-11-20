print('Nhap dict1:')
dict1={}
while True:
    a=input()
    if a=="":
        break
    gt=input()
    a=int(a)
    gt=int(gt)
    dict1[a]=gt
dict2={}
while True:
    a=input()
    if a=="":
        break
    gt=input()
    a=int(a)
    gt=int(gt)
    dict1[a]=gt
tong=0
for gt in dict1 :
    tong=tong+dict1[gt]
for gt in dict2 :
    tong=tong+dict2[gt]
print(tong)


