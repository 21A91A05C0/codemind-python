n=int(input())
arr=list(map(int,input().split()))
c1=0
b=0
for i in arr:
    b=arr.count(i)
    if(b==i):
        c1=c1+1
        if(b>1):
            arr.remove(i)
print(c1)