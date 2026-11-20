s=input()
ds=[]
tu=""
for t in s:
    if t!= ",":
        tu=tu+t
    else:
        if tu not in ds:
            ds.append(tu)
        tu=""
if tu not in ds:
    ds.append(tu)
ds.sort()
k=",".join(ds)
print(k)