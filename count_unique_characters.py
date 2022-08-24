n=input().lower()

n=n.replace(" ","")
c=0
for i in n:
    if n.count(i)==1:
        c=c+1
print(c)

