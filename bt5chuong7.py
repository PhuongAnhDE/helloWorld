s=input()
x=int(input())
a=s.split()
d=0
for i in range(len(a)):
    if int(a[i])==x:
        i=i+1
        print(i)
        d=d+1
if d==0:
    print(0)