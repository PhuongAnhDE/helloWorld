while True:
    n=int(input("n="))
    if n<0 or n>100 :
        break
    elif 0<=n<=100 :
        i=1
        l=1
        while i<=n :
            l=l*i
            i=i+1
        print(f'{n}!={l}',sep="")
        break

    

