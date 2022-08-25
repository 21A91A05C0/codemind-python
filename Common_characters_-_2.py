n=input().lower().split()
p=n[0]
d=0
c=0
for i in p:
    c=0
    for j in range(1,len(n)):
        if i in n[j]:
            c=c+1
    if(c==len(n)-1):
        d=d+1
print(d)