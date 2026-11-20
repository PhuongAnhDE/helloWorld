a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a>=c:
  max=a
  min=c
else :
 max=c
 min=a
if b>max :
    print(f"SLN={b}")
else:
    print(f'SLN={max}')
if b<min:
    print(f'SBN={b}')
else:
    print(f'SBN={min}')