t=int(input())

while(t>0):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    arr1=list(map(int,input().split()))
    res=0
    res=arr+arr1
    print(*(sorted(res)))
    t=t-1