n=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in range(len(l)-1,1,-1):
    if(l[i]==l[i-1]+l[i-2]):
        c=1
    else:
        d=d+1
if(c!=0 and d==0):
    print("yes")
else:
    print("no")
        