#a
for i in range (9,0,-1):
     j=1
     for j in range (i):
         print("$",end="")
         j=j+1 
     print("")
#b
n=9
i=1
for i in range (1,n+1):
    l = 1
    for l in range (n-i):
        print(" ", end="")
    j=1    
    for j in range (2*i-1):
        print("*",end="")    
    print("")
   
        