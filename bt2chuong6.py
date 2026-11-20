s1=input() 
s2=input()   
td={}
t1=""
t2=""
i=0
for tu in s1:
    if tu!=" ":
        t1=t1+tu
    else:
        while i<len(s2) and s2[i]!=" ":
            t2=t2+s2[i]
            i=i+1
        i=i+1
        td[t1]=int(t2)
        t1=""
        t2=""
if t1!="" :
    while i<len(s2):
        t2=t2+s2[i]
        i=i+1
    td[t1]=int(t2)
print(td)