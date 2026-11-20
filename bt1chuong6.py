s=input()
s=s.lower()
td={}
t=""
for tu in s:
    if tu!=" " :
        t=t+tu
    else:
        if t!="" :
            td[t] = td.get(t, 0) + 1
            t=""
if t!="" :
    td[t] = td.get(t, 0) + 1
print(td)
    

