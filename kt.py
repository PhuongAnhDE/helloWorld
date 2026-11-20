n=int(input())
d=0
for j in range(2,n+1):
    kt=1
    for i in range(2,int(j**0.5)+1):
        if j%i==0:
            kt=0
            break
    if kt==1:
        d=d+1
print(d)

                
