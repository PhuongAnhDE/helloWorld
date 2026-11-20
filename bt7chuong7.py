s=input()
e=""
d=0  
i=0
while i<len(s):
    if s[i]=='E':
        if s[i:i+6]=="Email:":
            d="True"
            i=i+6
            continue
    if d=="True":
        if s[i]!=" ":
            e=e+s[i]
    i=i+1
print(e)