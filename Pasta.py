n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=set(b)
c=0
if(len(s)==len(b)):
    for i in b:
        if i in a:
            c=c+1
    if(c==len(b)):
        print("Yes")
    else:
        print("No")
else:
    print("No")