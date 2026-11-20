n=int(input("n="))
b=n
dem=0
if n==0:
    dem=1
else:
    while n>0:
        dem=dem+1
        n=n//10
print(f"{b} co {dem} chu so")
    
    