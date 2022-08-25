n=input().lower().split(" ")
a=n[0]
k=""
d=0
c=0
for i in a:
    c=0
    for j in range(1,len(n)):
        if i in n[j]:
            c=c+1
    if(c==(len(n)-1)):
        d=d+1
        k=k+i
if(len(k)!=0):
    print(min(k))
else:
    print("-1")
    