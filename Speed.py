t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    c=1
    for i in range(0,len(arr)-1):
        if(arr[i]>arr[i+1]):
            c=c+1
    print(c)
    t=t-1