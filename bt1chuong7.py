c=input()
h=0
t=0
s=0
k=0
for ch in c:
    if 'A'<=ch<='Z':
        h=h+1
    elif 'a'<=ch<='z':
        t=t+1
    elif '0'<=ch<='9':
        s=s+1
    else:
        k=k+1
print("In hoa:", h)
print("In thuong:", t)
print("Chu so:", s)
print("Khac:", k)
