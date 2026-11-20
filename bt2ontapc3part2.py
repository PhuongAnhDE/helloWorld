try:
    n=int(input("n="))
    if 2<=n<=100:
        snt=True
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                snt= False
                break
        if snt == True:
            print(f"{n} la SNT")
        else:
            print(f"{n} khong la SNT")
    else:
        print("")
except ValueError:
    print("")
        
        