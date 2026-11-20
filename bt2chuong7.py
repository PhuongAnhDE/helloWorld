s=input()
s=s.strip()
s=s.lower()
a=s.split()
s=" ".join(a)
s=s.replace(" ,", ",")
s=s.replace(" .", ".")
s=s.replace(" ;", ";")
s=s.replace(" :", ":")
s2=""
for i in range(len(s)):
    if i==0:
        s2=s2+s[i].upper()
    else:
        s2=s2+s[i]
s=s2
print(s)