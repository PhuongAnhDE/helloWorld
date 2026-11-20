#a
td={}
while True:
    s=input()
    if s=="":
        break
    ten=""
    sl=""
    for tu in s:
        if tu!=" " and sl=="":
            ten=ten+tu
        elif tu!=" " and sl!="":
            sl=sl+tu
        elif tu==" ":
            sl="0"
    if ten not in td:
        td[ten]= int(sl)
print(td)
#b
td={}
while True:
    s=input()
    if s=="":
        break
    ten=""
    sl=""
    for tu in s:
        if tu!=" " and sl=="":
            ten=ten+tu
        elif tu!=" " and sl!="":
            sl=sl+tu
        elif tu==" ":
            sl="0"
    if ten not in td:
        td[ten]= int(sl)
for ten in td:
    if td[ten]>=200:
        print(ten, end=", ")
#c
td={}
while True:
    s=input()
    if s=="":
        break
    ten=""
    sl=""
    for tu in s:
        if tu!=" " and sl=="":
            ten=ten+tu
        elif tu!=" " and sl!="":
            sl=sl+tu
        elif tu==" ":
            sl="0"
    if ten not in td:
        td[ten]= int(sl)
tong=0
for ten in td:
    tong=tong+td[ten] 
print(tong)
# d
td={}
while True:
    s=input()
    if s=="":
        break
    ten=""
    sl=""
    for tu in s:
        if tu!=" " and sl=="":
            ten=ten+tu
        elif tu!=" " and sl!="":
            sl=sl+tu
        elif tu==" ":
            sl="0"
    if ten not in td:
        td[ten]= int(sl)
tdk={}
for ten in td:
    if td[ten]>100:
        tdk[ten]=td[ten]
print(tdk)
#e
td={}
while True:
    s=input()
    if s=="":
        break
    ten=""
    sl=""
    for tu in s:
        if tu!=" " and sl=="":
            ten=ten+tu
        elif tu!=" " and sl!="":
            sl=sl+tu
        elif tu==" ":
            sl="0"
    if ten not in td:
        td[ten]= int(sl)
kt=input()
if kt in td:
    td[kt]=td[kt]+100   
print(td)


        


        
        
        