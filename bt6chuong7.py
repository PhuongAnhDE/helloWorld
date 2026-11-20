s=input()
a=s.split(",")
kq=[]
for x in a:
    if int(x,2)%3==0:
        kq.append(x)
k=",".join(kq)
print(k)
