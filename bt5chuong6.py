td={}
tt=1
while True:
    s=input()
    if s=="":
        break
    ten=""
    tuoi=""
    for tu in s:
        if tu!=" " and tuoi=="":
            ten=ten+tu
        elif tu!=" " and tuoi!="":
            tuoi=tuoi+tu
        elif tu==" ":
            tuoi="0"
    td[tt] = {"name":ten,"age":int(tuoi)}
    tt=tt+1
print(td)