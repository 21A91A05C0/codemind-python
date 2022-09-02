t=int(input())
while(t>0):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    res=n-m
    k=[]
    for i in range(len(arr)):
        k.append(arr[(n-m+i)%n])
    print(*k)
        
    t=t-1