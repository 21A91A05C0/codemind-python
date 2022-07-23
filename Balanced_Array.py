t=int(input())
while(t>0):
    a=int(input())
    arr=list(map(int,input().split()))
    s=0
    l=0
    flag=0
    for i in range(len(arr)):
        s=sum(arr[:i])
        l=sum(arr[i+1:])
        if(s==l):
            flag=1
            break
    if(flag==1):
        print("YES")
    else:
        print("NO")
    t=t-1