n=input().lower()
n1=input().lower()
k=set(n)
k1=set(n1)
c=0
for i in k:
    if i in k1 and i!=" ":
        c=c+1
print(c)
        